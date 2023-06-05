
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'nonassocLESSGREATEREQUALSNOTEQUALLESSTHANGREATERTHANleftPLUSMINUSleftTIMESDIVIDErightASSIGNAND ASSIGN BOOLEAN CHAR COLON COMMA COMMENT CTEB CTEC CTEF CTEI CTES DIVIDE DO ELSE ENCRYPT END EQUALS FLOAT FOR FROM FUNCTION GENKEY GREATER GREATERTHAN ID IF INT LBRACE LBRACK LESS LESSTHAN LPAREN MAIN MINUS NOT NOTEQUAL OR PLUS PRINT PROGRAM RBRACE RBRACK READ RETURN RPAREN SEMICOLON SPECIAL STRING THEN TIMES VARIABLE VOID WHILE\n    program : PROGRAM ID SEMICOLON global_scope var_declarations functions main END\n    \n    global_scope : empty\n    \n    functions : functions function\n                    | function\n                    | empty\n    \n    function : FUNCTION function_signature block\n    \n    function_signature : simple_type ID function_1 LPAREN open_var_declaration parameters close_var_declaration RPAREN var_declarations\n                    | VOID ID function_1 LPAREN open_var_declaration parameters close_var_declaration RPAREN var_declarations\n    \n    return : RETURN expressions SEMICOLON\n    \n    function_1 : empty\n    \n    main : MAIN LPAREN RPAREN main_scope var_declarations block\n    \n    main_scope : empty\n    \n    var_declarations : var_declaration_list\n                    | empty\n    \n    var_declaration_list : var_declaration var_declarations\n    \n    var_declaration : VARIABLE open_var_declaration simple_type variables SEMICOLON close_var_declaration\n    \n    open_var_declaration : empty\n    \n    close_var_declaration : empty\n    \n    variables : variable \n            | variable COMMA variables\n    \n    variable : ID\n            | ID LBRACK expression RBRACK\n            | ID LBRACK expression RBRACK LBRACK expression RBRACK\n    \n    parameters : parameters  COMMA parameter\n    | parameter\n    | empty\n    \n    parameter : simple_type ID \n    \n    block : LBRACE block2 RBRACE\n    \n    block2 : block3\n           | empty\n    \n    block3 : statement block2\n    \n    statement : special_func \n    | assingation\n    | for\n    | do_while\n    | while\n    | if_else\n    | invocation\n    | if\n    | print\n    | read \n    \n    special_func : gen_key\n                | encrypt\n    \n    gen_key : GENKEY LPAREN RPAREN SPECIAL ID SEMICOLON\n    \n    encrypt : ENCRYPT LPAREN ID COMMA ID RPAREN SPECIAL ID SEMICOLON\n    \n    read : READ LPAREN ID RPAREN SEMICOLON\n    \n    assing_to_call : variable ASSIGN invocation\n    \n    do_while : DO breadcrumb block WHILE LPAREN expression RPAREN gotot SEMICOLON \n    \n    for : FOR LPAREN ID for_1 ASSIGN expression for_2 FROM expression RPAREN for_3 DO block for_4\n    \n    for_1 : empty\n    \n    for_2 : empty\n    \n    for_3 : empty\n    \n    for_4 : empty\n    \n    while : WHILE breadcrumb LPAREN expression RPAREN gotof block\n    \n    breadcrumb : empty\n    \n    if : IF LPAREN expression  RPAREN gotof block\n    \n    if_else : IF LPAREN  expression  RPAREN  gotof block  ELSE goto block\n    \n    gotot : empty\n    \n    goto : empty\n    \n    gotof : empty\n    \n    variable_list : variable\n                  | variable_list COMMA variable\n    \n    invocation : ID invocation_1 LPAREN  invocation_2 expressions RPAREN invocation_5 SEMICOLON invocation_6 \n    \n    invocation_1 : empty\n    \n    invocation_2 : empty\n    \n    invocation_3 : empty\n    \n    invocation_4 : empty\n    \n    invocation_5 : empty\n    \n    invocation_6 : empty\n    \n    expressions : expressions COMMA invocation_4 expression invocation_3\n                | expression invocation_3\n                | empty\n    \n    expression : t_expression \n                | NOT t_expression\n    \n    print : PRINT LPAREN print_arguments RPAREN SEMICOLON\n    \n    print_arguments : print_argument\n                    | print_arguments COMMA print_argument\n    \n    print_argument : CTES\n                    | expression\n    \n    assingation : variable ASSIGN expression SEMICOLON\n    \n    t_expression : g_expression \n                | t_expression boolean_operator g_expression\n    \n    g_expression : m_expression \n                | g_expression comparison_operator m_expression\n    \n    m_expression : term \n                |  m_expression addition_operator term\n    \n    term : factor \n        |  term multiplication_operator factor\n    \n    factor : variable\n            | cte\n            | invocation\n            | expression_parenthesis\n    \n    expression_parenthesis : LPAREN expression RPAREN \n    \n    comparison_operator : LESS\n                        | GREATER\n                        | EQUALS\n                        | NOTEQUAL\n                        | GREATERTHAN\n                        | LESSTHAN\n    \n    addition_operator : PLUS\n                    | MINUS\n    \n    boolean_operator : AND\n                    | OR\n    \n    multiplication_operator : TIMES\n                            | DIVIDE\n    \n    simple_type : INT\n                | FLOAT\n                | CHAR\n                | BOOLEAN\n                | STRING\n    \n    cte : CTEI\n        | CTEF\n        | CTEC\n        | CTEB\n        | CTES\n    \n    empty :\n    '
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,31,],[0,-1,]),'ID':([2,23,24,25,26,27,28,29,30,34,44,45,46,47,48,49,50,51,52,53,54,55,56,71,72,75,77,78,84,85,86,88,97,111,115,117,129,130,131,133,134,135,136,137,138,139,140,141,142,143,144,145,148,151,152,157,159,160,161,166,172,176,180,182,192,197,198,208,209,211,213,216,217,225,226,228,229,230,235,236,237,],[3,35,36,-106,-107,-108,-109,-110,39,59,59,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,39,94,-28,94,114,94,94,123,125,94,94,-116,94,94,-102,-103,94,-94,-95,-96,-97,-98,-99,94,-100,-101,94,-104,-105,-80,94,-65,94,183,184,185,94,94,94,-75,-46,-116,-56,-44,94,-67,-54,223,94,-116,-63,-69,-48,-57,-45,-116,-49,-53,]),'SEMICOLON':([3,37,38,39,93,94,96,98,99,100,101,102,103,104,105,106,107,108,109,110,113,128,132,156,158,167,168,169,170,171,183,191,203,206,207,210,217,219,220,223,225,226,],[4,70,-19,-21,-20,-21,-73,-81,-83,-85,-87,-89,-90,-91,-92,-111,-112,-113,-114,-115,148,-22,-74,180,182,-82,-84,-86,-88,-93,198,-116,-23,217,-68,-116,-116,228,-58,230,-63,-69,]),'VARIABLE':([4,5,6,10,40,70,73,74,91,92,200,202,],[-116,11,-2,11,-116,-116,11,-12,-16,-18,11,11,]),'FUNCTION':([4,5,6,7,8,9,10,12,13,14,16,20,33,70,75,91,92,],[-116,-116,-2,15,-13,-14,-116,15,-4,-5,-15,-3,-6,-116,-28,-16,-18,]),'MAIN':([4,5,6,7,8,9,10,12,13,14,16,20,33,70,75,91,92,],[-116,-116,-2,-116,-13,-14,-116,21,-4,-5,-15,-3,-6,-116,-28,-16,-18,]),'LBRACE':([8,9,10,16,22,40,60,70,73,74,81,82,91,92,112,155,177,178,179,196,200,202,212,214,215,221,222,234,],[-13,-14,-116,-15,34,-116,-116,-116,-116,-12,34,-55,-16,-18,34,-116,-116,34,-60,34,-116,-116,-116,-7,-8,34,-59,34,]),'INT':([11,15,17,18,89,90,126,127,187,],[-116,25,25,-17,-116,-116,25,25,25,]),'FLOAT':([11,15,17,18,89,90,126,127,187,],[-116,26,26,-17,-116,-116,26,26,26,]),'CHAR':([11,15,17,18,89,90,126,127,187,],[-116,27,27,-17,-116,-116,27,27,27,]),'BOOLEAN':([11,15,17,18,89,90,126,127,187,],[-116,28,28,-17,-116,-116,28,28,28,]),'STRING':([11,15,17,18,89,90,126,127,187,],[-116,29,29,-17,-116,-116,29,29,29,]),'VOID':([15,],[24,]),'COMMA':([18,38,39,89,90,94,96,98,99,100,101,102,103,104,105,106,107,108,109,110,115,119,120,121,122,125,126,127,128,132,151,152,162,163,164,165,167,168,169,170,171,173,174,175,181,185,193,194,201,203,217,218,225,226,227,],[-17,71,-21,-116,-116,-21,-73,-81,-83,-85,-87,-89,-90,-91,-92,-111,-112,-113,-114,-115,-116,157,-76,-78,-79,160,-116,-116,-22,-74,-116,-65,187,-25,-26,187,-82,-84,-86,-88,-93,192,-116,-72,-77,-27,-71,-66,-24,-23,-116,-116,-63,-69,-70,]),'RPAREN':([18,32,87,89,90,92,94,96,98,99,100,101,102,103,104,105,106,107,108,109,110,115,118,119,120,121,122,123,126,127,128,132,146,151,152,154,162,163,164,165,167,168,169,170,171,173,174,175,181,184,185,186,188,193,194,195,201,203,217,218,224,225,226,227,],[-17,40,124,-116,-116,-18,-21,-73,-81,-83,-85,-87,-89,-90,-91,-92,-111,-112,-113,-114,-115,-116,155,156,-76,-78,-79,158,-116,-116,-22,-74,171,-116,-65,177,-116,-25,-26,-116,-82,-84,-86,-88,-93,191,-116,-72,-77,199,-27,200,202,-71,-66,210,-24,-23,-116,-116,231,-63,-69,-70,]),'END':([19,75,147,],[31,-28,-11,]),'LPAREN':([21,35,36,58,59,61,62,63,64,65,66,67,68,69,72,77,79,80,82,83,84,85,94,97,111,115,117,129,130,131,133,134,135,136,137,138,139,140,141,142,143,144,145,151,152,153,157,166,172,176,192,208,209,216,],[32,-116,-116,78,-116,-116,84,85,86,87,88,89,-10,90,111,111,115,-64,-55,117,111,111,-116,111,111,-116,111,111,-102,-103,111,-94,-95,-96,-97,-98,-99,111,-100,-101,111,-104,-105,111,-65,176,111,111,111,111,-116,111,-67,111,]),'RBRACE':([34,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,75,76,148,180,182,197,198,211,217,225,226,228,229,230,235,236,237,],[-116,75,-29,-30,-116,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-28,-31,-80,-75,-46,-56,-44,-54,-116,-63,-69,-48,-57,-45,-116,-49,-53,]),'FOR':([34,44,45,46,47,48,49,50,51,52,53,54,55,56,75,148,180,182,197,198,211,217,225,226,228,229,230,235,236,237,],[58,58,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-28,-80,-75,-46,-56,-44,-54,-116,-63,-69,-48,-57,-45,-116,-49,-53,]),'DO':([34,44,45,46,47,48,49,50,51,52,53,54,55,56,75,148,180,182,197,198,211,217,225,226,228,229,230,231,232,233,235,236,237,],[60,60,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-28,-80,-75,-46,-56,-44,-54,-116,-63,-69,-48,-57,-45,-116,234,-52,-116,-49,-53,]),'WHILE':([34,44,45,46,47,48,49,50,51,52,53,54,55,56,75,116,148,180,182,197,198,211,217,225,226,228,229,230,235,236,237,],[61,61,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-28,153,-80,-75,-46,-56,-44,-54,-116,-63,-69,-48,-57,-45,-116,-49,-53,]),'IF':([34,44,45,46,47,48,49,50,51,52,53,54,55,56,75,148,180,182,197,198,211,217,225,226,228,229,230,235,236,237,],[62,62,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-28,-80,-75,-46,-56,-44,-54,-116,-63,-69,-48,-57,-45,-116,-49,-53,]),'PRINT':([34,44,45,46,47,48,49,50,51,52,53,54,55,56,75,148,180,182,197,198,211,217,225,226,228,229,230,235,236,237,],[63,63,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-28,-80,-75,-46,-56,-44,-54,-116,-63,-69,-48,-57,-45,-116,-49,-53,]),'READ':([34,44,45,46,47,48,49,50,51,52,53,54,55,56,75,148,180,182,197,198,211,217,225,226,228,229,230,235,236,237,],[64,64,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-28,-80,-75,-46,-56,-44,-54,-116,-63,-69,-48,-57,-45,-116,-49,-53,]),'GENKEY':([34,44,45,46,47,48,49,50,51,52,53,54,55,56,75,148,180,182,197,198,211,217,225,226,228,229,230,235,236,237,],[65,65,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-28,-80,-75,-46,-56,-44,-54,-116,-63,-69,-48,-57,-45,-116,-49,-53,]),'ENCRYPT':([34,44,45,46,47,48,49,50,51,52,53,54,55,56,75,148,180,182,197,198,211,217,225,226,228,229,230,235,236,237,],[66,66,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-28,-80,-75,-46,-56,-44,-54,-116,-63,-69,-48,-57,-45,-116,-49,-53,]),'LBRACK':([39,59,94,128,],[72,72,72,166,]),'ASSIGN':([57,59,114,128,149,150,203,],[77,-21,-116,-22,172,-50,-23,]),'NOT':([72,77,84,85,111,115,117,151,152,157,166,172,176,192,208,209,216,],[97,97,97,97,97,-116,97,97,-65,97,97,97,97,-116,97,-67,97,]),'CTEI':([72,77,84,85,97,111,115,117,129,130,131,133,134,135,136,137,138,139,140,141,142,143,144,145,151,152,157,166,172,176,192,208,209,216,],[106,106,106,106,106,106,-116,106,106,-102,-103,106,-94,-95,-96,-97,-98,-99,106,-100,-101,106,-104,-105,106,-65,106,106,106,106,-116,106,-67,106,]),'CTEF':([72,77,84,85,97,111,115,117,129,130,131,133,134,135,136,137,138,139,140,141,142,143,144,145,151,152,157,166,172,176,192,208,209,216,],[107,107,107,107,107,107,-116,107,107,-102,-103,107,-94,-95,-96,-97,-98,-99,107,-100,-101,107,-104,-105,107,-65,107,107,107,107,-116,107,-67,107,]),'CTEC':([72,77,84,85,97,111,115,117,129,130,131,133,134,135,136,137,138,139,140,141,142,143,144,145,151,152,157,166,172,176,192,208,209,216,],[108,108,108,108,108,108,-116,108,108,-102,-103,108,-94,-95,-96,-97,-98,-99,108,-100,-101,108,-104,-105,108,-65,108,108,108,108,-116,108,-67,108,]),'CTEB':([72,77,84,85,97,111,115,117,129,130,131,133,134,135,136,137,138,139,140,141,142,143,144,145,151,152,157,166,172,176,192,208,209,216,],[109,109,109,109,109,109,-116,109,109,-102,-103,109,-94,-95,-96,-97,-98,-99,109,-100,-101,109,-104,-105,109,-65,109,109,109,109,-116,109,-67,109,]),'CTES':([72,77,84,85,97,111,115,117,129,130,131,133,134,135,136,137,138,139,140,141,142,143,144,145,151,152,157,166,172,176,192,208,209,216,],[110,110,110,121,110,110,-116,110,110,-102,-103,110,-94,-95,-96,-97,-98,-99,110,-100,-101,110,-104,-105,110,-65,121,110,110,110,-116,110,-67,110,]),'ELSE':([75,197,],[-28,212,]),'TIMES':([94,100,101,102,103,104,105,106,107,108,109,110,121,128,169,170,171,203,217,225,226,],[-21,144,-87,-89,-90,-91,-92,-111,-112,-113,-114,-115,-115,-22,144,-88,-93,-23,-116,-63,-69,]),'DIVIDE':([94,100,101,102,103,104,105,106,107,108,109,110,121,128,169,170,171,203,217,225,226,],[-21,145,-87,-89,-90,-91,-92,-111,-112,-113,-114,-115,-115,-22,145,-88,-93,-23,-116,-63,-69,]),'PLUS':([94,99,100,101,102,103,104,105,106,107,108,109,110,121,128,168,169,170,171,203,217,225,226,],[-21,141,-85,-87,-89,-90,-91,-92,-111,-112,-113,-114,-115,-115,-22,141,-86,-88,-93,-23,-116,-63,-69,]),'MINUS':([94,99,100,101,102,103,104,105,106,107,108,109,110,121,128,168,169,170,171,203,217,225,226,],[-21,142,-85,-87,-89,-90,-91,-92,-111,-112,-113,-114,-115,-115,-22,142,-86,-88,-93,-23,-116,-63,-69,]),'LESS':([94,98,99,100,101,102,103,104,105,106,107,108,109,110,121,128,167,168,169,170,171,203,217,225,226,],[-21,134,-83,-85,-87,-89,-90,-91,-92,-111,-112,-113,-114,-115,-115,-22,134,-84,-86,-88,-93,-23,-116,-63,-69,]),'GREATER':([94,98,99,100,101,102,103,104,105,106,107,108,109,110,121,128,167,168,169,170,171,203,217,225,226,],[-21,135,-83,-85,-87,-89,-90,-91,-92,-111,-112,-113,-114,-115,-115,-22,135,-84,-86,-88,-93,-23,-116,-63,-69,]),'EQUALS':([94,98,99,100,101,102,103,104,105,106,107,108,109,110,121,128,167,168,169,170,171,203,217,225,226,],[-21,136,-83,-85,-87,-89,-90,-91,-92,-111,-112,-113,-114,-115,-115,-22,136,-84,-86,-88,-93,-23,-116,-63,-69,]),'NOTEQUAL':([94,98,99,100,101,102,103,104,105,106,107,108,109,110,121,128,167,168,169,170,171,203,217,225,226,],[-21,137,-83,-85,-87,-89,-90,-91,-92,-111,-112,-113,-114,-115,-115,-22,137,-84,-86,-88,-93,-23,-116,-63,-69,]),'GREATERTHAN':([94,98,99,100,101,102,103,104,105,106,107,108,109,110,121,128,167,168,169,170,171,203,217,225,226,],[-21,138,-83,-85,-87,-89,-90,-91,-92,-111,-112,-113,-114,-115,-115,-22,138,-84,-86,-88,-93,-23,-116,-63,-69,]),'LESSTHAN':([94,98,99,100,101,102,103,104,105,106,107,108,109,110,121,128,167,168,169,170,171,203,217,225,226,],[-21,139,-83,-85,-87,-89,-90,-91,-92,-111,-112,-113,-114,-115,-115,-22,139,-84,-86,-88,-93,-23,-116,-63,-69,]),'AND':([94,96,98,99,100,101,102,103,104,105,106,107,108,109,110,121,128,132,167,168,169,170,171,203,217,225,226,],[-21,130,-81,-83,-85,-87,-89,-90,-91,-92,-111,-112,-113,-114,-115,-115,-22,130,-82,-84,-86,-88,-93,-23,-116,-63,-69,]),'OR':([94,96,98,99,100,101,102,103,104,105,106,107,108,109,110,121,128,132,167,168,169,170,171,203,217,225,226,],[-21,131,-81,-83,-85,-87,-89,-90,-91,-92,-111,-112,-113,-114,-115,-115,-22,131,-82,-84,-86,-88,-93,-23,-116,-63,-69,]),'RBRACK':([94,95,96,98,99,100,101,102,103,104,105,106,107,108,109,110,128,132,167,168,169,170,171,189,203,217,225,226,],[-21,128,-73,-81,-83,-85,-87,-89,-90,-91,-92,-111,-112,-113,-114,-115,-22,-74,-82,-84,-86,-88,-93,203,-23,-116,-63,-69,]),'FROM':([94,96,98,99,100,101,102,103,104,105,106,107,108,109,110,128,132,167,168,169,170,171,190,203,204,205,217,225,226,],[-21,-73,-81,-83,-85,-87,-89,-90,-91,-92,-111,-112,-113,-114,-115,-22,-74,-82,-84,-86,-88,-93,-116,-23,216,-51,-116,-63,-69,]),'SPECIAL':([124,199,],[159,213,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'global_scope':([4,],[5,]),'empty':([4,5,7,10,11,34,35,36,40,44,59,60,61,70,73,89,90,94,114,115,126,127,151,155,162,165,174,177,190,191,192,200,202,210,212,217,218,231,235,],[6,9,14,9,18,43,68,68,74,43,80,82,82,92,9,18,18,80,150,152,164,164,175,179,92,92,194,179,205,207,209,9,9,220,222,226,194,233,237,]),'var_declarations':([5,10,73,200,202,],[7,16,112,214,215,]),'var_declaration_list':([5,10,73,200,202,],[8,8,8,8,8,]),'var_declaration':([5,10,73,200,202,],[10,10,10,10,10,]),'functions':([7,],[12,]),'function':([7,12,],[13,20,]),'open_var_declaration':([11,89,90,],[17,126,127,]),'main':([12,],[19,]),'function_signature':([15,],[22,]),'simple_type':([15,17,126,127,187,],[23,30,161,161,161,]),'block':([22,81,112,178,196,221,234,],[33,116,147,197,211,229,235,]),'variables':([30,71,],[37,93,]),'variable':([30,34,44,71,72,77,84,85,97,111,117,129,133,140,143,151,157,166,172,176,208,216,],[38,57,57,38,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,]),'block2':([34,44,],[41,76,]),'block3':([34,44,],[42,42,]),'statement':([34,44,],[44,44,]),'special_func':([34,44,],[45,45,]),'assingation':([34,44,],[46,46,]),'for':([34,44,],[47,47,]),'do_while':([34,44,],[48,48,]),'while':([34,44,],[49,49,]),'if_else':([34,44,],[50,50,]),'invocation':([34,44,72,77,84,85,97,111,117,129,133,140,143,151,157,166,172,176,208,216,],[51,51,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,]),'if':([34,44,],[52,52,]),'print':([34,44,],[53,53,]),'read':([34,44,],[54,54,]),'gen_key':([34,44,],[55,55,]),'encrypt':([34,44,],[56,56,]),'function_1':([35,36,],[67,69,]),'main_scope':([40,],[73,]),'invocation_1':([59,94,],[79,79,]),'breadcrumb':([60,61,],[81,83,]),'close_var_declaration':([70,162,165,],[91,186,188,]),'expression':([72,77,84,85,111,117,151,157,166,172,176,208,216,],[95,113,118,122,146,154,174,122,189,190,195,218,224,]),'t_expression':([72,77,84,85,97,111,117,151,157,166,172,176,208,216,],[96,96,96,96,132,96,96,96,96,96,96,96,96,96,]),'g_expression':([72,77,84,85,97,111,117,129,151,157,166,172,176,208,216,],[98,98,98,98,98,98,98,167,98,98,98,98,98,98,98,]),'m_expression':([72,77,84,85,97,111,117,129,133,151,157,166,172,176,208,216,],[99,99,99,99,99,99,99,99,168,99,99,99,99,99,99,99,]),'term':([72,77,84,85,97,111,117,129,133,140,151,157,166,172,176,208,216,],[100,100,100,100,100,100,100,100,100,169,100,100,100,100,100,100,100,]),'factor':([72,77,84,85,97,111,117,129,133,140,143,151,157,166,172,176,208,216,],[101,101,101,101,101,101,101,101,101,101,170,101,101,101,101,101,101,101,]),'cte':([72,77,84,85,97,111,117,129,133,140,143,151,157,166,172,176,208,216,],[103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,]),'expression_parenthesis':([72,77,84,85,97,111,117,129,133,140,143,151,157,166,172,176,208,216,],[105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,]),'print_arguments':([85,],[119,]),'print_argument':([85,157,],[120,181,]),'boolean_operator':([96,132,],[129,129,]),'comparison_operator':([98,167,],[133,133,]),'addition_operator':([99,168,],[140,140,]),'multiplication_operator':([100,169,],[143,143,]),'for_1':([114,],[149,]),'invocation_2':([115,],[151,]),'parameters':([126,127,],[162,165,]),'parameter':([126,127,187,],[163,163,201,]),'expressions':([151,],[173,]),'gotof':([155,177,],[178,196,]),'invocation_3':([174,218,],[193,227,]),'for_2':([190,],[204,]),'invocation_5':([191,],[206,]),'invocation_4':([192,],[208,]),'gotot':([210,],[219,]),'goto':([212,],[221,]),'invocation_6':([217,],[225,]),'for_3':([231,],[232,]),'for_4':([235,],[236,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID SEMICOLON global_scope var_declarations functions main END','program',8,'p_program','grammar.py',29),
  ('global_scope -> empty','global_scope',1,'p_global_scope','grammar.py',35),
  ('functions -> functions function','functions',2,'p_functions','grammar.py',51),
  ('functions -> function','functions',1,'p_functions','grammar.py',52),
  ('functions -> empty','functions',1,'p_functions','grammar.py',53),
  ('function -> FUNCTION function_signature block','function',3,'p_function','grammar.py',58),
  ('function_signature -> simple_type ID function_1 LPAREN open_var_declaration parameters close_var_declaration RPAREN var_declarations','function_signature',9,'p_function_signature','grammar.py',71),
  ('function_signature -> VOID ID function_1 LPAREN open_var_declaration parameters close_var_declaration RPAREN var_declarations','function_signature',9,'p_function_signature','grammar.py',72),
  ('return -> RETURN expressions SEMICOLON','return',3,'p_return','grammar.py',79),
  ('function_1 -> empty','function_1',1,'p_function_1','grammar.py',92),
  ('main -> MAIN LPAREN RPAREN main_scope var_declarations block','main',6,'p_main','grammar.py',111),
  ('main_scope -> empty','main_scope',1,'p_main_scope','grammar.py',121),
  ('var_declarations -> var_declaration_list','var_declarations',1,'p_var_declarations','grammar.py',134),
  ('var_declarations -> empty','var_declarations',1,'p_var_declarations','grammar.py',135),
  ('var_declaration_list -> var_declaration var_declarations','var_declaration_list',2,'p_var_declaration_list','grammar.py',141),
  ('var_declaration -> VARIABLE open_var_declaration simple_type variables SEMICOLON close_var_declaration','var_declaration',6,'p_var_declaration','grammar.py',149),
  ('open_var_declaration -> empty','open_var_declaration',1,'p_open_var_declaration','grammar.py',159),
  ('close_var_declaration -> empty','close_var_declaration',1,'p_close_var_declaration','grammar.py',165),
  ('variables -> variable','variables',1,'p_variables','grammar.py',172),
  ('variables -> variable COMMA variables','variables',3,'p_variables','grammar.py',173),
  ('variable -> ID','variable',1,'p_variable','grammar.py',186),
  ('variable -> ID LBRACK expression RBRACK','variable',4,'p_variable','grammar.py',187),
  ('variable -> ID LBRACK expression RBRACK LBRACK expression RBRACK','variable',7,'p_variable','grammar.py',188),
  ('parameters -> parameters COMMA parameter','parameters',3,'p_parameters','grammar.py',197),
  ('parameters -> parameter','parameters',1,'p_parameters','grammar.py',198),
  ('parameters -> empty','parameters',1,'p_parameters','grammar.py',199),
  ('parameter -> simple_type ID','parameter',2,'p_parameter','grammar.py',205),
  ('block -> LBRACE block2 RBRACE','block',3,'p_block','grammar.py',219),
  ('block2 -> block3','block2',1,'p_block2','grammar.py',225),
  ('block2 -> empty','block2',1,'p_block2','grammar.py',226),
  ('block3 -> statement block2','block3',2,'p_block3','grammar.py',232),
  ('statement -> special_func','statement',1,'p_statement','grammar.py',240),
  ('statement -> assingation','statement',1,'p_statement','grammar.py',241),
  ('statement -> for','statement',1,'p_statement','grammar.py',242),
  ('statement -> do_while','statement',1,'p_statement','grammar.py',243),
  ('statement -> while','statement',1,'p_statement','grammar.py',244),
  ('statement -> if_else','statement',1,'p_statement','grammar.py',245),
  ('statement -> invocation','statement',1,'p_statement','grammar.py',246),
  ('statement -> if','statement',1,'p_statement','grammar.py',247),
  ('statement -> print','statement',1,'p_statement','grammar.py',248),
  ('statement -> read','statement',1,'p_statement','grammar.py',249),
  ('special_func -> gen_key','special_func',1,'p_special_func','grammar.py',257),
  ('special_func -> encrypt','special_func',1,'p_special_func','grammar.py',258),
  ('gen_key -> GENKEY LPAREN RPAREN SPECIAL ID SEMICOLON','gen_key',6,'p_gen_key','grammar.py',264),
  ('encrypt -> ENCRYPT LPAREN ID COMMA ID RPAREN SPECIAL ID SEMICOLON','encrypt',9,'p_encrypt','grammar.py',280),
  ('read -> READ LPAREN ID RPAREN SEMICOLON','read',5,'p_read','grammar.py',300),
  ('assing_to_call -> variable ASSIGN invocation','assing_to_call',3,'p_assing_to_call','grammar.py',312),
  ('do_while -> DO breadcrumb block WHILE LPAREN expression RPAREN gotot SEMICOLON','do_while',9,'p_do_while','grammar.py',318),
  ('for -> FOR LPAREN ID for_1 ASSIGN expression for_2 FROM expression RPAREN for_3 DO block for_4','for',14,'p_for','grammar.py',323),
  ('for_1 -> empty','for_1',1,'p_for_1','grammar.py',328),
  ('for_2 -> empty','for_2',1,'p_for_2','grammar.py',341),
  ('for_3 -> empty','for_3',1,'p_for_3','grammar.py',369),
  ('for_4 -> empty','for_4',1,'p_for_4','grammar.py',405),
  ('while -> WHILE breadcrumb LPAREN expression RPAREN gotof block','while',7,'p_while','grammar.py',449),
  ('breadcrumb -> empty','breadcrumb',1,'p_breadcrumb','grammar.py',455),
  ('if -> IF LPAREN expression RPAREN gotof block','if',6,'p_if','grammar.py',461),
  ('if_else -> IF LPAREN expression RPAREN gotof block ELSE goto block','if_else',9,'p_if_else','grammar.py',468),
  ('gotot -> empty','gotot',1,'p_gotot','grammar.py',475),
  ('goto -> empty','goto',1,'p_goto','grammar.py',481),
  ('gotof -> empty','gotof',1,'p_gotof','grammar.py',487),
  ('variable_list -> variable','variable_list',1,'p_variable_list','grammar.py',497),
  ('variable_list -> variable_list COMMA variable','variable_list',3,'p_variable_list','grammar.py',498),
  ('invocation -> ID invocation_1 LPAREN invocation_2 expressions RPAREN invocation_5 SEMICOLON invocation_6','invocation',9,'p_invocation','grammar.py',508),
  ('invocation_1 -> empty','invocation_1',1,'p_invocation_1','grammar.py',516),
  ('invocation_2 -> empty','invocation_2',1,'p_invocation_2','grammar.py',524),
  ('invocation_3 -> empty','invocation_3',1,'p_invocation_3','grammar.py',532),
  ('invocation_4 -> empty','invocation_4',1,'p_invocation_4','grammar.py',540),
  ('invocation_5 -> empty','invocation_5',1,'p_invocation_5','grammar.py',548),
  ('invocation_6 -> empty','invocation_6',1,'p_invocation_6','grammar.py',554),
  ('expressions -> expressions COMMA invocation_4 expression invocation_3','expressions',5,'p_expressions','grammar.py',562),
  ('expressions -> expression invocation_3','expressions',2,'p_expressions','grammar.py',563),
  ('expressions -> empty','expressions',1,'p_expressions','grammar.py',564),
  ('expression -> t_expression','expression',1,'p_expression','grammar.py',569),
  ('expression -> NOT t_expression','expression',2,'p_expression','grammar.py',570),
  ('print -> PRINT LPAREN print_arguments RPAREN SEMICOLON','print',5,'p_print','grammar.py',582),
  ('print_arguments -> print_argument','print_arguments',1,'p_print_arguments','grammar.py',589),
  ('print_arguments -> print_arguments COMMA print_argument','print_arguments',3,'p_print_arguments','grammar.py',590),
  ('print_argument -> CTES','print_argument',1,'p_print_argument','grammar.py',602),
  ('print_argument -> expression','print_argument',1,'p_print_argument','grammar.py',603),
  ('assingation -> variable ASSIGN expression SEMICOLON','assingation',4,'p_assingation','grammar.py',629),
  ('t_expression -> g_expression','t_expression',1,'p_t_expression','grammar.py',643),
  ('t_expression -> t_expression boolean_operator g_expression','t_expression',3,'p_t_expression','grammar.py',644),
  ('g_expression -> m_expression','g_expression',1,'p_g_expression','grammar.py',654),
  ('g_expression -> g_expression comparison_operator m_expression','g_expression',3,'p_g_expression','grammar.py',655),
  ('m_expression -> term','m_expression',1,'p_m_expression','grammar.py',665),
  ('m_expression -> m_expression addition_operator term','m_expression',3,'p_m_expression','grammar.py',666),
  ('term -> factor','term',1,'p_term','grammar.py',676),
  ('term -> term multiplication_operator factor','term',3,'p_term','grammar.py',677),
  ('factor -> variable','factor',1,'p_factor','grammar.py',687),
  ('factor -> cte','factor',1,'p_factor','grammar.py',688),
  ('factor -> invocation','factor',1,'p_factor','grammar.py',689),
  ('factor -> expression_parenthesis','factor',1,'p_factor','grammar.py',690),
  ('expression_parenthesis -> LPAREN expression RPAREN','expression_parenthesis',3,'p_expression_parenthesis','grammar.py',701),
  ('comparison_operator -> LESS','comparison_operator',1,'p_comparison_operator','grammar.py',708),
  ('comparison_operator -> GREATER','comparison_operator',1,'p_comparison_operator','grammar.py',709),
  ('comparison_operator -> EQUALS','comparison_operator',1,'p_comparison_operator','grammar.py',710),
  ('comparison_operator -> NOTEQUAL','comparison_operator',1,'p_comparison_operator','grammar.py',711),
  ('comparison_operator -> GREATERTHAN','comparison_operator',1,'p_comparison_operator','grammar.py',712),
  ('comparison_operator -> LESSTHAN','comparison_operator',1,'p_comparison_operator','grammar.py',713),
  ('addition_operator -> PLUS','addition_operator',1,'p_addition_operator','grammar.py',719),
  ('addition_operator -> MINUS','addition_operator',1,'p_addition_operator','grammar.py',720),
  ('boolean_operator -> AND','boolean_operator',1,'p_boolean_operator','grammar.py',726),
  ('boolean_operator -> OR','boolean_operator',1,'p_boolean_operator','grammar.py',727),
  ('multiplication_operator -> TIMES','multiplication_operator',1,'p_multiplication_operator','grammar.py',733),
  ('multiplication_operator -> DIVIDE','multiplication_operator',1,'p_multiplication_operator','grammar.py',734),
  ('simple_type -> INT','simple_type',1,'p_simple_type','grammar.py',740),
  ('simple_type -> FLOAT','simple_type',1,'p_simple_type','grammar.py',741),
  ('simple_type -> CHAR','simple_type',1,'p_simple_type','grammar.py',742),
  ('simple_type -> BOOLEAN','simple_type',1,'p_simple_type','grammar.py',743),
  ('simple_type -> STRING','simple_type',1,'p_simple_type','grammar.py',744),
  ('cte -> CTEI','cte',1,'p_cte','grammar.py',750),
  ('cte -> CTEF','cte',1,'p_cte','grammar.py',751),
  ('cte -> CTEC','cte',1,'p_cte','grammar.py',752),
  ('cte -> CTEB','cte',1,'p_cte','grammar.py',753),
  ('cte -> CTES','cte',1,'p_cte','grammar.py',754),
  ('empty -> <empty>','empty',0,'p_empty','grammar.py',762),
]
