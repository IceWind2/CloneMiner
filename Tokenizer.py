from antlr4 import *
from lexer.MyGrammarLexer import MyGrammarLexer

dict = {}
nextId = 0

class Token:
    def __init__(self, token, id):
        self.raw = token
        self.txt = token.text
        self.id = id
    
    def __str__(self) -> str:
        return self.txt
    
    def __repr__(self) -> str:
        return f'{self.txt}:{self.id}'
    
def tokenize(input) -> list:
    global nextId
    global dict
    
    data =  InputStream(input)
    lexer = MyGrammarLexer(data)
    tokens = lexer.getAllTokens()
    result = []
    
    for token in tokens:
        if (token.text in dict):
            result.append(Token(token, dict[token.text]))
        else :
            result.append(Token(token, nextId))
            dict[token.text] = nextId
            nextId += 1
    
    return result