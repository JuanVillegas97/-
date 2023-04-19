import ply.yacc as yacc
from lexer import tokens

def p_program(p):
    '''
    program : PROGRAM LPAREN RPAREN block
    '''
    p[0] = "PROGRAM COMPILED"

def p_block(p):
    '''
    block : LBRACE statement_list RBRACE
            | empty
    '''

def p_statement_list(p):
    '''
    statement_list : statement
                    | statement_list statement
    '''

def p_statement(p): 
    '''
    statement : variable_declaration
                | variable_assignation
    '''

def p_variable_assignation(p):
    '''
    variable_assignation : ID EQUALS expression SEMICOLON
    '''

def p_variable_declaration(p):
    '''
    variable_declaration : simple_type id_list SEMICOLON
                        | simple_type LBRACK CTEI RBRACK id_list SEMICOLON
    '''
    # Your code here

def p_id_list(p):
    '''
    id_list : ID
            | id_list COMMA ID
    '''

def p_simple_type(p):
    '''
    simple_type : INT
                | FLOAT
                | CHAR
                | STRING
                | BOOLEAN
    '''

def p_expression(p):
    '''
    expression : factor 
                | expression PLUS factor
                | expression MINUS factor
    '''

def p_term(p):
    '''
    term : factor 
        | term TIMES factor
        | term DIVIDE factor
    '''

def p_factor(p):
    '''
    factor : ID
        | cte
        | LPAREN expression RPAREN
    '''
    
def p_cte(p):
    '''
    cte : CTEI
        | CTEF
        | CTEC
        | CTES
        | CTEB
    '''

def p_empty(p):
    '''
    empty :
    '''
    pass
    
#! LEFT TO DO MORE STAMENTS

def p_error(p):
    if p:
        print("Syntax error at line %d, token=%s" % (p.lineno, p.type))
    else:
        print("Syntax error: unexpected end of input")

# Build the parser
parser = yacc.yacc(debug=True)

input_string = '''
プログラム(){
    整数 number, uwu;
    整数[1] numasdsadber;

}
'''
result = parser.parse(input_string)
print(result)
