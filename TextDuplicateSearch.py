import Tokenizer
import RepeatSearch
import os

__classesFile = ''

def find_clones(inFile, minTokens, outFile):
    text = open(inFile, encoding='utf-8')
    tokens = Tokenizer.tokenize(text.read(), __classesFile)
    
    result = RepeatSearch.get_clone_data(tokens, minTokens)
    with open(outFile, 'w') as out:
        out.write(str(result))

def enable_token_classes(classesFile = os.path.join('lexer', 'TokenClasses.txt')):
    global __classesFile
    
    __classesFile = classesFile
    
def disable_token_classes():
    global __classesFile
    
    __classesFile = ''

if __name__=='__main__':
    fin = "text.txt"
    fout = "res.txt"
    enable_token_classes()
    find_clones(fin, 3, fout)