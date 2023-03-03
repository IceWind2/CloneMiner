from typing import Tuple, Any


class Token:
    def __init__(self, token: str, ID: int, position: Tuple[int, int], idx: int) -> None:
        self.txt: str = token
        self.ID: int = ID
        self.line: int = position[0]
        self.col: int = position[1]
        self.idx: int = idx

    def __str__(self) -> str:
        return self.txt

    def __repr__(self) -> str:
        return f'{self.txt}:{self.ID}'

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Token):
            return self.ID == other.ID
        return False
