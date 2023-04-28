import ply.yacc as yacc
from my_lexer import tokens

def p_program(p):
    '''
    program : PROGRAM ID SEMICOLON var_declarations functions MAIN LPAREN RPAREN var_declarations LBRACE statements RBRACE END
    '''
    p[0] = "PROGRAM COMPILED"

def p_var_declarations(p):
    '''
    var_declarations : var_declarations var_declaration 
                    | var_declaration
                    | empty
    '''

def p_var_declaration(p):
    '''
    var_declaration : VARIABLE simple_type variables SEMICOLON
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

def p_functions(p):
    '''
    functions : functions function
                    | function
                    | empty

    '''

def p_function(p):
    '''
    function : FUNCTION simple_type ID LPAREN parameters RPAREN var_declarations LBRACE statements statement RBRACE
            |  FUNCTION VOID ID LPAREN parameters RPAREN var_declarations LBRACE statements RBRACE
    '''

def p_parameters(p):
    '''
    parameters : parameters  COMMA parameter
                | parameter
                | empty
    '''

def p_parameter(p):
    '''
    parameter : simple_type ID 
    '''

def p_statements(p):
    '''
    statements : statements statement
            | statement
            | empty
    '''

def p_statement(p):
    '''
    statement : assingation
            | invocation
            | read
            | return
    '''

def p_return(p):
    '''
    return : RETURN expression SEMICOLON
    '''

def p_read(p):
    '''
    read : READ LPAREN variable RPAREN SEMICOLON
    '''

def p_assingation(p):
    '''
    assingation : variable ASSIGN expression SEMICOLON
    '''


def p_invocation(p):
    '''
    invocation : ID LPAREN expressions RPAREN SEMICOLON
    '''

def p_expressions(p):
    '''
    expressions : expressions COMMA expression  
                | expression
                | empty
    '''

def p_expression(p):
    '''
    expression : t_expression 
                | t_expression ASSIGN t_expression
    '''

def p_t_expression(p):
    '''
    t_expression : g_expression 
                | g_expression boolean_operator g_expression
    '''

def p_g_expression(p):
    '''
    g_expression : m_expression 
                | m_expression comparison_operator m_expression
    '''

def p_m_expression(p):
    '''
    m_expression : term 
                | term addition_operator term
    '''

def p_term(p):
    '''
    term : factor 
        | factor multiplication_operator factor
    '''

def p_factor(p):
    '''
    factor : variable
            | cte
            | LPAREN expression RPAREN 
    '''

def p_comparison_operator(p):
    '''
    comparison_operator : LESS
                        | GREATER
                        | EQUALS
                        | NOTEQUAL
    '''

def p_addition_operator(p):
    '''
    addition_operator : PLUS
                    | MINUS
    '''

def p_boolean_operator(p):
    '''
    boolean_operator : AND
                    | OR
    '''

def p_multiplication_operator(p):
    '''
    multiplication_operator : TIMES
                            | DIVIDE
    '''

def p_simple_type(p):
    '''
    simple_type : INT
                | FLOAT
                | CHAR
                | STRING
                | BOOLEAN
    '''
    # implementation of simple_type function

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


# def p_comment_opt(p):
#     '''
#     comment_opt : comment
#                 | empty
#     '''

# def p_comment(p):
#     '''
#     comment : COMMENT
#     '''



def p_error(p):
    if p:
        print("Syntax error at line %d, token=%s" % (p.lineno, p.type))
    else:
        print("Syntax error: unexpected end of input")

def error(token):
    print(f"Syntax error: Unexpected token '{token.value}' at line {token.lineno}, column {token.lexpos}")




parser = yacc.yacc(debug=True)

with open("input.txt", "r",encoding="utf-8") as file:
    code = file.read()

result = parser.parse(code)