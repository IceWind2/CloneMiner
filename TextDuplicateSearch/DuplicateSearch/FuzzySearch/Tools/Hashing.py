import string

from typing import List, Dict
from TextDuplicateSearch.TextProcessing.Token import Token


class Hashing:
    _signature_mapping: Dict[str, int] = {ch: 1 << (8 - (ord(ch) - ord('a')) // 3) for ch in string.ascii_lowercase[:24]}

    @staticmethod
    def signature_hash_func(tokens: List[Token]) -> int:
        result: int = 0
        for token in tokens:
            if token.txt[0] in Hashing._signature_mapping:
                result = result | Hashing._signature_mapping[token.txt[0]]
            else:
                result = result | 1

        return result
