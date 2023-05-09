from lexer.tokens import tokens
from compiler.functions_directory import functionsDirectory
from compiler.intermidiate_representation import intermediateRepresentation
# Because PLY is a bottom-up and cannot be converted to a top-down it's difficult to track stuff
# The rules named with ..._scope are neural points to prepare the variable table

directory = functionsDirectory()
Inter_Rep = intermediateRepresentation()
def p_program(p):
    '''
    program : PROGRAM ID SEMICOLON global_scope var_declarations functions main END
    '''
    p[0] = "PROGRAM COMPILED"


def p_global_scope(p):
    '''
    global_scope : 
    '''
    function_name = p[-2] 
    function_type = "PROGRAM"
    scope = "GLOBAL"
    directory.set_current(function_name,function_type,scope)
    directory.add_function()

def p_functions(p):
    '''
    functions : functions function
                    | function
                    | empty
    '''

def p_function(p):
    '''
    function : FUNCTION simple_type ID LPAREN function_scope parameters RPAREN var_declarations LBRACE statements RBRACE
            |  FUNCTION VOID ID LPAREN function_scope parameters RPAREN var_declarations LBRACE statements RBRACE
    '''

def p_function_scope(p):
    '''
    function_scope : 
    '''
    function_name = p[-2] 
    function_type = p[-3]
    scope = "LOCAL"
    directory.set_current(function_name,function_type,scope)
    directory.add_function()

def p_main(p):
    '''
    main : MAIN LPAREN RPAREN main_scope var_declarations LBRACE statements RBRACE
    '''

def p_main_scope(p):
    '''
    main_scope : 
    '''
    function_name = "MAIN"
    function_type = "MAIN"
    scope = "LOCAL"
    directory.set_current(function_name,function_type,scope)
    directory.add_function()


def p_var_declarations(p):
    '''
    var_declarations : var_declaration var_declarations 
                    | var_declaration
                    | empty
    '''
    p[0] = p[1]


def p_var_declaration(p):
    '''
    var_declaration : VARIABLE simple_type variables SEMICOLON
    '''
    type = p[2]
    ids = p[3]
    directory.add_variable(ids,type)


def p_variables(p):
    '''
    variables : variable COMMA variables
            | variable
    '''
    if len(p) == 2:
        # Only one variable was matched
        p[0] = [p[1]]
    else:
        # Multiple variables were matched
        p[3].insert(0, p[1])  # Add the current variable to the list
        p[0] = p[3]



def p_variable(p):
    '''
    variable : ID
            | ID LBRACK expression RBRACK
            | ID LBRACK expression RBRACK LBRACK expression RBRACK
    '''
    p[0] = p[1]



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
    type = p[1]
    ids = p[2]
    directory.add_variable([ids],type)
    

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




