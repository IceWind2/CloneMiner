from TextDuplicateSearch.DataModels.DuplicateCase import DuplicateCase
from TextDuplicateSearch.DataModels.DuplicateCollection import DuplicateCollection


def merge_duplicate_groups(dup_collection: DuplicateCollection) -> None:
    for i in range(len(dup_collection.cases)):
        for j in range(i + 1, len(dup_collection.cases)):
            if _merge_cases(dup_collection.cases[i], dup_collection.cases[j]):
                dup_collection.cases[i].reset()
                break

    dup_collection.cases = list(filter(lambda case: case.length() != 0, dup_collection.cases))


def _merge_cases(case_a: DuplicateCase, case_b: DuplicateCase) -> bool:
    if len(case_a.text_fragments) != len(case_b.text_fragments):
        return False

    if not all(case_a.text_fragments[i].is_neighbor(case_b.text_fragments[i]) for i in range(len(case_b.text_fragments))):
        return False

    for i in range(len(case_b.text_fragments)):
        case_b.text_fragments[i].merge_with(case_a.text_fragments[i])

    return True
