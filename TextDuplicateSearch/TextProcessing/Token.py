from typing import Tuple, Any


class Token:
    def __init__(self, token: str, position: Tuple[int, int], idx: int) -> None:
        self.text: str = token
        self.line: int = position[0]
        self.col: int = position[1]
        self.idx: int = idx

        self.processed: str = ""
        self.id: int = -1

    def __str__(self) -> str:
        return self.text

    def __repr__(self) -> str:
        return f'{self.text}:{self.id}'

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Token):
            return self.id == other.id
        return False
