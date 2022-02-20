from typing import List
from Tokenizer import Token


class Duplicate:
    def __init__(self, start: Token, end: Token, length: int) -> None:
        self.start: Token = start
        self.end: Token = end
        self.length: int = length


class DuplicateCase:
    def __init__(self) -> None:
        self.length: int = -1
        self.number: int = 0
        self.duplicates: List[Duplicate] = []

    def add_duplicate(self, dup: Duplicate) -> None:
        self.duplicates.append(dup)
        self.number += 1
        if self.length == -1:
            self.length = dup.length
        else:
            self.length = min(self.length, dup.length)
    
    
class DuplicateData:
    def __init__(self, tokenArray: List[Token]) -> None:
        self.cases: List[DuplicateCase] = []
        self.tokens: List[Token] = tokenArray
        
    def add_case(self, duplicateCase: DuplicateCase) -> None:
        self.cases.append(duplicateCase)
                 
    def __repr__(self) -> str:
        repres: str = ''

        for ID, case in enumerate(self.cases):
            caseStr = f'{ID};{case.length};{case.number}\n'
            for duplicate in case.duplicates:
                caseStr += f'0:{duplicate.start.raw.line}.{duplicate.start.raw.column + 1}-{duplicate.end.raw.line}.{duplicate.end.raw.column + 1}\n'
            
            caseStr += '\n'
            repres += caseStr
                
        return repres
