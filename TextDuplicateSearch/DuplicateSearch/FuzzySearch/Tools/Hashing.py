import string
from typing import List, Dict

from TextDuplicateSearch.TextProcessing.Token import Token


class Hashing:
    _signature_mapping: Dict[str, int] = {ch: 1 << (8 - (ord(ch) - ord('a')) // 3) for ch in string.ascii_lowercase[:24]}

    @staticmethod
    def signature_hash_func(tokens: List[Token]) -> int:
        result: int = 0
        for token in tokens:
            if token.processed[0] in Hashing._signature_mapping:
                result = result | Hashing._signature_mapping[token.processed[0]]
            else:
                result = result | 1

        return result

    @staticmethod
    def get_diff(hash_a: int, hash_b: int) -> int:
        diff: int = hash_a ^ hash_b
        bit: int = 1
        result: int = 0

        while bit < diff:
            if bit & diff != 0:
                result += 1

            bit <<= 1

        return result
