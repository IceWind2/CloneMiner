from dataclasses import dataclass, field


@dataclass
class SearchConfig:
    # general
    input_file: str = ""
    output_file: str = "output.txt"
    write_to_file: bool = False
    need_text_processing: bool = True

    # strict search
    min_dup_length: int = 3

    # fuzzy search
    # test: List[int] = field(default_factory=list)
