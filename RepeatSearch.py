from abc import abstractproperty
from CloneData import CloneData
import SuffixArray

__suffArr = None
__LCPArr = None
__marked = None
MIN_CLONE_SIZE = 3

def get_clone_data(tokens) -> CloneData:
    global __suffArr
    global __marked
    global __LCPArr
    
    __suffArr, __LCPArr = SuffixArray.build_suffix_array(tokens)
    __marked = [False] * len(tokens)
    
    repeats = __basic_repeats()
    clones = __simple_clones()
    
    result = CloneData(tokens)
    for repeat in repeats:
        result.add_repeat_case(repeat)
    for clone in clones:
        result.add_clone_case(clone)
        
    return result
    
    
def __basic_repeats() -> list:
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
    
    return repeats  # token array ranges, format [ [], [] ]
    

def __simple_clones() -> list:
    global __suffArr
    global __marked
    
    curIdx = 1
    clones = []
    repeatRange = [-1, -1]
    while (curIdx < len(__marked)):
        if (__marked[curIdx]):
            curIdx += 1
            continue
        
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
                clones.append(tmp)
                
                repeatRange = [-1, -1]
                
        curIdx += 1
        
    return clones  # token array ranges, format [ [[],[]], [[],[]] ]