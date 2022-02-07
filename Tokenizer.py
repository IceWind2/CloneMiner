from antlr4 import *
from lexer.MyGrammarLexer import MyGrammarLexer
import re

class Token:
    def __init__(self, token, id):
        self.raw = token
        self.txt = token.text
        self.id = id
    
    def __str__(self) -> str:
        return self.txt
    
    def __repr__(self) -> str:
        return f'{self.txt}:{self.id}'
    
    def __eq__(self, other):
        if isinstance(other, Token):
            return self.id == other.id
        return False
    
def tokenize(input, classesFile) -> list:
    dict = {}
    nextId = 0
    
    if classesFile != '':
        try:
            with open(classesFile, 'r') as tc:
                classes = re.sub('\n+', '', tc.read()).split(';')[:-1]
            
            for cls in classes:
                line = re.sub("[\s\t]+", ' ', cls)
                for word in line.split():
                    dict[word.lower()] = nextId
                
                nextId += 1
        except Exception:
            print("Token classes file not found.")
    
    data =  InputStream(input)
    lexer = MyGrammarLexer(data)
    tokens = lexer.getAllTokens()
    result = []
    
    for token in tokens:
        if (token.text.lower() in dict):
            result.append(Token(token, dict[token.text.lower()]))
        else:
            result.append(Token(token, nextId))
            dict[token.text.lower()] = nextId
            nextId += 1
    
    return result