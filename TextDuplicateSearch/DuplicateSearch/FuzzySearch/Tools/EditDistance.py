from typing import Dict, List, Tuple
import math

from TextDuplicateSearch.DataModels.TextFragment import TextFragment


class EditDistance:
    _edit_costs: Dict[str, float] = {
        "delete": 1,
        "insert": 1,
        "substitute": 1,
        "transpose": 1
    }

    @staticmethod
    def define_costs(*, delete: float = -1, insert: float = -1, substitute: float = -1, transpose: float = -1) -> None:
        if delete != -1:
            EditDistance._edit_costs["delete"] = delete
        if insert != -1:
            EditDistance._edit_costs["insert"] = insert
        if substitute != -1:
            EditDistance._edit_costs["substitute"] = substitute
        if transpose != -1:
            EditDistance._edit_costs["transpose"] = transpose

    # Calculates Damerau-Levenshtein distance:
    #   - edit operations: deletions, insertions, substitutions, transposition
    #   - complexity: O(M * N), where M,N - fragment lengths
    @staticmethod
    def damerau_levenshtein(frg_a: TextFragment, frg_b: TextFragment, threshold: float = 0) -> float:
        dist_a: Dict[int, int] = {}
        n: int = len(frg_a.tokens)
        m: int = len(frg_b.tokens)
        max_dist: int = n + m

        dist: List[List[float]] = [[max_dist for _ in range(m + 2)] for _ in range(n + 2)]
        dist[n][m] = 0
        for i in range(n + 1):
            dist[i][0] = i * EditDistance._edit_costs["delete"]
        for j in range(m + 1):
            dist[0][j] = j * EditDistance._edit_costs["insert"]

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

    # Calculates Levenshtein distance:
    #   - edit operations: deletions, insertions, substitutions
    #   - complexity: O(t * min(M, N)), where M,N - fragment lengths, t - threshold
    @staticmethod
    def ukkonen_asm(frg_a: TextFragment, frg_b: TextFragment, threshold: float = -1) -> float:
        if frg_a.length == 0 and frg_b.length == 0:
            return 0

        swapped: bool = False
        if frg_a.length > frg_b.length:
            frg_a, frg_b = frg_b, frg_a
            EditDistance.define_costs(insert=EditDistance._edit_costs["delete"],
                                      delete=EditDistance._edit_costs["insert"])
            swapped = True

        if threshold == -1:
            threshold = frg_a.length * EditDistance._edit_costs["delete"] + \
                        frg_b.length * EditDistance._edit_costs["insert"]

        c_min: float = min(EditDistance._edit_costs["delete"], EditDistance._edit_costs["insert"])
        m: int = frg_a.length
        n: int = frg_b.length
        dist: Dict[Tuple[int, int], float] = {}
        p: int = math.floor((threshold / c_min - math.fabs(n - m)) / 2)

        if threshold / c_min < math.fabs(n - m):
            return math.inf

        for i in range(0, m + 1):
            for j in range(max(0, i - p), (min(n, i + (n - m) + p)) + 1):
                val_sub: float = dist[(i - 1, j - 1)] if (i - 1, j - 1) in dist else math.inf
                val_del: float = dist[(i - 1, j)] if (i - 1, j) in dist else math.inf
                val_ins: float = dist[(i, j - 1)] if (i, j - 1) in dist else math.inf

                if i == 0:
                    dist[(i, j)] = j * EditDistance._edit_costs["insert"]
                    continue
                elif j == 0:
                    dist[(i, j)] = i * EditDistance._edit_costs["delete"]
                    continue
                elif frg_a.tokens[i - 1] != frg_b.tokens[j - 1]:
                    val_sub += EditDistance._edit_costs["substitute"]

                dist[(i, j)] = min(val_sub,
                                   val_del + EditDistance._edit_costs["delete"],
                                   val_ins + EditDistance._edit_costs["insert"])

        if swapped:
            EditDistance.define_costs(insert=EditDistance._edit_costs["delete"],
                                      delete=EditDistance._edit_costs["insert"])

        return dist[(m, n)]
