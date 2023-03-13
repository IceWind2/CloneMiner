from typing import Callable, List, Tuple

from TextDuplicateSearch.DataModels.TextFragment import TextFragment
from TextDuplicateSearch.TextProcessing.Token import Token


class FragmentSearch:
    def __init__(self,
                 hashin_func: Callable[[List[Token]], int],
                 editdistance_func: Callable[[TextFragment, TextFragment, float], float]) -> None:

        self.hashin_func: Callable[[List[Token]], int] = hashin_func
        self.editdistance_func: Callable[[TextFragment, TextFragment, float], float] = editdistance_func
