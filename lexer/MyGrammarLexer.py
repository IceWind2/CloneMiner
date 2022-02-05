# Generated from D:\dev\projects\TextDuplicateSearch\lexer\MyGrammar.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\7")
        buf.write("\62\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write("\7\3\2\3\2\6\2\22\n\2\r\2\16\2\23\3\3\3\3\3\4\6\4\31\n")
        buf.write("\4\r\4\16\4\32\3\5\6\5\36\n\5\r\5\16\5\37\3\5\3\5\3\6")
        buf.write("\3\6\6\6&\n\6\r\6\16\6\'\3\6\3\6\3\7\6\7-\n\7\r\7\16\7")
        buf.write(".\3\7\3\7\3.\2\b\3\3\5\2\7\4\t\5\13\6\r\7\3\2\7\4\2C\\")
        buf.write("c|\6\2##.\60<=AA\3\2\62;\4\2\13\f\"\"\7\2$$))aa}}\177")
        buf.write("\177\2\67\2\3\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\3\21\3\2\2\2\5\25\3\2\2\2\7\30\3\2\2")
        buf.write("\2\t\35\3\2\2\2\13%\3\2\2\2\r,\3\2\2\2\17\22\t\2\2\2\20")
        buf.write("\22\5\7\4\2\21\17\3\2\2\2\21\20\3\2\2\2\22\23\3\2\2\2")
        buf.write("\23\21\3\2\2\2\23\24\3\2\2\2\24\4\3\2\2\2\25\26\t\3\2")
        buf.write("\2\26\6\3\2\2\2\27\31\t\4\2\2\30\27\3\2\2\2\31\32\3\2")
        buf.write("\2\2\32\30\3\2\2\2\32\33\3\2\2\2\33\b\3\2\2\2\34\36\t")
        buf.write("\5\2\2\35\34\3\2\2\2\36\37\3\2\2\2\37\35\3\2\2\2\37 \3")
        buf.write("\2\2\2 !\3\2\2\2!\"\b\5\2\2\"\n\3\2\2\2#&\t\6\2\2$&\5")
        buf.write("\5\3\2%#\3\2\2\2%$\3\2\2\2&\'\3\2\2\2\'%\3\2\2\2\'(\3")
        buf.write("\2\2\2()\3\2\2\2)*\b\6\2\2*\f\3\2\2\2+-\13\2\2\2,+\3\2")
        buf.write("\2\2-.\3\2\2\2./\3\2\2\2.,\3\2\2\2/\60\3\2\2\2\60\61\b")
        buf.write("\7\2\2\61\16\3\2\2\2\n\2\21\23\32\37%\'.\3\b\2\2")
        return buf.getvalue()


class MyGrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    WORD = 1
    NUM = 2
    WS = 3
    SKP = 4
    ALL = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "WORD", "NUM", "WS", "SKP", "ALL" ]

    ruleNames = [ "WORD", "PUNCT", "NUM", "WS", "SKP", "ALL" ]

    grammarFileName = "MyGrammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


