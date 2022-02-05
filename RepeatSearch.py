from abc import abstractproperty
from DuplicateData import *
import SuffixArray

__suffArr = None
__LCPArr = None
__marked = None
MIN_CLONE_SIZE = None

def get_clone_data(tokens, minTokens) -> DuplicateData:
    global __suffArr
    global __marked
    global __LCPArr
    global MIN_CLONE_SIZE
    
    MIN_CLONE_SIZE = minTokens
    
    __suffArr, __LCPArr = SuffixArray.build_suffix_array(tokens)
    __marked = [False] * len(tokens)
    
    clones = __simple_clones(tokens)
    
    result = DuplicateData(tokens)
    for clone in clones:
        case = DuplicateCase()
        for repeat in clone:
            case.add_duplicate(Duplicate(tokens[repeat[0]], tokens[repeat[1]], repeat[1] - repeat[0] + 1))
        
        result.add_case(case)
        
    return result
    
    
def __basic_repeats() -> list:  # token array ranges, format [ [], [] ]
    global __suffArr
    global __marked
    global __LCPArr
    
    prev = 0
    repeatRange = [-1, -1]
    repeats = []
    
    for idx in range(1, len(__suffArr)):
        if (__suffArr[idx] - __suffArr[idx - 1] == prev and __LCPArr[idx] > 0):
            if (repeatRange[0] == -1):
                repeatRange[0] = idx-2
                repeatRange[1] = idx
            else:
                repeatRange[1] += 1
        else:
            if (repeatRange[0] != -1):
                repeats.append([__suffArr[repeatRange[0]], __suffArr[repeatRange[1]]])
                repeatRange = [-1, -1]
        prev = __suffArr[idx] - __suffArr[idx - 1]
                
    for repeatRange in repeats:
        for idx in range(repeatRange[0], repeatRange[1] + 1):
            __marked[idx] = True
    
    return repeats
    

def __simple_clones(tokens) -> list:  # token array ranges, format [ [[],[]], [[],[]] ]
    global __suffArr
    global __marked
    
    curIdx = 1
    duplicates = []
    repeatRange = [-1, -1]
    isNested = True
    while (curIdx < len(__marked)):  # going through suffix array
        if (__LCPArr[curIdx] >= MIN_CLONE_SIZE):
            if (not __marked[__suffArr[curIdx]]):
                isNested = False
            if (repeatRange[0] == -1):
                repeatRange[0] = curIdx-1
                repeatRange[1] = curIdx
            else:
                repeatRange[1] += 1
        else:
            if (repeatRange[0] != -1 and not isNested):
                isNested = True
                
                tmp = []
                length = min(__LCPArr[repeatRange[0] + 1 : repeatRange[1] + 1])  # forward from starting tokens
                
                expand = True
                shift = 1
                while (expand):  # trying to go backwards from starting tokens
                    curToken = tokens[__suffArr[repeatRange[0]] - shift]
                    for idx in range(repeatRange[0] + 1, repeatRange[1] + 1):
                        if (tokens[__suffArr[idx] - shift] != curToken):
                            expand = False
                            
                    if (expand):
                        for idx in range(repeatRange[0] + 1, repeatRange[1] + 1):
                            __marked[__suffArr[idx] - shift] = True;
                        shift += 1
                        
                shift -= 1
                    
                for idx in range(repeatRange[0], repeatRange[1] + 1):
                    tmp.append([__suffArr[idx] - shift, __suffArr[idx] + length - 1])
                    __marked[__suffArr[idx] - shift:__suffArr[idx] + length] = [True] * (shift + length)
                duplicates.append(tmp)
                
            repeatRange = [-1, -1]
                
        curIdx += 1
        
    return duplicates
