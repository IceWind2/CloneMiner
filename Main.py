from encodings import utf_8
from DuplicateData import DuplicateData
import Tokenizer
import RepeatSearch
import SuffixArray

def find_clones(inPath, minTokens, outPath):
    text = open(inPath, encoding='utf-8')
    tokens = Tokenizer.tokenize(text.read())
    
    result = RepeatSearch.get_clone_data(tokens, minTokens)
    with open(outPath, 'w') as out:
        out.write(str(result))
    

if __name__=='__main__':
    fin = "text.txt"
    fout = "res.txt"
    find_clones(fin, 3, fout)