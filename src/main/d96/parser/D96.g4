// 1952406
grammar D96;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: classdecl+ EOF;

// Begin to define lexer
// Fragments
fragment LETTER: [A-Za-z];
fragment DIGIT: [0-9];
fragment DOLLAR: '$';
fragment EXPONENT: 'E' | 'e';
fragment DOUBLE_QUOTE: '"';

// Characters set
fragment BLANK: ' ';
fragment TAB: '\\t';
fragment BACKSPACE: '\\b';
fragment FORM_FEED: '\\f';
fragment CARRIAGE_RETURN: '\\r';
fragment NEWLINE: '\\n';
fragment WHITE_CHAR: (BLANK | TAB | BACKSPACE | FORM_FEED | CARRIAGE_RETURN | NEWLINE);
fragment SINGLE_QUOTE: '\\\'';
fragment BACKSLASH: '\\\\';

// Program comment
COMMENT: '##' .*? '##' -> skip;

// Literals
// Note: màu tím - 1 word, màu vàng - 1 sentence. Moreover, fragment bị bỏ qua
fragment DECIMAL: [1-9](DIGIT | '_' DIGIT)*;
fragment DEC_NO_: '0' | [1-9] DIGIT*;
fragment OCTAL: '0'([1-7]([0-7] | '_'[0-7])*);
fragment HEXA: ('0x' | '0X') ([A-F1-9]([A-F0-9] | '_'[A-F0-9])*);
fragment BINARY: ('0b' | '0B') ('1'([01] | '_'[01])*);
INTLIT: (DECIMAL | OCTAL | HEXA | BINARY){self.text = self.text.replace('_','')};
ZERO: '0' | '00' | '0x0' | '0X0' | '0b0' | '0B0';

FLOATLIT: ((DECIMAL | '0') DOT DIGIT* | (DECIMAL | '0') EXPONENT (ADD | MINUS)? DIGIT+ | (DECIMAL | '0') DOT DIGIT* EXPONENT (ADD | MINUS)? DIGIT+ | DOT DIGIT* EXPONENT (ADD | MINUS)? DIGIT+){self.text = self.text.replace('_','')};
// FLOATLIT: ((DECIMAL | '0') DOT DEC_NO_? | (DECIMAL | '0') EXPONENT (ADD | MINUS)? (DEC_NO_ | '0') | (DECIMAL | '0') DOT DEC_NO_? EXPONENT (ADD | MINUS)? (DEC_NO_ | '0') | DOT DEC_NO_? EXPONENT (ADD | MINUS)? (DEC_NO_ | '0')){self.text = self.text.replace('_','')};

BOOLLIT: TRUE | FALSE;

STRINGLIT: DOUBLE_QUOTE VALID_CHARACTER* DOUBLE_QUOTE {self.text = self.text[1:-1]};

arrlit: 'Array' '(' ((expr ',')* expr) ')';

mul_arrlit: 'Array' '(' (((arrlit | mul_arrlit) ',')* (arrlit | mul_arrlit)) ')';

literal: INTLIT | FLOATLIT | BOOLLIT | STRINGLIT | arrlit | mul_arrlit;

// Expressions
exprlist1: expr exprlist2 | ;
exprlist2: COMMA expr exprlist2 | ;

expr: expr0;
expr0: expr1 (CONCAT_STR | COMPARE_STR) expr1 | expr1;
expr1: expr2 (EQUAL | UNEQUAL | LESS  |  GREATER  |  LESS_EQ | GREATER_EQ) expr2 | expr2;
expr2: expr2 (AND | OR) expr3 | expr3;
expr3: expr3 (ADD | MINUS) expr4 | expr4;
expr4: expr4 (MULTIPLY | DIVIDE | MODULUS) expr5 | expr5;
expr5: NOT expr5 | expr6;
expr6: MINUS expr6 | expr7;
expr7: expr7 LSB expr RSB | expr8;
expr8: expr8 DOT ID | ID DOUBLE_COLON STATIC_ID | expr8 DOT ID LP exprlist1 RP | ID DOUBLE_COLON STATIC_ID LP exprlist1 RP | expr9;
expr9: NEW ID LP exprlist1 RP | expr10;
expr10: LP expr0 RP | operand;
operand: INTLIT | ZERO | FLOATLIT | BOOLLIT | STRINGLIT | arrlit | mul_arrlit | ID | SELF | NULL;

// Statements
statement: vardecl | constdecl | assign | ifstmt | forstmt | breakstmt | continuestmt | returnstmt | method_invoc | blockstmt;

// Ensure num of ID = num of value
attr_list_1: ID attr_list_2 expr| idlist1 COLON dtype;
attr_list_2: COMMA ID attr_list_2 expr COMMA | COLON dtype ASSIGN;

// VAR & CONST declaration
vardecl: VAR attr_list_1 SEMI;
constdecl: VAL attr_list_1 SEMI;

idlist1: ID idlist2 | ID;
idlist2: COMMA ID idlist2 | ;

// Assignment Statement
assign: (ID | expr7 LSB expr RSB | expr8 DOT ID | ID DOUBLE_COLON STATIC_ID) ASSIGN expr SEMI;

