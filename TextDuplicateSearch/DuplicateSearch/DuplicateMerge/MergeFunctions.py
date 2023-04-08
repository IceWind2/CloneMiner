from typing import Union
from bisect import bisect_left

from TextDuplicateSearch.DataModels.DuplicateCase import DuplicateCase
from TextDuplicateSearch.DataModels.DuplicateCollection import DuplicateCollection
from TextDuplicateSearch.DuplicateSearch.DuplicateMerge.SignificanceFunctions import size_length_significance

check_significance = size_length_significance


def merge_duplicate_groups(dup_collection: DuplicateCollection) -> None:
    dup_collection.filter_irrelevant()

    for i in range(len(dup_collection.cases)):
        for j in range(i + 1, len(dup_collection.cases)):
            if _merge_cases(dup_collection.cases[i], dup_collection.cases[j]):
                dup_collection.cases[i].reset()
                break

            _balance_cases(dup_collection.cases[i], dup_collection.cases[j])

    dup_collection.filter_irrelevant()


def _merge_cases(case_a: DuplicateCase, case_b: DuplicateCase) -> bool:
    if case_a.count != case_b.count:
        return False

    if not all(
            case_a.text_fragments[i].is_neighbor(case_b.text_fragments[i]) for i in range(case_b.count)):
        return False

    for i in range(case_b.count):
        case_b.text_fragments[i].merge_with(case_a.text_fragments[i])

    return True


def _balance_cases(case_a: DuplicateCase, case_b: DuplicateCase) -> None:
    if case_a.count < case_b.count:
        case_b, case_a = case_a, case_b

    if case_b.text_fragments[-1].is_before(case_a.text_fragments[0]) or \
            case_b.text_fragments[0].is_after(case_a.text_fragments[-1]):
        return

    right_merge: Union[None, bool] = None
    candidates = []

    for i in range(case_b.count):
        idx: int = bisect_left(case_a.text_fragments, case_b.text_fragments[i]) - 1

        if idx >= 0 and case_b.text_fragments[i].is_neighbor(case_a.text_fragments[idx]):
            if right_merge is None:
                right_merge = True
                candidates.append(idx)
                continue

            if not right_merge:
                right_merge = None
                break

            candidates.append(idx)
            continue

        idx += 1

        if idx < case_a.count and case_b.text_fragments[i].is_neighbor(case_a.text_fragments[idx]):
            if right_merge is None:
                right_merge = False
                candidates.append(idx)
                continue

            if right_merge:
                right_merge = None
                break

            candidates.append(idx)
            continue

        right_merge = None
        break

    if right_merge is None:
        return

    if check_significance(case_a, case_b, candidates):
        for i in range(len(candidates)):
            case_b.text_fragments[i].merge_with(case_a.text_fragments[candidates[i]])

        for frag in [frag for idx, frag in enumerate(case_a.text_fragments) if idx in candidates]:
            case_a.remove_fragment(frag)
