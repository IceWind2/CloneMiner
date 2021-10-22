from CloneData import CloneData
import Tokenizer
import RepeatSearch
import SuffixArray

def find_clones(text):
    tokens = Tokenizer.tokenize(text)
    #suffArr, LCPArr = SuffixArray.build_suffix_array(tokens)
    result = RepeatSearch.get_clone_data(tokens)
    print(result)
    

if __name__=='__main__':
    f = open("text.txt", encoding='utf-8')
    find_clones(f.read())