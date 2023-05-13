from lexer.tokens import tokens
from compiler.functions_directory import functionsDirectory
from compiler.intermidiate_representation import intermediateRepresentation
from compiler.quadruple import Quadruple
# Because PLY is a bottom-up and cannot be converted to a top-down it's difficult to track stuff
# The rules named with ..._scope are neural points to prepare the variable table

OPERATORS  ="operators"
TYPES      ="types"
OPERANDS   ="operands"
QUADRUPLES ="quadruples"
JUMPS      ="jumps"

precedence = (
     ('nonassoc', 'LESS', 'GREATER', 'EQUALS', 'NOTEQUAL', 'LESSTHAN', 'GREATERTHAN'),  # Nonassociative operators
     ('left', 'PLUS', 'MINUS'),
     ('left', 'TIMES', 'DIVIDE'),
     ('right', 'ASSIGN')
)

directory = functionsDirectory()
inter_rep = intermediateRepresentation()
def p_program(p):
    '''
    program : PROGRAM ID SEMICOLON global_scope var_declarations functions main END
    '''
    p[0] = "PROGRAM COMPILED"


def p_global_scope(p):
    '''
    global_scope : empty
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
    function_scope : empty
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
    main_scope : empty
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
    statement : read 
    | invocation
    | if
    | assingation
    | return
    | print
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


    
def p_print(p):
    '''
    print : PRINT LPAREN print_arguments RPAREN SEMICOLON
    '''
    
def p_print_arguments(p):
    '''
    print_arguments : print_argument
                    | print_arguments COMMA print_argument
    '''
    p[0] = p[1]
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[3])
        p[0] = p[1]

    
def p_print_argument(p):
    '''
    print_argument : CTES
                   | expression
    '''
    if p[1] == None: #Means it is an expression therefore I gotta create a new quadruple with print statement
        print_operand = inter_rep.pop(OPERANDS)
        new_quadruple = Quadruple("print","","",print_operand)
    else: #Means it's a string therfore I gotta create anew quadruple with print statement
        new_quadruple = Quadruple("print","","",p[1])
    inter_rep.push(QUADRUPLES,new_quadruple)
    inter_rep.print_stacks()
    
        
    



def p_assingation(p): #! STILL NEED TO SEARCH EXPRESSIONS IF THE DO EXIST!
    '''
    assingation : variable ASSIGN expression SEMICOLON
    '''
    variable = p[1]
    operator = p[2]
    directory.search_variable([variable])
    
    inter_rep.push(OPERANDS,variable)
    inter_rep.push(OPERATORS,operator)
    inter_rep.print_stacks()
    inter_rep.create_quadruple()
    
def p_expression(p): # instead of = it ahs to be not
    '''
    expression : t_expression 
                | NOT t_expression
    '''
    if len(p) == 4: # push opeartor
        operator = p[2]
        inter_rep.push(OPERATORS,operator)
        inter_rep.print_stacks()
        inter_rep.create_quadruple()

def p_t_expression(p):
    '''
    t_expression : g_expression 
                | t_expression boolean_operator g_expression
    '''
    if len(p) == 4: # Neural-point 2 POper.Push(* or /)
        operator = p[2]
        inter_rep.push(OPERATORS,operator)
        inter_rep.print_stacks()
        inter_rep.create_quadruple()


def p_g_expression(p):
    '''
    g_expression : m_expression 
                | g_expression comparison_operator m_expression
    '''
    if len(p) == 4: # Neural-point 2 POper.Push(* or /)
        operator = p[2]
        inter_rep.push(OPERATORS,operator)
        inter_rep.print_stacks()
        inter_rep.create_quadruple()

def p_m_expression(p):
    '''
    m_expression : term 
                |  m_expression addition_operator term
    '''
    if len(p) == 4: # Neural-point 2 POper.Push(* or /)
        operator = p[2]
        inter_rep.push(OPERATORS,operator)
        inter_rep.print_stacks()
        inter_rep.create_quadruple()


def p_term(p):
    '''
    term : factor 
        |  term multiplication_operator factor
    '''
    if len(p) == 4: # Neural-point 2 POper.Push(* or /)
        operator = p[2]
        inter_rep.push(OPERATORS,operator)
        inter_rep.print_stacks()
        inter_rep.create_quadruple()



def p_factor(p):
    '''
    factor : variable
            | cte
            | expression_parenthesis
            | invocation
    '''
    id = p[1]
    if id != None: # Neurla-point 1 PilaO.Push(id.name) and PTypes.Push(id.type)
        current_function_name = directory.get_current_function_name()
        current_variable  = directory.get_variable(current_function_name,id)
        inter_rep.push(OPERANDS,current_variable.id)
        inter_rep.push(TYPES,current_variable.type)

def p_expression_parenthesis(p):
    '''
    expression_parenthesis : LPAREN expression RPAREN 
    '''
    p[0] = p[2]
    
    
def p_comparison_operator(p):
    '''
    comparison_operator : LESS
                        | GREATER
                        | EQUALS
                        | NOTEQUAL
                        | GREATERTHAN
                        | LESSTHAN
    '''
    p[0] = p[1]

def p_addition_operator(p):
    '''
    addition_operator : PLUS
                    | MINUS
    '''
    p[0] = p[1]


def p_boolean_operator(p):
    '''
    boolean_operator : AND
                    | OR
    '''
    p[0] = p[1]


def p_multiplication_operator(p):
    '''
    multiplication_operator : TIMES
                            | DIVIDE
    '''
    p[0] = p[1]

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
    p[0] = p[1]
    # implementation of cte function

def p_empty(p):
    '''
    empty :
    '''
    pass


def p_error(p):
    if p:
        error_message = f"Syntax error at line {p.lineno}, token={p.type}, value={p.value}, "
        raise SyntaxError(error_message)
    else:
        raise SyntaxError("Syntax error: unexpected end of input")


def error(token):
    print(f"Syntax error: Unexpected token '{token.value}' at line {token.lineno}, column {token.lexpos}")




