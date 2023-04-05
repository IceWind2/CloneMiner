from typing import Union

from TextDuplicateSearch.DataModels.DuplicateCase import DuplicateCase
from TextDuplicateSearch.DataModels.DuplicateCollection import DuplicateCollection
from TextDuplicateSearch.DuplicateSearch.DuplicateMerge.SignificanceFunctions import size_length_significance


check_significance = size_length_significance


def merge_duplicate_groups(dup_collection: DuplicateCollection) -> None:
    for i in range(len(dup_collection.cases)):
        for j in range(i + 1, len(dup_collection.cases)):
            if _merge_cases(dup_collection.cases[i], dup_collection.cases[j]):
                dup_collection.cases[i].reset()
                break

            # _balance_cases(dup_collection.cases[i], dup_collection.cases[j])

    dup_collection.filter_irrelevant()


def _merge_cases(case_a: DuplicateCase, case_b: DuplicateCase) -> bool:
    if len(case_a.text_fragments) != len(case_b.text_fragments):
        return False

    if not all(
            case_a.text_fragments[i].is_neighbor(case_b.text_fragments[i]) for i in range(len(case_b.text_fragments))):
        return False

    for i in range(len(case_b.text_fragments)):
        case_b.text_fragments[i].merge_with(case_a.text_fragments[i])

    return True


def _balance_cases(case_a: DuplicateCase, case_b: DuplicateCase) -> None:
    if len(case_a.text_fragments) < len(case_b.text_fragments):
        case_b, case_a = case_a, case_b

    from_right: Union[None, bool] = None
    a_idx: int = 0
    b_idx: int = 0
    candidates = []

    while a_idx < len(case_a.text_fragments) and b_idx < len(case_b.text_fragments):
        if case_b.text_fragments[b_idx].is_neighbor(case_a.text_fragments[a_idx]):
            if from_right is None:
                from_right = case_a.text_fragments[a_idx].is_before(case_b.text_fragments[b_idx])
                continue

            if from_right and case_a.text_fragments[a_idx].is_after(case_b.text_fragments[b_idx]):
                from_right = None
                break

            candidates.append(a_idx)
            b_idx += 1

        a_idx += 1

    if from_right is None:
        return

    if check_significance(case_a, case_b, candidates):
        for i in range(len(candidates)):
            case_b.text_fragments[i].merge_with(case_a.text_fragments[candidates[i]])

        for frag in [frag for idx, frag in enumerate(case_a.text_fragments) if idx in candidates]:
            case_a.remove_fragment(frag)
