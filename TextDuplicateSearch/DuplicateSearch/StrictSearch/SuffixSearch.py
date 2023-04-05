from typing import List

from TextDuplicateSearch.DataModels.TextModel import TextModel
from TextDuplicateSearch.DataModels.SearchConfig import SearchConfig
from TextDuplicateSearch.DataModels.DuplicateCollection import DuplicateCollection
from TextDuplicateSearch.DataModels.DuplicateCase import DuplicateCase
from TextDuplicateSearch.DataModels.TextFragment import TextFragment
from TextDuplicateSearch.DuplicateSearch.DuplicateSearcher import DuplicateSearcher
from TextDuplicateSearch.DuplicateSearch.StrictSearch import SuffixArray
from TextDuplicateSearch.TextProcessing.Token import Token
from TextDuplicateSearch.DuplicateSearch.DuplicateMerge.MergeFunctions import merge_duplicate_groups


class SuffixSearch(DuplicateSearcher):
    def __init__(self, search_config: SearchConfig) -> None:
        super().__init__(search_config)
        self.suffix_array: List[int] = []
        self.lcp_array: List[int] = []

    def find_duplicates(self, text_model: TextModel) -> DuplicateCollection:
        self.suffix_array, self.lcp_array = SuffixArray.build_from_tokens(text_model.tokens)

        result: DuplicateCollection = DuplicateCollection()
        marked: List[bool] = [False] * len(text_model.tokens)
        cur_idx: int = 1
        group_interval: Interval = Interval()

        # going through suffix array
        while cur_idx < len(marked):
            if self.lcp_array[cur_idx] >= self.config.min_dup_length:
                if not marked[self.suffix_array[cur_idx]]:
                    group_interval.is_nested = False

                if not group_interval.is_active:
                    group_interval.set(cur_idx - 1, cur_idx)
                else:
                    group_interval.end += 1

            else:
                if not group_interval.is_active or group_interval.is_nested:
                    cur_idx += 1
                    group_interval.reset()
                    continue

                dup_case: DuplicateCase = DuplicateCase()

                # forward from starting tokens
                length: int = min(self.lcp_array[group_interval.begin + 1: group_interval.end + 1])

                # trying to go backwards from starting tokens
                expand: bool = True
                shift: int = 1
                while expand:
                    cur_token: Token = text_model.tokens[self.suffix_array[group_interval.begin] - shift]

                    for idx in range(group_interval.begin + 1, group_interval.end + 1):
                        if marked[self.suffix_array[idx] - shift] or \
                                text_model.tokens[self.suffix_array[idx] - shift] != cur_token:
                            expand = False

                    if expand:
                        shift += 1

                    if self.suffix_array[group_interval.begin] - shift < 0:
                        break

                shift -= 1

                for idx in range(group_interval.begin, group_interval.end + 1):
                    fragment: TextFragment = TextFragment(text_model.tokens[self.suffix_array[idx] - shift:
                                                                            self.suffix_array[
                                                                                idx] + length])
                    dup_case.add_fragment(fragment)
                    marked[self.suffix_array[idx] - shift: self.suffix_array[idx] + length] = [True] * (shift + length)

                result.add_case(dup_case)

                group_interval.reset()

            cur_idx += 1

        merge_duplicate_groups(result)

        return result


class Interval:
    def __init__(self) -> None:
        self.is_active: bool = False
        self.is_nested: bool = True
        self.begin: int = -1
        self.end: int = -1

    def set(self, begin: int, end: int) -> None:
        self.begin = begin
        self.end = end
        self.is_active = True

    def reset(self) -> None:
        self.is_active = False
        self.is_nested = True
        self.begin = 0
        self.end = 0
