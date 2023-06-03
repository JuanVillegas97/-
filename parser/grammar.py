from lexer.tokens import tokens
from constants.constants import *
from compiler.sematnic_cube import SemanticCube
from compiler.functions_directory import FunctionsDirectory
from compiler.intermidiate_representation import IntermediateRepresentation
from compiler.interfaces.quadruple import Quadruple
from compiler.neural_points_handler import NeuralPointsHandler
from compiler.interfaces.variable import variable
# Because PLY is a bottom-up and cannot be converted to a top-down it's difficult to track stuff
# The rules named with ..._scope are neural points to prepare the variable table
precedence = (
     ('nonassoc', 'LESS', 'GREATER', 'EQUALS', 'NOTEQUAL', 'LESSTHAN', 'GREATERTHAN'),  # Nonassociative operators
     ('left', 'PLUS', 'MINUS'),
     ('left', 'TIMES', 'DIVIDE'),
     ('right', 'ASSIGN')
)

directory = FunctionsDirectory.get_instance()
inter_rep = IntermediateRepresentation.get_instance()
neural_points_handler = NeuralPointsHandler()
cube = SemanticCube()
#* MANAGES VIRTUAL ADDRESS LOOK
inter_rep.set_virtual_address(True)
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
    directory.set_program_name(function_name)
    directory.set_current(function_name,function_type,scope)
    directory.add_function()
    
    new_quadruple = Quadruple(GOTOMAIN,"","","_")
    inter_rep.push(QUADRUPLES,new_quadruple)
    inter_rep.push(JUMPS,1)

    

def p_functions(p):
    '''
    functions : functions function
                    | function
                    | empty
    '''

def p_function(p):
    '''
    function : FUNCTION function_signature function_body
    '''

def p_function_signature(p):
    '''
    function_signature : simple_type ID function_1 LPAREN open_var_declaration parameters close_var_declaration RPAREN var_declarations
                    | VOID ID function_1 LPAREN open_var_declaration parameters close_var_declaration RPAREN var_declarations
    '''
    # Process the function signature

def p_function_body(p):
    '''
    function_body : LBRACE statements return_stmt RBRACE
                | LBRACE statements RBRACE
    '''
    new_quadruple = Quadruple(ENDFUNC,"","","")
    inter_rep.push(QUADRUPLES,new_quadruple)
    
    num_of_temporals = inter_rep.get_temporal_counter()
    directory.set_resource(TEMPORALS,num_of_temporals)
    
    inter_rep.reset_temporal_counter()

def p_return_stmt(p):
    '''
    return_stmt : RETURN expression SEMICOLON
    '''
    return_value = inter_rep.pop(OPERANDS)
    return_type = inter_rep.pop(TYPES) #!vereify type with singature
    new_quadruple = Quadruple(RETURN,"","",return_value)
    inter_rep.push(QUADRUPLES,new_quadruple)
    inter_rep.print_stacks()
    


def p_empty_return_stmt(p):
    '''
    return_stmt : RETURN SEMICOLON
    '''
    # Process the empty return statement
    
def p_function_1(p):
    '''
    function_1 : empty
    '''
    function_name = p[-1] 
    function_type = p[-2]
    neural_points_handler.function_1(function_name,function_type,LOCAL)
    
    #* HANDELS THE CONVERTION TO ADDRESSS I 
    directory.add_typed_func_to_global()
    
    


def p_main(p):
    '''
    main : MAIN LPAREN RPAREN main_scope var_declarations LBRACE statements RBRACE
    '''
    num_of_temporals = inter_rep.get_temporal_counter()
    directory.set_resource(TEMPORALS,num_of_temporals)
    
    new_quadruple = Quadruple(END,"","","")
    inter_rep.push(QUADRUPLES,new_quadruple)

def p_main_scope(p):
    '''
    main_scope : empty
    '''
    function_name = "MAIN"
    function_type = "MAIN"
    scope = "LOCAL"
    directory.set_current(function_name,function_type,scope)
    directory.add_function()
    
    inter_rep.fill() 

def p_var_declarations(p):
    '''
    var_declarations : var_declaration_list
                    | empty
    '''
    p[0] = p[1]

def p_var_declaration_list(p):
    '''
    var_declaration_list : var_declaration var_declarations
    '''

#? 2 neuronal points open and close variable declaration so I can cehck if and id has already been declared 
#? This can be seen in p_variable
def p_var_declaration(p):
    '''
    var_declaration : VARIABLE open_var_declaration simple_type variables SEMICOLON close_var_declaration
    '''
    type = p[3]
    ids = p[4]
    directory.add_variable(ids,type)
    
    directory.add_resource(ids,VARIABLES)
    
