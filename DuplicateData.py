class Duplicate:
    def __init__(self, start, end, length):
        self.start = start
        self.end = end
        self.length = length


class DuplicateCase:
    def __init__(self):
        self.length = -1
        self.number = 0
        self.duplicates = []

    def add_duplicate(self, dup: Duplicate):
        self.duplicates.append(dup)
        self.number += 1
        if (self.length == -1):
            self.length = dup.length
        else:
            self.length = min(self.length, dup.length)
    
    
class DuplicateData:
    def __init__(self, tokenArray) -> None:
        self.cases = []
        self.tokens = tokenArray
        
    def add_case(self, duplicateCase: DuplicateCase):
        self.cases.append(duplicateCase)
                 
    def __repr__(self):
        repr = ''
        
        caseStr = ''
        for id, case in enumerate(self.cases):
            caseStr = f'{id};{case.length};{case.number}\n'
            for duplicate in case.duplicates:
                caseStr += f'0:{duplicate.start.raw.line}.{duplicate.start.raw.column + 1}-{duplicate.end.raw.line}.{duplicate.end.raw.column + 1}\n'
            
            caseStr += '\n'
            repr += caseStr
                
        return repr