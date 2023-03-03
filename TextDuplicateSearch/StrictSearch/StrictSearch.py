from typing import List

from TextDuplicateSearch.DataModels.Configs.SearchConfig import SearchConfig
from TextDuplicateSearch.DataModels.DuplicateCollection import DuplicateCollection
from TextDuplicateSearch.DataModels.DuplicateCase import DuplicateCase
from TextDuplicateSearch.DataModels.TextFragment import TextFragment
from TextDuplicateSearch.StrictSearch import SuffixArray
from TextDuplicateSearch.TextProcessing.Token import Token


class StrictSearch:
    suffix_array: List[int] = []
    lcp_array: List[int] = []

    class Interval:
        def __init__(self):
            self.is_active: bool = False
            self.is_nested: bool = True
            self.begin: int = -1
            self.end: int = -1

        def set(self, begin, end):
            self.begin = begin
            self.end = end
            self.is_active = True

        def reset(self):
            self.is_active: bool = False
            self.is_nested: bool = True
            self.begin: int = 0
            self.end: int = 0

    @staticmethod
    def get_duplicate_data(tokens: List[Token], search_config: SearchConfig) -> DuplicateCollection:
        StrictSearch.suffix_array, StrictSearch.lcp_array = SuffixArray.build_from_tokens(tokens)

        result: DuplicateCollection = DuplicateCollection(tokens)
        marked: List[bool] = [False] * len(tokens)
        cur_idx: int = 1
        group_interval: StrictSearch.Interval = StrictSearch.Interval()

        # going through suffix array
        while cur_idx < len(marked):
            if StrictSearch.lcp_array[cur_idx] >= search_config.min_dup_length:
                if not marked[StrictSearch.suffix_array[cur_idx]]:
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
                length: int = min(StrictSearch.lcp_array[group_interval.begin + 1: group_interval.end + 1])

                # trying to go backwards from starting tokens
                expand: bool = True
                shift: int = 1
                while expand:
                    cur_token: Token = tokens[StrictSearch.suffix_array[group_interval.begin] - shift]
                    for idx in range(group_interval.begin + 1, group_interval.end + 1):
                        if tokens[StrictSearch.suffix_array[idx] - shift] != cur_token:
                            expand = False

                    if expand:
                        shift += 1

                    if StrictSearch.suffix_array[group_interval.begin] - shift < 0:
                        break

                shift -= 1

                for idx in range(group_interval.begin, group_interval.end + 1):
                    fragment: TextFragment = TextFragment(tokens[StrictSearch.suffix_array[idx] - shift], tokens[StrictSearch.suffix_array[idx] + length - 1])
                    dup_case.add_text_fragment(fragment)
                    marked[StrictSearch.suffix_array[idx] - shift : StrictSearch.suffix_array[idx] + length] = [True] * (shift + length)

                result.add_case(dup_case)

                group_interval.reset()

            cur_idx += 1

        return result
