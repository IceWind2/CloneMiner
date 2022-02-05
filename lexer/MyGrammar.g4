grammar MyGrammar;
text: (WORD)+ EOF;

WORD: ([A-Z] | [a-z] | NUM)+ ;
fragment PUNCT: (',' | '-' | '.' | '?' | '!' | ':' | ';') ;
NUM: [0-9]+ ;
WS: [ \t\n]+ -> skip ;
SKP: ('{' | '}' | '_' | '\'' | '"' | PUNCT)+ -> skip ;
ALL: .+? -> skip ;