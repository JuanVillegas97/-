import ply.yacc as yacc
from lexer import tokens

def p_program(p):
    '''
    program : PROGRAM ID SEMICOLON var_declaration functions MAIN body END
    '''
    p[0] = "PROGRAM COMPILED"


def p_functions(p):
    '''
    functions : functions function
                    | function
    '''

def p_function(p):
    '''
    function : FUNCTION simple_type ID LPAREN parameters RPAREN body
            | empty
    '''

def p_parameters(p):
    '''
    parameters : parameter_list
                | empty
    '''

def p_parameter_list(p):
    '''
    parameter_list : parameter
                    | parameter_list COMMA parameter
    '''

def p_parameter(p):
    '''
    parameter : simple_type ID 
    '''

def p_body(p):
    '''
    body : LBRACE statement RBRACE
    '''

def p_statement(p):
    '''
    statement : assingation
            | empty
    '''

def p_assingation(p):
    '''
    assingation : variable ASSIGN expression SEMICOLON
    '''

def p_var_declaration(p):
    '''
    var_declaration : VARIABLE simple_type variables SEMICOLON
                    | empty
    '''
    # implementation of variable_declaration function

def p_variables(p):
    '''
    variables : variables COMMA variable
            | variable
    '''
    # implementation of variables function

def p_variable(p):
    '''
    variable : ID
            | ID LBRACK expression RBRACK
            | ID LBRACK expression RBRACK LBRACK expression RBRACK
    '''
    # implementation of variable function

def p_simple_type(p):
    '''
    simple_type : INT
                | FLOAT
                | CHAR
                | STRING
                | BOOLEAN
    '''
    # implementation of simple_type function


def p_expression(p):
    '''
    expression : t_expression 
            | t_expression ASSIGN t_expression
    '''

def p_t_expression(p):
    '''
    t_expression : g_expression 
                | g_expression AND g_expression
                | g_expression OR  g_expression
    '''

def p_g_expression(p):
    '''
    g_expression : m_expression 
                | m_expression LESS     m_expression
                | m_expression GREATER  m_expression
                | m_expression EQUALS   m_expression
                | m_expression NOTEQUAL m_expression
    '''

def p_m_expression(p):
    '''
    m_expression : term 
                | term PLUS term
                | term MINUS term
    '''

def p_term(p):
    '''
    term : factor 
        | factor TIMES factor
        | factor DIVIDE factor
    '''
    # implementation of term function

def p_factor(p):
    '''
    factor : variable
        | cte
        | LPAREN expression RPAREN 
    '''
    # implementation of factor function

def p_cte(p):
    '''
    cte : CTEI
        | CTEF
        | CTEC
        | CTES
        | CTEB
    '''
    # implementation of cte function

def p_empty(p):
    '''
    empty :
    '''
    pass


# def p_block(p):
#     '''
#     block : LBRACE statement_list RBRACE comment_opt
#             | empty
#     '''


# def p_comment_opt(p):
#     '''
#     comment_opt : comment
#                 | empty
#     '''

# def p_comment(p):
#     '''
#     comment : COMMENT
#     '''

# def p_statement_list(p):
#     '''
#     statement_list : statement
#                     | statement_list statement
#     '''

# def p_statement(p): 
#     '''
#     statement : variable_assignation
#                 | declaration
#                 | variable_init
#                 | multi_declaration
#                 | empty
#     '''


def p_error(p):
    if p:
        print("Syntax error at line %d, token=%s" % (p.lineno, p.type))
    else:
        print("Syntax error: unexpected end of input")

def error(token):
    print(f"Syntax error: Unexpected token '{token.value}' at line {token.lineno}, column {token.lexpos}")



parser = yacc.yacc(debug=True)

input_string = '''
プログラム my_program;

変数 整数 x, y[10], z[5][5];

関数 整数 myFunc(整数 x, 整数 y){
    x = 5 + 2;
}

関数 文字 myFun_2(整数 x, 整数 y){
    y = 2 + a;
}

メイン{

}

エンド
'''
result = parser.parse(input_string)
print(result)
