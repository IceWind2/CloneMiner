from typing import List

from TextDuplicateSearch.DataModels.TextFragment import TextFragment


class DuplicateCase:
    def __init__(self) -> None:
        self.length: int = -1
        self.count: int = 0
        self.text_fragments: List[TextFragment] = []

    def add_text_fragment(self, fragment: TextFragment) -> None:
        self.text_fragments.append(fragment)
        self.count += 1
        if self.length == -1:
            self.length = fragment.length
        else:
            self.length = min(self.length, fragment.length)

        self.text_fragments.sort(key=lambda frg: frg.start.idx)
