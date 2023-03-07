from typing import Dict, List

from TextDuplicateSearch.DataModels.TextFragment import TextFragment


class EditDistance:
    _edit_costs: Dict[str, float] = {
        "delete": 1,
        "insert": 1,
        "substitute": 1,
        "transpose": 1
    }

    @staticmethod
    def define_costs(*, delete: float = 1, insert: float = 1, substitute: float = 1, transpose: float = 1):
        EditDistance._edit_costs["delete"] = delete
        EditDistance._edit_costs["insert"] = insert
        EditDistance._edit_costs["substitute"] = substitute
        EditDistance._edit_costs["transpose"] = transpose

    # Damerau-Levenshtein distance:
    #   - edit operations: deletions, insertions, substitutions, transposition
    #   - complexity: O(M * N), where M,N - fragment lengths
    @staticmethod
    def damerau_levenshtein(frg_a: TextFragment, frg_b: TextFragment) -> float:
        dist_a: Dict[int, int] = {}
        n: int = len(frg_a.tokens)
        m: int = len(frg_b.tokens)
        max_dist: int = n + m

        dist: List[List[float]] = [[max_dist for _ in range(m + 2)] for _ in range(n + 2)]
        for i in range(n + 1):
            dist[i][0] = i
        for j in range(m + 1):
            dist[0][j] = j

        for i in range(1, n + 1):
            dist_b: int = 0
            for j in range(1, m + 1):
                k: int = dist_a[frg_b.tokens[j - 1].id] if frg_b.tokens[j - 1].id in dist_a else 0
                l: int = dist_b

                sub_cost: float = EditDistance._edit_costs["substitute"]
                trans_cost = EditDistance._edit_costs["transpose"] + \
                            (i - k - 1) * EditDistance._edit_costs["delete"] + \
                            (j - l - 1) * EditDistance._edit_costs["insert"]

                if frg_a.tokens[i - 1].id == frg_b.tokens[j - 1].id:
                    dist_b = j
                    sub_cost = 0

                dist[i][j] = min(dist[i - 1][j - 1] + sub_cost,
                                 dist[i][j - 1] + EditDistance._edit_costs["insert"],
                                 dist[i - 1][j] + EditDistance._edit_costs["delete"],
                                 dist[k - 1][l - 1] + trans_cost)

            dist_a[frg_a.tokens[i - 1].id] = i

        return dist[n][m]
