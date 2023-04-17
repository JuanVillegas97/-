import ply.yacc as yacc
from lexer import tokens

def p_program(p):
    '''
    program : program_statement
            | empty
    '''
    p[0] = "コンパイルされたプログラム"
    pass

def p_program_statement(p):
    '''
    program_statement : var_declaration
                        | statement
    '''
    pass


def p_var_declaration(p):
    '''
    var_declaration : type ID SEMICOLON
    '''
    pass



def p_statement(p):
    '''
    statement : print_statement
                | assignment_statement
                | if_statement
                | while_statement
    '''
    pass

def p_print_statement(p):
    '''
    print_statement : PRINT LPAREN expression RPAREN SEMICOLON
    '''
    pass

def p_assignment_statement(p):
    '''
    assignment_statement : ID EQUALS expression SEMICOLON
    '''
    pass

def p_if_statement(p):
    '''
    if_statement : IF LPAREN expression RPAREN statement
                | IF LPAREN expression RPAREN statement ELSE statement
    '''
    pass

def p_while_statement(p):
    '''
    while_statement : WHILE LPAREN expression RPAREN statement
    '''
    pass

def p_expression(p):
    '''
    expression : expression PLUS term
            | expression MINUS term
            | term'''
    pass

def p_term(p):
    '''
    term : term TIMES factor
            | term DIVIDE factor
            | factor
        '''
    pass

def p_factor(p):
    '''
    factor : LPAREN expression RPAREN
    | ID
    | type
    '''
    pass

def p_type(p):
    '''
    type : INT
        | FLOAT
        | STRING
        | CHAR
    '''
    p[0] = p[1]

def p_empty(p):
    'empty :'
    pass

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

result = parser.parse("整数 dsd 数字;")
print(result)
