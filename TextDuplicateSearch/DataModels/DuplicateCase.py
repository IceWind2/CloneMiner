from typing import List

from TextDuplicateSearch.DataModels.TextFragment import TextFragment


class DuplicateCase:
    def __init__(self) -> None:
        self.count: int = 0
        self.text_fragments: List[TextFragment] = []

    def add_text_fragment(self, fragment: TextFragment) -> None:
        self.text_fragments.append(fragment)
        self.count += 1
        self.text_fragments.sort(key=lambda frg: frg.start.idx)

    def length(self) -> int:
        return min([fragment.length for fragment in self.text_fragments]) if len(self.text_fragments) > 0 else 0

    def reset(self) -> None:
        self.count = 0
        self.text_fragments = []