// If statement
ifstmt: IF LP expr RP blockstmt elifstmt* elsestmt?;
blockstmt: LCB statement* RCB; // Block statement
elifstmt: ELSEIF LP expr RP blockstmt;
elsestmt: ELSE blockstmt;

// For/In statement
forstmt: FOREACH LP ID IN expr '..' expr (BY expr)? RP blockstmt;

// Break statement
breakstmt: BREAK SEMI;

// Continue statement
continuestmt: CONTINUE SEMI;

// Return statement
returnstmt: RETURN expr? SEMI;

// Method call
index_expr: (ID | attr_access | static_attr) index_operator;
index_operator: LSB expr? RSB index_operator | ;

// For normal attr & method
accessor: object_create | ID | SELF | static_attr | static_method | NULL | LP exprlist1 RP | literal;
object_create: NEW ID LP exprlist1 RP;
attr_access: attr_access DOT ID | accessor;
method_access: attr_access DOT ID LP exprlist1 RP (DOT ID (LP exprlist1 RP)?)*;

// For static attr & method
static_attr: ID DOUBLE_COLON STATIC_ID;
static_method: ID DOUBLE_COLON STATIC_ID LP exprlist1 RP;

// Method Invocation statement
method_invoc: (method_access | static_method) SEMI;

// Program structure
// Class declaration
classdecl: CLASS ID (COLON ID)? LCB declaration* RCB;

// Ensure num of ID = num of value
attr_list_1_gen: (ID | STATIC_ID) attr_list_2_gen expr| idlist1_general COLON dtype;
attr_list_2_gen: COMMA (ID | STATIC_ID) attr_list_2_gen expr COMMA | COLON dtype ASSIGN;

vardecl_general: VAR attr_list_1_gen SEMI;
constdecl_general: VAL attr_list_1_gen SEMI;

idlist1_general: (ID | STATIC_ID) idlist2_general | (ID | STATIC_ID);
idlist2_general: COMMA (ID | STATIC_ID) idlist2_general | ;

method_decl: (ID | STATIC_ID) LP paralist1 RP blockstmt;

paralist1: idlist1 COLON dtype paralist2 | ;
paralist2: SEMI idlist1 COLON dtype paralist2 | ;

construct_decl: CONSTRUCTOR LP paralist1 RP blockstmt;
destruct_decl: DESTRUCTOR LP RP blockstmt;

declaration: vardecl_general | constdecl_general | method_decl | construct_decl | destruct_decl;

// Type and Value
// Array type
array_decl: ARRAY LSB dtype_array COMMA INTLIT RSB;

// Keywords
BREAK: 'Break';
CONTINUE: 'Continue';
IF: 'If';
ELSEIF: 'Elseif';
ELSE: 'Else';
FOREACH: 'Foreach';
TRUE: 'True';
FALSE: 'False';
ARRAY: 'Array';
IN: 'In';
INT: 'Int';
FLOAT: 'Float';
BOOLEAN: 'Boolean';
STRING: 'String';
RETURN: 'Return';
NULL: 'Null';
CLASS: 'Class';
VAL: 'Val';
VAR: 'Var';
CONSTRUCTOR: 'Constructor';
DESTRUCTOR: 'Destructor';
NEW: 'New';
BY: 'By';
SELF: 'Self';
dtype: INT | FLOAT | BOOLEAN | STRING | array_decl | ID;
dtype_array: INT | FLOAT | BOOLEAN | STRING | array_decl;

//Operators
ADD: '+';
MINUS: '-';
MULTIPLY: '*';
DIVIDE: '/';
MODULUS: '%';
NOT: '!';
AND: '&&';
OR: '||';
EQUAL: '==';
ASSIGN: '=';
UNEQUAL: '!=';
GREATER: '>';
LESS_EQ: '<=';
LESS: '<';
GREATER_EQ: '>=';
COMPARE_STR: '==.';
CONCAT_STR: '+.';
DOUBLE_COLON: '::';
COLON: ':';

// Seperators
LP: '(';
RP: ')';
LSB: '[';
RSB: ']';
DOT: '.';
COMMA: ',';
SEMI: ';';
LCB: '{';
RCB: '}';

// Identifiers
ID: (LETTER | '_')(LETTER | DIGIT | '_')*;
STATIC_ID: DOLLAR (LETTER | DIGIT | '_')+;

// ERROR RAISE
fragment DBQUOTE_IN_STR: '\'"';
fragment ESCAPE_SEQUENCE: '\\' [bfrnt'\\];
fragment VALID_CHARACTER: ~[\b\f\n\r\t\\"] | ESCAPE_SEQUENCE | DBQUOTE_IN_STR;
fragment ILLEGAL_CHARACTER: '\\' (~[bfrnt'\\])?;

// Outliers
WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

UNCLOSE_STRING: DOUBLE_QUOTE VALID_CHARACTER* { raise UncloseString(self.text[1:])};
ERROR_CHAR: . {raise ErrorToken(self.text)};
ILLEGAL_ESCAPE: DOUBLE_QUOTE VALID_CHARACTER* ILLEGAL_CHARACTER {
		raise IllegalEscape(self.text[1:])
};