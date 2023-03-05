import string

from TextDuplicateSearch.DataModels.TextFragment import TextFragment


class Hashing:
    signature_mapping = {ch: 1 << (8 - (ord(ch) - ord('a')) // 3) for ch in string.ascii_lowercase[:24]}

    @staticmethod
    def signature_hash_func(fragment: TextFragment) -> None:
        result: int = 0
        for token in fragment.tokens:
            if token.txt[0] in Hashing.signature_mapping:
                result = result | Hashing.signature_mapping[token.txt[0]]
            else:
                result = result | 1

        fragment.hash = result
