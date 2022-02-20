from typing import List, Tuple
from Tokenizer import Token


def build_suffix_array(tokenArray: List[Token]) -> Tuple[List[int], List[int]]:
    n: int = len(tokenArray)
    suffixes: List[__Suffix] = [__Suffix() for _ in range(n)]

    for i in range(n):
        suffixes[i].index = i
        suffixes[i].rank[0] = tokenArray[i].ID
        suffixes[i].rank[1] = tokenArray[i + 1].ID if ((i + 1) < n) else -1

    suffixes = sorted(
        suffixes, key=lambda x: (
            x.rank[0], x.rank[1]))

    ind: List[int] = [0] * n
    k: int = 4
    while k < 2 * n:
        rank: int = 0
        prev_rank: int = suffixes[0].rank[0]
        suffixes[0].rank[0] = rank
        ind[suffixes[0].index] = 0

        for i in range(1, n):
            if (suffixes[i].rank[0] == prev_rank and
                    suffixes[i].rank[1] == suffixes[i - 1].rank[1]):
                prev_rank = suffixes[i].rank[0]
                suffixes[i].rank[0] = rank
            else:
                prev_rank = suffixes[i].rank[0]
                rank += 1
                suffixes[i].rank[0] = rank
            ind[suffixes[i].index] = i

        for i in range(n):
            nextindex: int = suffixes[i].index + k // 2
            suffixes[i].rank[1] = suffixes[ind[nextindex]].rank[0] \
                if (nextindex < n) else -1

        suffixes = sorted(
            suffixes, key=lambda x: (
                x.rank[0], x.rank[1]))

        k *= 2

    suffixArray: List[int] = [0] * n

    for i in range(n):
        suffixArray[i] = suffixes[i].index

    return suffixArray, __build_LCP_array(tokenArray, suffixArray)


class __Suffix:
    def __init__(self) -> None:
        self.index: int = 0
        self.rank: List[int] = [0, 0]


def __build_LCP_array(tokenArray: List[Token], suffixArray: List[int]) -> List[int]:
    LCP: List[int] = [0]
    for idx in range(len(tokenArray) - 1):
        i: int = suffixArray[idx]
        q: int = suffixArray[idx + 1]
        common: int = 0
        while (i < len(tokenArray) and
               q < len(tokenArray) and
               tokenArray[i].ID == tokenArray[q].ID):
            common += 1
            i += 1
            q += 1

        LCP.append(common)

    return LCP