def p_open_var_declaration(p):
    '''
    open_var_declaration : empty
    '''
    directory.set_is_variable_declaration_true()
    
def p_close_var_declaration(p):
    '''
    close_var_declaration : empty
    '''
    directory.set_is_variable_declaration_false()
    

def p_variables(p):
    '''
    variables : variable 
            | variable COMMA variables
    '''
    if len(p) == 2:
        # Only one variable was matched
        p[0] = [p[1]]
    else:
        # Multiple variables were matched
        p[3].insert(0, p[1])  # Add the current variable to the list
        p[0] = p[3]

# Here if is not open the variable declaration search for the id
def p_variable(p):
    '''
    variable : ID
            | ID LBRACK expression RBRACK
            | ID LBRACK expression RBRACK LBRACK expression RBRACK
    '''
    id = p[1]
    p[0] = id
    if not directory.get_is_variable_declaration():
        directory.search_variable(id)

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
    directory.add_parameters(type)
    directory.add_variable([ids],type)
    directory.add_resource([ids],PARAMETERS)
    
def p_statements(p):
    '''
    statements : statements statement
    | statement
    | empty
    '''

def p_statement(p):
    '''
    statement : read 
    | for
    | do_while
    | while
    | if_else
    | invocation
    | if
    | assingation
    | return
    | print
    '''

def p_do_while(p):
    '''
    do_while : DO breadcrumb LBRACE statements RBRACE WHILE LPAREN expression RPAREN gotot SEMICOLON 
    '''

def p_for(p):
    '''
    for : FOR LPAREN ID for_1 ASSIGN expression for_2 FROM expression RPAREN for_3 DO LBRACE statements RBRACE for_4
    '''
#   
def p_for_1(p):
    '''
    for_1 : empty
    '''
    id = p[-1]
    function_name = directory.get_current_function_name()
    variable = directory.get_variable(function_name,id)
    if variable.type != INT:
        raise TypeError("Type-mismatch lower limit must be an integer value")
    else:
        inter_rep.push(OPERANDS,id)
        inter_rep.push(TYPES,variable.type)

def p_for_2(p):
    '''
    for_2 : empty
    '''
    exp_type = inter_rep.pop(TYPES)
    if exp_type != INT:
        raise TypeError("Type-mismatch lower limit must be an integer value")
    else:
        exp = inter_rep.pop(OPERANDS)
        v_control = inter_rep.top(OPERANDS)
        control_type = inter_rep.top(TYPES)
        res_type = cube.get_type(control_type,exp_type,ASSIGN)
        if res_type == ERROR:
            raise Exception("Type-mismatch")
        else:
            new_quadruple = Quadruple(ASSIGN,exp,"",v_control)
            new_quadrupleVControl = Quadruple(ASSIGN,v_control,"",VCONTROL)
            inter_rep.push(QUADRUPLES,new_quadruple)
            inter_rep.push(QUADRUPLES,new_quadrupleVControl)
            

def p_for_3(p): 
    '''
    for_3 : empty
    '''
    exp_type = inter_rep.pop(TYPES)
    if exp_type != INT:
        raise TypeError("Type-mismatch lower limit must be an integer value")
    else:
        exp = inter_rep.pop(OPERANDS)
        new_quadruple = Quadruple(ASSIGN,exp,"",VFINAL)
        inter_rep.push(QUADRUPLES,new_quadruple)
        new_temporal = inter_rep.generate_avail()
        new_quadruple = Quadruple(LESS,VCONTROL,VFINAL,new_temporal)
        inter_rep.push(QUADRUPLES,new_quadruple)
        cont = len(inter_rep.get_stack(QUADRUPLES))
        inter_rep.push(JUMPS,cont)
        new_quadruple = Quadruple(GOTOF,new_temporal,"","_")
        inter_rep.push(QUADRUPLES,new_quadruple)
        cont = len(inter_rep.get_stack(QUADRUPLES))
        inter_rep.push(JUMPS,cont)
        
