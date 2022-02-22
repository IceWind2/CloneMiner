from TextDuplicateSearch.DuplicateData import *
from TextDuplicateSearch import SuffixArray

__suffArr: List[int] = []
__LCPArr: List[int] = []
__marked: List[bool] = []
MIN_CLONE_SIZE: int = 0


def get_clone_data(tokens: List[Token], minTokens: int) -> DuplicateData:
    global __suffArr
    global __marked
    global __LCPArr
    global MIN_CLONE_SIZE
    
    MIN_CLONE_SIZE = minTokens
    
    __suffArr, __LCPArr = SuffixArray.build_suffix_array(tokens)
    __marked = [False] * len(tokens)
    
    clones: List[List[List[int]]] = __simple_clones(tokens)
    
    result: DuplicateData = DuplicateData(tokens)
    for clone in clones:
        case: DuplicateCase = DuplicateCase()
        for repeat in clone:
            case.add_duplicate(Duplicate(tokens[repeat[0]], tokens[repeat[1]], repeat[1] - repeat[0] + 1))
        
        result.add_case(case)
        
    return result
    

def __simple_clones(tokens: List[Token]) -> List[List[List[int]]]:
    global __suffArr
    global __marked
    
    curIdx: int = 1
    duplicates: List[List[List[int]]] = []
    repeatRange: List[int] = [-1, -1]
    isNested: bool = True
    while curIdx < len(__marked):  # going through suffix array
        if __LCPArr[curIdx] >= MIN_CLONE_SIZE:
            if not __marked[__suffArr[curIdx]]:
                isNested = False
            if repeatRange[0] == -1:
                repeatRange[0] = curIdx-1
                repeatRange[1] = curIdx
            else:
                repeatRange[1] += 1
        else:
            if repeatRange[0] != -1 and not isNested:
                isNested = True
                
                tmp: List[List[int]] = []
                length: int = min(__LCPArr[repeatRange[0] + 1 : repeatRange[1] + 1])  # forward from starting tokens
                
                expand: bool = True
                shift: int = 1
                while expand:  # trying to go backwards from starting tokens
                    curToken: Token = tokens[__suffArr[repeatRange[0]] - shift]
                    for idx in range(repeatRange[0] + 1, repeatRange[1] + 1):
                        if tokens[__suffArr[idx] - shift] != curToken:
                            expand = False
                            
                    if expand:
                        for idx in range(repeatRange[0] + 1, repeatRange[1] + 1):
                            __marked[__suffArr[idx] - shift] = True
                        shift += 1
                        
                shift -= 1
                    
                for idx in range(repeatRange[0], repeatRange[1] + 1):
                    tmp.append([__suffArr[idx] - shift, __suffArr[idx] + length - 1])
                    __marked[__suffArr[idx] - shift:__suffArr[idx] + length] = [True] * (shift + length)
                duplicates.append(tmp)
                
            repeatRange = [-1, -1]
                
        curIdx += 1
        
    return duplicates
