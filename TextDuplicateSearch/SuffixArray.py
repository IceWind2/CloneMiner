from typing import List, Tuple

from TextDuplicateSearch.Tokenizer import Token


def build_from_tokens(tokens: List[Token]) -> Tuple[List[int], List[int]]:
    token_ids: List[int] = [token.ID for token in tokens]
    suffix_array: List[int] = _build_suffix_array(token_ids)
    lcp_array: List[int] = _build_lcp_array(token_ids, suffix_array)
    return suffix_array, lcp_array


def build_from_string(text: str) -> Tuple[List[int], List[int]]:
    text_int: List[int] = [int(char) for char in text]
    suffix_array: List[int] = _build_suffix_array(text_int)
    lcp_array: List[int] = _build_lcp_array(text_int, suffix_array)
    return suffix_array, lcp_array


def build_from_array(array: List[int]) -> Tuple[List[int], List[int]]:
    suffix_array: List[int] = _build_suffix_array(array)
    lcp_array: List[int] = _build_lcp_array(array, suffix_array)
    return suffix_array, lcp_array


class _Suffix:
    def __init__(self) -> None:
        self.position: int = -1
        self.first_rank: int = -1
        self.second_rank: int = -1


# O(n log^2 n)
# take suffixes sorted on first 2^i chars, split into equivalence classes,
# for each suffix @i take suffix @i+2^i and sort pairs => sorted on first 2^(i+1) chars
def _build_suffix_array(input_array: List[int]) -> List[int]:
    n: int = len(input_array)
    suffixes: List[_Suffix] = [_Suffix() for _ in range(n)]

    for i in range(n):
        suffixes[i].position = i
        suffixes[i].first_rank = input_array[i]
        suffixes[i].second_rank = input_array[i + 1] if ((i + 1) < n) else -1

    suffixes = sorted(
        suffixes, key=lambda x: (
            x.first_rank, x.second_rank
        )
    )

    current_idx: List[int] = [0] * n
    k: int = 4

    while k < 2 * n:
        new_rank: int = 0
        prev_rank: int = suffixes[0].first_rank
        suffixes[0].first_rank = new_rank
        current_idx[suffixes[0].position] = 0

        for i in range(1, n):
            if (suffixes[i].first_rank == prev_rank and
                    suffixes[i].second_rank == suffixes[i - 1].second_rank):
                suffixes[i].first_rank = new_rank
            else:
                prev_rank = suffixes[i].first_rank
                new_rank += 1
                suffixes[i].first_rank = new_rank
            current_idx[suffixes[i].position] = i

        for i in range(n):
            paired_suffix_pos: int = suffixes[i].position + k // 2
            suffixes[i].second_rank = suffixes[current_idx[paired_suffix_pos]].first_rank \
                if (paired_suffix_pos < n) else -1

        suffixes = sorted(
            suffixes, key=lambda x: (
                x.first_rank, x.second_rank
            )
        )

        k *= 2

    result: List[int] = [suffix.position for suffix in suffixes]

    return result


# O(n)
def _build_lcp_array(input_array: List[int], suffix_array: List[int]) -> List[int]:
    n: int = len(input_array)
    result: List[int] = [-1] * n

    inv_suffix: List[int] = [-1] * n
    for idx in range(n):
        inv_suffix[suffix_array[idx]] = idx

    common: int = 0
    for idx in range(1, n):
        if inv_suffix[idx] == 0:
            common = 0
            continue

        prev_idx: int = suffix_array[inv_suffix[idx] - 1]
        while (idx + common < n and
               prev_idx + common < n and
               input_array[idx + common] == input_array[prev_idx + common]):
            common += 1

        result[inv_suffix[idx]] = common
        if common > 0:
            common -= 1

    return result
