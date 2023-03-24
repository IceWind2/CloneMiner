from typing import List

from TextDuplicateSearch.DataModels.DuplicateCase import DuplicateCase


class DuplicateCollection:
    def __init__(self) -> None:
        self.cases: List[DuplicateCase] = []
        # self.tokens: List[Token] = token_array
        
    def add_case(self, duplicate_case: DuplicateCase) -> None:
        self.cases.append(duplicate_case)
                 
    def __repr__(self) -> str:
        result: str = ''

        for ID, case in enumerate(self.cases):
            case_string = f'{ID};{case.length};{case.count}\n'
            for duplicate in case.text_fragments:
                case_string += f'0:{duplicate.start.line}.{duplicate.start.col}-{duplicate.end.line}.{duplicate.end.col}\n'
            
            case_string += '\n'
            result += case_string
                
        return result

    def pretty_print(self) -> None:
        for i in range(len(self.cases)):
            print(f"Case #{i + 1}:")
            for j in range(len(self.cases[i].text_fragments)):
                print(self.cases[i].text_fragments[j])
                if j != len(self.cases[i].text_fragments) - 1:
                    print('|||')

            print('-------------------------------')
