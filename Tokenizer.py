from antlr4 import *
from lexer.MyGrammarLexer import MyGrammarLexer
from nltk.stem import PorterStemmer
import re

token_id = {}
__nextId = 0
__stemmer = PorterStemmer()

class Token:
    def __init__(self, token, id, position):
        self.raw = token
        self.txt = token.text
        self.id = id
        self.pos = position
    
    def __str__(self) -> str:
        return self.txt
    
    def __repr__(self) -> str:
        return f'{self.txt}:{self.id}'
    
    def __eq__(self, other):
        if isinstance(other, Token):
            return self.id == other.id
        return False
    
def process_token(text):
    global __nextId
    
    t_word = __stemmer.stem(text.lower())
        
    if t_word not in token_id:
        token_id[t_word] = __nextId
        __nextId += 1
        
    return token_id[t_word]    
    
def tokenize(input, classesFile) -> list:
    if classesFile != '':
        try:
            with open(classesFile, 'r') as tc:
                classes = re.sub('\n+', '', tc.read()).split(';')[:-1]
            
            for cls in classes:
                line = re.sub("[\s\t]+", ' ', cls)
                for word in line.split():
                    process_token(word)
                
        except Exception:
            print("Token classes file not found.")
    
    data =  InputStream(input)
    lexer = MyGrammarLexer(data)
    tokens = lexer.getAllTokens()
    result = []
    
    for pos, token in enumerate(tokens):
        id = process_token(token.text)
        result.append(Token(token, id, pos))

    return result