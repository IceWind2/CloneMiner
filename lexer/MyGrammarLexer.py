# Generated from MyGrammar.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\6")
        buf.write(")\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2")
        buf.write("\6\2\20\n\2\r\2\16\2\21\3\3\3\3\3\4\6\4\27\n\4\r\4\16")
        buf.write("\4\30\3\5\6\5\34\n\5\r\5\16\5\35\3\5\3\5\3\6\3\6\6\6$")
        buf.write("\n\6\r\6\16\6%\3\6\3\6\2\2\7\3\3\5\2\7\4\t\5\13\6\3\2")
        buf.write("\7\4\2C\\c|\6\2##.\60<=AA\3\2\62;\4\2\13\f\"\"\7\2$$)")
        buf.write(")aa}}\177\177\2-\2\3\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2")
        buf.write("\13\3\2\2\2\3\17\3\2\2\2\5\23\3\2\2\2\7\26\3\2\2\2\t\33")
        buf.write("\3\2\2\2\13#\3\2\2\2\r\20\t\2\2\2\16\20\5\7\4\2\17\r\3")
        buf.write("\2\2\2\17\16\3\2\2\2\20\21\3\2\2\2\21\17\3\2\2\2\21\22")
        buf.write("\3\2\2\2\22\4\3\2\2\2\23\24\t\3\2\2\24\6\3\2\2\2\25\27")
        buf.write("\t\4\2\2\26\25\3\2\2\2\27\30\3\2\2\2\30\26\3\2\2\2\30")
        buf.write("\31\3\2\2\2\31\b\3\2\2\2\32\34\t\5\2\2\33\32\3\2\2\2\34")
        buf.write("\35\3\2\2\2\35\33\3\2\2\2\35\36\3\2\2\2\36\37\3\2\2\2")
        buf.write("\37 \b\5\2\2 \n\3\2\2\2!$\t\6\2\2\"$\5\5\3\2#!\3\2\2\2")
        buf.write("#\"\3\2\2\2$%\3\2\2\2%#\3\2\2\2%&\3\2\2\2&\'\3\2\2\2\'")
        buf.write("(\b\6\2\2(\f\3\2\2\2\t\2\17\21\30\35#%\3\b\2\2")
        return buf.getvalue()


class MyGrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    WORD = 1
    NUM = 2
    WS = 3
    SKP = 4

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "WORD", "NUM", "WS", "SKP" ]

    ruleNames = [ "WORD", "PUNCT", "NUM", "WS", "SKP" ]

    grammarFileName = "MyGrammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