def p_for_4(p): 
    '''
    for_4 : empty
    '''
    new_temporal = inter_rep.generate_avail()
    new_quadruple = Quadruple(PLUS,VCONTROL,"1",new_temporal)
    inter_rep.push(QUADRUPLES,new_quadruple)
    
    new_quadruple = Quadruple(ASSIGN,new_temporal,"",VCONTROL)
    inter_rep.push(QUADRUPLES,new_quadruple)
    
    original_id = inter_rep.top(OPERANDS)
    new_quadruple = Quadruple(ASSIGN,new_temporal,"",original_id)
    inter_rep.push(QUADRUPLES,new_quadruple)
    
    end = inter_rep.pop(JUMPS)-1
    ret = inter_rep.pop(JUMPS)
    new_quadruple = Quadruple(GOTO,"","",ret)
    inter_rep.push(QUADRUPLES,new_quadruple)
    quadruples_stack = inter_rep.get_stack(QUADRUPLES)
    quadruples_stack[end].set_avail(len(quadruples_stack)+1)
    
    delete_original_id = inter_rep.pop(OPERANDS)
    delete_type = inter_rep.pop(TYPES)
        
def p_while(p):
    '''
    while : WHILE breadcrumb LPAREN expression RPAREN gotof LBRACE statements RBRACE
    '''
    inter_rep.fill_while()

def p_breadcrumb(p):
    '''
    breadcrumb : empty
    '''
    inter_rep.push_breadcrumb() # Empujar la migajona de pan ole!
    
def p_if(p):
    '''
    if : IF LPAREN expression  RPAREN gotof LBRACE statements RBRACE
    '''
    inter_rep.fill()
    
def p_if_else(p):
    '''
    if_else : IF LPAREN  expression  RPAREN  gotof LBRACE statements RBRACE  ELSE goto LBRACE statements RBRACE
    '''
    inter_rep.fill()

def p_gotot(p):
    '''
    gotot : empty
    '''
    inter_rep.gotot_while()
    
def p_goto(p):
    '''
    goto : empty
    '''
    inter_rep.gotof_if_else()
    
def p_gotof(p):
    '''
    gotof : empty
    '''
    inter_rep.gotof_if()
    
def p_return(p):
    '''
    return : RETURN expression SEMICOLON
    '''

def p_read(p):
    '''
    read : READ LPAREN variable_list RPAREN SEMICOLON
    '''
    variables = p[3]
    for variable in variables:
        new_quadruple = Quadruple("read","","",variable)
        inter_rep.push(QUADRUPLES,new_quadruple)

def p_variable_list(p):
    '''
    variable_list : variable
                  | variable_list COMMA variable
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[3])
        p[0] = p[1]

def p_invocation(p):
    '''
    invocation : ID invocation_1 LPAREN  invocation_2 expressions RPAREN invocation_5 SEMICOLON invocation_6    '''
    
def p_invocation_1(p):
    '''
    invocation_1 : empty
    '''
    invocation_id = p[-1]
    neural_points_handler.invocation_1(invocation_id)
    
def p_invocation_2(p):
    '''
    invocation_2 : empty
    '''
    neural_points_handler.invocation_2()
    
def p_invocation_3(p):
    '''
    invocation_3 : empty
    '''
    neural_points_handler.invocation_3()
    
def p_invocation_4(p):
    '''
    invocation_4 : empty
    '''
    neural_points_handler.invocation_4()
    
def p_invocation_5(p):
    '''
    invocation_5 : empty
    '''
    neural_points_handler.invocation_5()
    
def p_invocation_6(p):
    '''
    invocation_6 : empty
    '''
    neural_points_handler.invocation_6()
    
def p_expressions(p):
    '''
    expressions : expressions COMMA invocation_4 expression invocation_3
                | expression invocation_3
                | empty
    '''
    
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
        name, type = inter_rep.get_temporal_info()

def p_print(p):
    '''
    print : PRINT LPAREN print_arguments RPAREN SEMICOLON
    '''
    
def p_print_arguments(p):
    '''
    print_arguments : print_argument
                    | print_arguments COMMA print_argument
    '''
    type_printed = inter_rep.pop(TYPES) #!Don't know what to do with them
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
        #* HANDELS THE CONVERTION TO ADDRESSS I
        virtual_address = inter_rep.get_virtual_address()
        if virtual_address:
            print_operand = inter_rep.convert_operand_to_address(print_operand)
        #*
        new_quadruple = Quadruple(PRINT,"","",print_operand)
    else: #Means it's a string therfore I gotta create anew quadruple with print statement
        new_quadruple = Quadruple(PRINT,"","",p[1])
    inter_rep.push(QUADRUPLES,new_quadruple)
    inter_rep.print_stacks()
    
def p_assingation(p):
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
                | BOOLEAN
    '''
    p[0] = p[1]

#? Adding constants to the constant table
def p_cte(p):
    '''
    cte : CTEI
        | CTEF
        | CTEC
        | CTEB
    '''
    p[0] = p[1]
    value = p[1]


    directory.add_constant(value)

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




