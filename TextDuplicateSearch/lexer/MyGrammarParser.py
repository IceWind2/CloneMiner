# Generated from D:\dev\projects\TextDuplicateSearch\lexer\MyGrammar.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\7")
        buf.write("\f\4\2\t\2\3\2\6\2\6\n\2\r\2\16\2\7\3\2\3\2\3\2\2\2\3")
        buf.write("\2\2\2\2\13\2\5\3\2\2\2\4\6\7\3\2\2\5\4\3\2\2\2\6\7\3")
        buf.write("\2\2\2\7\5\3\2\2\2\7\b\3\2\2\2\b\t\3\2\2\2\t\n\7\2\2\3")
        buf.write("\n\3\3\2\2\2\3\7")
        return buf.getvalue()


class MyGrammarParser ( Parser ):

    grammarFileName = "MyGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "WORD", "NUM", "WS", "SKP", "ALL" ]

    RULE_text = 0

    ruleNames =  [ "text" ]

    EOF = Token.EOF
    WORD=1
    NUM=2
    WS=3
    SKP=4
    ALL=5

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class TextContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MyGrammarParser.EOF, 0)

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(MyGrammarParser.WORD)
            else:
                return self.getToken(MyGrammarParser.WORD, i)

        def getRuleIndex(self):
            return MyGrammarParser.RULE_text

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterText" ):
                listener.enterText(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitText" ):
                listener.exitText(self)




    def text(self):

        localctx = MyGrammarParser.TextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_text)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 3 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 2
                self.match(MyGrammarParser.WORD)
                self.state = 5 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MyGrammarParser.WORD):
                    break

            self.state = 7
            self.match(MyGrammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





