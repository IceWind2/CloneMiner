from typing import Callable, List, Union

from TextDuplicateSearch.DataModels.DuplicateCase import DuplicateCase
from TextDuplicateSearch.DataModels.DuplicateCollection import DuplicateCollection
from TextDuplicateSearch.DataModels.SearchConfig import SearchConfig
from TextDuplicateSearch.DataModels.TextModel import TextModel
from TextDuplicateSearch.DataModels.TextFragment import TextFragment
from TextDuplicateSearch.DuplicateSearch.DuplicateSearcher import DuplicateSearcher
from TextDuplicateSearch.DuplicateSearch.FuzzySearch.Tools.Hashing import Hashing
from TextDuplicateSearch.TextProcessing.Token import Token


class FragmentSearch(DuplicateSearcher):
    def __init__(self, hashin_func: Callable[[List[Token]], int],
                 editdistance_func: Callable[[TextFragment, TextFragment, float], float],
                 search_config: SearchConfig) -> None:
        super().__init__(search_config)
        self.hashin_func: Callable[[List[Token]], int] = hashin_func
        self.editdistance_func: Callable[[TextFragment, TextFragment, float], float] = editdistance_func
        self.text_model: TextModel = TextModel([])

        self.duplicates: List[List[int]] = []
        self.visited: List[bool] = []
        self.collection: Union[DuplicateCollection, None] = None

    def find_duplicates(self, text_model: TextModel) -> DuplicateCollection:
        self.text_model = text_model
        text_model.split_into_parts(self.config.fragment_size)

        self.duplicates = self._get_duplicates(text_model.parts)
        self.visited = [False for _ in range(len(text_model.parts))]

        if self.config.precise_grouping:
            self.collection = self._precise_grouping()
        else:
            self.collection = self._imprecise_grouping()

        merged: List[int] = []
        for i in range(len(self.collection.cases)):
            for j in range(i + 1, len(self.collection.cases)):
                if self._merge_groups(self.collection.cases[i], self.collection.cases[j]):
                    merged.append(i)
                    break

        self.collection.cases = [case for i, case in enumerate(self.collection.cases) if i not in merged]

        return self.collection

    # Constructs adjacency list for similar fragments
    def _get_duplicates(self, fragments: List[TextFragment]) -> List[List[int]]:
        duplicates: List[List[int]] = []
        current_list: List[int]

        for i in range(len(fragments)):
            current_list = []
            for j in range(len(fragments)):
                if i == j:
                    continue

                hash_i = self.hashin_func(fragments[i].tokens)
                hash_j = self.hashin_func(fragments[j].tokens)

                if Hashing.get_diff(hash_i, hash_j) > self.config.max_hashing_diff:
                    continue

                edit_dist = self.editdistance_func(fragments[i],
                                                   fragments[j],
                                                   self.config.max_edit_distance)

                if edit_dist <= self.config.max_edit_distance:
                    current_list.append(j)

            duplicates.append(current_list)

        return duplicates

    # Finds graph components via DFS
    def _imprecise_grouping(self) -> DuplicateCollection:
        result: DuplicateCollection = DuplicateCollection()

        for i in range(len(self.visited)):
            if self.visited[i]:
                continue

            group: List[int] = []
            self._dfs(i, group)
            dup_case: DuplicateCase = DuplicateCase()

            if len(group) < 2:
                continue

            for fragment in group:
                dup_case.add_text_fragment(self.text_model.parts[fragment])

            result.add_case(dup_case)

        return result

    # Finds all max cliques via Bron–Kerbosch algorithm
    def _precise_grouping(self) -> DuplicateCollection:
        pass

    def _dfs(self, current: int, component: List[int]) -> None:
        self.visited[current] = True
        component.append(current)

        for neighbor in self.duplicates[current]:
            if not self.visited[neighbor]:
                self._dfs(neighbor, component)

    def _merge_groups(self, case_a: DuplicateCase, case_b: DuplicateCase) -> bool:
        if len(case_a.text_fragments) != len(case_b.text_fragments):
            return False

        if not all(case_a.text_fragments[i].is_neighbor(case_b.text_fragments[i]) for i in range(len(case_b.text_fragments))):
            return False

        for i in range(len(case_b.text_fragments)):
            case_b.text_fragments[i].merge_with(case_a.text_fragments[i])

        return True
