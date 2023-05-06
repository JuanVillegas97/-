from lexer.tokens import tokens
from compiler.functions_directory import functionsDirectory

directory = functionsDirectory()


def p_program(p):
    '''
    program : PROGRAM ID SEMICOLON var_declarations functions MAIN LPAREN RPAREN var_declarations LBRACE statements RBRACE END
    '''
    directory.current_function_name = p[2]  # Extract the function name from the parsed tokens
    directory.add_function(directory.current_function_name , type)

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
    # directory.has_variable_table(directory.current_variable_type)
    print(directory.current_function_name)
    # print(p[3])


def p_variables(p):
    '''
    variables : variable COMMA variables
            | variable
    '''
    p[0] = p[1]
    # print(p[0])
    # print(p)
    

def p_variable(p):
    '''
    variable : ID
            | ID LBRACK expression RBRACK
            | ID LBRACK expression RBRACK LBRACK expression RBRACK
    '''
    p[0] = p[1]  # Assign the ID as the default value


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
    directory.current_function_name = p[3]  # Extract the function name from the parsed tokens
    type = p[2] if p[2] != "VOID" else None  # Extract the function type (None for void functions)
    # Add the function to the directory
    directory.add_function(directory.current_function_name , type)





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
    | if
    | read
    | return
    | print
    '''

def p_print(p):
    '''
    print : PRINT LPAREN expression RPAREN SEMICOLON
    print : PRINT LPAREN CTES RPAREN SEMICOLON
    '''

def p_if(p):
    '''
    if : IF LPAREN expression RPAREN LBRACE statements RBRACE 
        | IF LPAREN expression RPAREN LBRACE statements RBRACE ELSE LBRACE statements RBRACE 
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
            | invocation
    '''

def p_comparison_operator(p):
    '''
    comparison_operator : LESS
                        | GREATER
                        | EQUALS
                        | NOTEQUAL
    '''


precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('nonassoc', 'EQUALS', 'NOTEQUAL'),
    ('nonassoc', 'LESS', 'GREATER'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)


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
    p[0] = p[1]
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
        error_message = f"Syntax error at line {p.lineno}, token={p.type}"
        raise SyntaxError(error_message)
    else:
        raise SyntaxError("Syntax error: unexpected end of input")


def error(token):
    print(f"Syntax error: Unexpected token '{token.value}' at line {token.lineno}, column {token.lexpos}")




