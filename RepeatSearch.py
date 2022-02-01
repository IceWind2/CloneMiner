from abc import abstractproperty
from DuplicateData import *
import SuffixArray

__suffArr = None
__LCPArr = None
__marked = None
MIN_CLONE_SIZE = 4

def get_clone_data(tokens) -> DuplicateData:
    global __suffArr
    global __marked
    global __LCPArr
    
    __suffArr, __LCPArr = SuffixArray.build_suffix_array(tokens)
    __marked = [False] * len(tokens)
    
    clones = __simple_clones()
    
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
    

def __simple_clones() -> list:  # token array ranges, format [ [[],[]], [[],[]] ]
    global __suffArr
    global __marked
    
    curIdx = 1
    duplicates = []
    repeatRange = [-1, -1]
    while (curIdx < len(__marked)):
        if (__LCPArr[curIdx] >= MIN_CLONE_SIZE):
            if repeatRange[0] == -1:
                repeatRange[0] = curIdx-1
                repeatRange[1] = curIdx
            else:
                repeatRange[1] += 1
        else:
            if (repeatRange[0] != -1):
                tmp = []
                length = min(__LCPArr[repeatRange[0] + 1 : repeatRange[1] + 1])
                
                for idx in range (repeatRange[0], repeatRange[1] + 1):
                    tmp.append([__suffArr[idx], __suffArr[idx] + length - 1])
                duplicates.append(tmp)
                
                repeatRange = [-1, -1]
                
        curIdx += 1
        
    return duplicates
