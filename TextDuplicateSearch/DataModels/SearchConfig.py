from dataclasses import dataclass, field


@dataclass
class SearchConfig:
    # general
    input_file: str = ""
    file_encoding: str = "utf-8"
    classes_file: str = ""
    output_file: str = "output.txt"
    write_to_file: bool = False
    need_text_processing: bool = True

    # strict search
    min_dup_length: int = 3

    # fragment search
    fragment_size: int = 10
    max_hashing_diff: int = 3
    max_edit_distance: int = 3
    precise_grouping: bool = False
