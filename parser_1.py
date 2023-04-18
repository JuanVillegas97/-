import ply.yacc as yacc
from lexer import tokens

def p_program(p):
    'program : PROGRAM ID SEMICOLON'
    p[0] = (p[1], p[2])


# def p_block(p):
#     '''
#     program : LBRACE RBRACE
#     '''


def p_empty(p):
    'empty :'
    pass

# # Error rule for syntax errors
# def p_error(p):
#     print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

input_string = "プログラム あ;"
result = parser.parse(input_string)
print(result)
