
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'nonassocLESSGREATEREQUALSNOTEQUALLESSTHANGREATERTHANleftPLUSMINUSleftTIMESDIVIDErightASSIGNAND ASSIGN BOOLEAN CHAR COLON COMMA COMMENT CTEB CTEC CTEF CTEI CTES DIVIDE DO ELSE END EQUALS FALSE FLOAT FUNCTION GREATER GREATERTHAN ID IF INT LBRACE LBRACK LESS LESSTHAN LPAREN MAIN MINUS NOT NOTEQUAL OR PLUS PRINT PROGRAM RBRACE RBRACK READ RETURN RPAREN SEMICOLON STRING THEN TIMES TRUE VARIABLE VOID WHILE\n    program : PROGRAM ID SEMICOLON global_scope var_declarations functions main END\n    \n    global_scope : empty\n    \n    functions : functions function\n                    | function\n                    | empty\n    \n    function : FUNCTION simple_type ID LPAREN function_scope open_var_declaration parameters close_var_declaration RPAREN var_declarations LBRACE statements RBRACE\n            |  FUNCTION VOID ID LPAREN function_scope open_var_declaration parameters close_var_declaration RPAREN var_declarations LBRACE statements RBRACE\n    \n    function_scope : empty\n    \n    main : MAIN LPAREN RPAREN main_scope var_declarations LBRACE statements RBRACE\n    \n    main_scope : empty\n    \n    var_declarations : var_declaration var_declarations \n                    | var_declaration\n                    | empty\n    \n    var_declaration : VARIABLE open_var_declaration simple_type variables SEMICOLON close_var_declaration\n    \n    open_var_declaration : empty\n    \n    close_var_declaration : empty\n    \n    variables : variable \n            | variable COMMA variables\n    \n    variable : ID\n            | ID LBRACK expression RBRACK\n            | ID LBRACK expression RBRACK LBRACK expression RBRACK\n    \n    parameters : parameters  COMMA parameter\n    | parameter\n    | empty\n    \n    parameter : simple_type ID \n    \n    statements : statements statement\n    | statement\n    | empty\n    \n    statement : read \n    | do_while\n    | while\n    | if_else\n    | invocation\n    | if\n    | assingation\n    | return\n    | print\n    \n    do_while : DO breadcrumb LBRACE statements RBRACE WHILE LPAREN expression RPAREN gotot SEMICOLON \n    \n    while : WHILE breadcrumb LPAREN expression RPAREN gotof LBRACE statements RBRACE\n    \n    breadcrumb : empty\n    \n    if : IF LPAREN expression RPAREN gotof LBRACE statements RBRACE\n    \n    if_else : IF LPAREN expression RPAREN  gotof LBRACE statements RBRACE  ELSE goto LBRACE statements RBRACE\n    \n    gotot : empty\n    \n    goto : empty\n    \n    gotof : empty\n    \n    return : RETURN expression SEMICOLON\n    \n    read : READ LPAREN variable_list RPAREN SEMICOLON\n    \n    variable_list : variable\n                  | variable_list COMMA variable\n    \n    invocation : ID LPAREN expressions RPAREN SEMICOLON\n    \n    expressions : expressions COMMA expression  \n                | expression\n                | empty\n    \n    print : PRINT LPAREN print_arguments RPAREN SEMICOLON\n    \n    print_arguments : print_argument\n                    | print_arguments COMMA print_argument\n    \n    print_argument : CTES\n                   | expression\n    \n    assingation : variable ASSIGN expression SEMICOLON\n    \n    expression : t_expression \n                | NOT t_expression\n    \n    t_expression : g_expression \n                | t_expression boolean_operator g_expression\n    \n    g_expression : m_expression \n                | g_expression comparison_operator m_expression\n    \n    m_expression : term \n                |  m_expression addition_operator term\n    \n    term : factor \n        |  term multiplication_operator factor\n    \n    factor : variable\n            | cte\n            | expression_parenthesis\n            | invocation\n    \n    expression_parenthesis : LPAREN expression RPAREN \n    \n    comparison_operator : LESS\n                        | GREATER\n                        | EQUALS\n                        | NOTEQUAL\n                        | GREATERTHAN\n                        | LESSTHAN\n    \n    addition_operator : PLUS\n                    | MINUS\n    \n    boolean_operator : AND\n                    | OR\n    \n    multiplication_operator : TIMES\n                            | DIVIDE\n    \n    simple_type : INT\n                | FLOAT\n                | CHAR\n                | BOOLEAN\n    \n    cte : CTEI\n        | CTEF\n        | CTEC\n        | CTEB\n    \n    empty :\n    '
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,28,],[0,-1,]),'ID':([2,21,22,23,24,25,26,27,39,40,52,65,69,71,72,73,75,76,77,78,79,80,81,82,83,84,85,86,87,89,90,98,104,105,106,107,108,109,110,111,112,113,114,115,122,129,132,133,137,138,140,144,149,150,153,161,162,165,167,168,169,170,176,178,179,182,185,186,187,189,190,192,198,199,200,201,],[3,30,31,-87,-88,-89,-90,34,34,49,49,49,49,49,-83,-84,49,-75,-76,-77,-78,-79,-80,49,-81,-82,49,-85,-86,120,124,49,120,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,49,49,-26,34,49,49,49,-50,120,49,-46,34,120,-59,49,120,120,-47,-54,120,120,120,49,120,120,120,-41,-39,-38,120,120,-42,]),'SEMICOLON':([3,32,33,34,48,49,51,53,54,55,56,57,58,59,60,61,62,63,64,70,74,99,100,101,102,103,128,139,144,146,152,160,166,191,194,195,],[4,38,-17,-19,-18,-19,-60,-62,-64,-66,-68,-70,-71,-72,-73,-91,-92,-93,-94,-20,-61,-63,-65,-67,-69,-74,144,153,-50,-21,165,170,176,-95,198,-43,]),'VARIABLE':([4,5,6,8,35,38,41,42,46,47,141,143,],[-95,10,-2,10,-95,-95,10,-10,-14,-16,10,10,]),'FUNCTION':([4,5,6,7,8,9,11,12,13,15,19,38,46,47,183,184,],[-95,-95,-2,14,-12,-13,14,-4,-5,-11,-3,-95,-14,-16,-6,-7,]),'MAIN':([4,5,6,7,8,9,11,12,13,15,19,38,46,47,183,184,],[-95,-95,-2,-95,-12,-13,20,-4,-5,-11,-3,-95,-14,-16,-6,-7,]),'LBRACE':([8,9,15,35,38,41,42,46,47,66,117,134,135,141,143,158,159,164,173,174,175,181,193,196,197,],[-12,-13,-11,-95,-95,-95,-10,-14,-16,89,-95,149,-40,-95,-95,168,169,-95,-95,182,-45,186,-95,199,-44,]),'INT':([10,14,16,17,36,37,43,44,45,67,68,126,],[-95,23,23,-15,-95,-95,-95,-8,-95,23,23,23,]),'FLOAT':([10,14,16,17,36,37,43,44,45,67,68,126,],[-95,24,24,-15,-95,-95,-95,-8,-95,24,24,24,]),'CHAR':([10,14,16,17,36,37,43,44,45,67,68,126,],[-95,25,25,-15,-95,-95,-95,-8,-95,25,25,25,]),'BOOLEAN':([10,14,16,17,36,37,43,44,45,67,68,126,],[-95,26,26,-15,-95,-95,-95,-8,-95,26,26,26,]),'VOID':([14,],[22,]),'COMMA':([17,33,34,36,37,43,44,45,49,51,53,54,55,56,57,58,59,60,61,62,63,64,67,68,69,70,74,91,92,93,94,95,96,97,99,100,101,102,103,124,142,144,145,146,147,148,154,155,156,157,171,177,],[-15,39,-19,-95,-95,-95,-8,-95,-19,-60,-62,-64,-66,-68,-70,-71,-72,-73,-91,-92,-93,-94,-95,-95,-95,-20,-61,126,-23,-24,126,129,-52,-53,-63,-65,-67,-69,-74,-25,-22,-50,-51,-21,161,-48,167,-55,-57,-58,-49,-56,]),'RPAREN':([17,29,34,36,37,43,44,45,47,49,51,53,54,55,56,57,58,59,60,61,62,63,64,67,68,69,70,74,88,91,92,93,94,95,96,97,99,100,101,102,103,124,125,127,142,144,145,146,147,148,151,154,155,156,157,163,171,177,188,],[-15,35,-19,-95,-95,-95,-8,-95,-16,-19,-60,-62,-64,-66,-68,-70,-71,-72,-73,-91,-92,-93,-94,-95,-95,-95,-20,-61,103,-95,-23,-24,-95,128,-52,-53,-63,-65,-67,-69,-74,-25,141,143,-22,-50,-51,-21,160,-48,164,166,-55,-57,-58,173,-49,-56,191,]),'END':([18,131,],[28,-9,]),'LPAREN':([20,30,31,40,49,52,65,69,71,72,73,75,76,77,78,79,80,81,82,83,84,85,86,87,98,116,118,119,120,122,123,129,135,136,137,138,140,150,167,180,185,],[29,36,37,65,69,65,65,65,65,-83,-84,65,-75,-76,-77,-78,-79,-80,65,-81,-82,65,-85,-86,65,133,-95,137,69,65,140,65,-40,150,65,65,65,65,65,185,65,]),'LBRACK':([34,49,70,120,],[40,40,98,40,]),'NOT':([40,65,69,98,122,129,137,138,140,150,167,185,],[52,52,52,52,52,52,52,52,52,52,52,52,]),'CTEI':([40,52,65,69,71,72,73,75,76,77,78,79,80,81,82,83,84,85,86,87,98,122,129,137,138,140,150,167,185,],[61,61,61,61,61,-83,-84,61,-75,-76,-77,-78,-79,-80,61,-81,-82,61,-85,-86,61,61,61,61,61,61,61,61,61,]),'CTEF':([40,52,65,69,71,72,73,75,76,77,78,79,80,81,82,83,84,85,86,87,98,122,129,137,138,140,150,167,185,],[62,62,62,62,62,-83,-84,62,-75,-76,-77,-78,-79,-80,62,-81,-82,62,-85,-86,62,62,62,62,62,62,62,62,62,]),'CTEC':([40,52,65,69,71,72,73,75,76,77,78,79,80,81,82,83,84,85,86,87,98,122,129,137,138,140,150,167,185,],[63,63,63,63,63,-83,-84,63,-75,-76,-77,-78,-79,-80,63,-81,-82,63,-85,-86,63,63,63,63,63,63,63,63,63,]),'CTEB':([40,52,65,69,71,72,73,75,76,77,78,79,80,81,82,83,84,85,86,87,98,122,129,137,138,140,150,167,185,],[64,64,64,64,64,-83,-84,64,-75,-76,-77,-78,-79,-80,64,-81,-82,64,-85,-86,64,64,64,64,64,64,64,64,64,]),'TIMES':([49,55,56,57,58,59,60,61,62,63,64,70,101,102,103,144,146,],[-19,86,-68,-70,-71,-72,-73,-91,-92,-93,-94,-20,86,-69,-74,-50,-21,]),'DIVIDE':([49,55,56,57,58,59,60,61,62,63,64,70,101,102,103,144,146,],[-19,87,-68,-70,-71,-72,-73,-91,-92,-93,-94,-20,87,-69,-74,-50,-21,]),'PLUS':([49,54,55,56,57,58,59,60,61,62,63,64,70,100,101,102,103,144,146,],[-19,83,-66,-68,-70,-71,-72,-73,-91,-92,-93,-94,-20,83,-67,-69,-74,-50,-21,]),'MINUS':([49,54,55,56,57,58,59,60,61,62,63,64,70,100,101,102,103,144,146,],[-19,84,-66,-68,-70,-71,-72,-73,-91,-92,-93,-94,-20,84,-67,-69,-74,-50,-21,]),'LESS':([49,53,54,55,56,57,58,59,60,61,62,63,64,70,99,100,101,102,103,144,146,],[-19,76,-64,-66,-68,-70,-71,-72,-73,-91,-92,-93,-94,-20,76,-65,-67,-69,-74,-50,-21,]),'GREATER':([49,53,54,55,56,57,58,59,60,61,62,63,64,70,99,100,101,102,103,144,146,],[-19,77,-64,-66,-68,-70,-71,-72,-73,-91,-92,-93,-94,-20,77,-65,-67,-69,-74,-50,-21,]),'EQUALS':([49,53,54,55,56,57,58,59,60,61,62,63,64,70,99,100,101,102,103,144,146,],[-19,78,-64,-66,-68,-70,-71,-72,-73,-91,-92,-93,-94,-20,78,-65,-67,-69,-74,-50,-21,]),'NOTEQUAL':([49,53,54,55,56,57,58,59,60,61,62,63,64,70,99,100,101,102,103,144,146,],[-19,79,-64,-66,-68,-70,-71,-72,-73,-91,-92,-93,-94,-20,79,-65,-67,-69,-74,-50,-21,]),'GREATERTHAN':([49,53,54,55,56,57,58,59,60,61,62,63,64,70,99,100,101,102,103,144,146,],[-19,80,-64,-66,-68,-70,-71,-72,-73,-91,-92,-93,-94,-20,80,-65,-67,-69,-74,-50,-21,]),'LESSTHAN':([49,53,54,55,56,57,58,59,60,61,62,63,64,70,99,100,101,102,103,144,146,],[-19,81,-64,-66,-68,-70,-71,-72,-73,-91,-92,-93,-94,-20,81,-65,-67,-69,-74,-50,-21,]),'AND':([49,51,53,54,55,56,57,58,59,60,61,62,63,64,70,74,99,100,101,102,103,144,146,],[-19,72,-62,-64,-66,-68,-70,-71,-72,-73,-91,-92,-93,-94,-20,72,-63,-65,-67,-69,-74,-50,-21,]),'OR':([49,51,53,54,55,56,57,58,59,60,61,62,63,64,70,74,99,100,101,102,103,144,146,],[-19,73,-62,-64,-66,-68,-70,-71,-72,-73,-91,-92,-93,-94,-20,73,-63,-65,-67,-69,-74,-50,-21,]),'RBRACK':([49,50,51,53,54,55,56,57,58,59,60,61,62,63,64,70,74,99,100,101,102,103,130,144,146,],[-19,70,-60,-62,-64,-66,-68,-70,-71,-72,-73,-91,-92,-93,-94,-20,-61,-63,-65,-67,-69,-74,146,-50,-21,]),'ASSIGN':([70,120,121,146,],[-20,-19,138,-21,]),'RBRACE':([89,104,105,106,107,108,109,110,111,112,113,114,115,132,144,149,153,162,165,168,169,170,176,178,179,182,186,187,189,190,192,198,199,200,201,],[-95,131,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-26,-50,-95,-46,172,-59,-95,-95,-47,-54,183,184,-95,-95,190,192,-41,-39,-38,-95,201,-42,]),'READ':([89,104,105,106,107,108,109,110,111,112,113,114,115,132,144,149,153,162,165,168,169,170,176,178,179,182,186,187,189,190,192,198,199,200,201,],[116,116,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-26,-50,116,-46,116,-59,116,116,-47,-54,116,116,116,116,116,116,-41,-39,-38,116,116,-42,]),'DO':([89,104,105,106,107,108,109,110,111,112,113,114,115,132,144,149,153,162,165,168,169,170,176,178,179,182,186,187,189,190,192,198,199,200,201,],[117,117,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-26,-50,117,-46,117,-59,117,117,-47,-54,117,117,117,117,117,117,-41,-39,-38,117,117,-42,]),'WHILE':([89,104,105,106,107,108,109,110,111,112,113,114,115,132,144,149,153,162,165,168,169,170,172,176,178,179,182,186,187,189,190,192,198,199,200,201,],[118,118,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-26,-50,118,-46,118,-59,118,118,-47,180,-54,118,118,118,118,118,118,-41,-39,-38,118,118,-42,]),'IF':([89,104,105,106,107,108,109,110,111,112,113,114,115,132,144,149,153,162,165,168,169,170,176,178,179,182,186,187,189,190,192,198,199,200,201,],[119,119,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-26,-50,119,-46,119,-59,119,119,-47,-54,119,119,119,119,119,119,-41,-39,-38,119,119,-42,]),'RETURN':([89,104,105,106,107,108,109,110,111,112,113,114,115,132,144,149,153,162,165,168,169,170,176,178,179,182,186,187,189,190,192,198,199,200,201,],[122,122,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-26,-50,122,-46,122,-59,122,122,-47,-54,122,122,122,122,122,122,-41,-39,-38,122,122,-42,]),'PRINT':([89,104,105,106,107,108,109,110,111,112,113,114,115,132,144,149,153,162,165,168,169,170,176,178,179,182,186,187,189,190,192,198,199,200,201,],[123,123,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-26,-50,123,-46,123,-59,123,123,-47,-54,123,123,123,123,123,123,-41,-39,-38,123,123,-42,]),'CTES':([140,167,],[156,156,]),'ELSE':([190,],[193,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'global_scope':([4,],[5,]),'empty':([4,5,7,8,10,35,36,37,38,41,43,45,67,68,69,89,91,94,117,118,141,143,149,164,168,169,173,182,186,191,193,199,],[6,9,13,9,17,42,44,44,47,9,17,17,93,93,97,106,47,47,135,135,9,9,106,175,106,106,175,106,106,195,197,106,]),'var_declarations':([5,8,41,141,143,],[7,15,66,158,159,]),'var_declaration':([5,8,41,141,143,],[8,8,8,8,8,]),'functions':([7,],[11,]),'function':([7,11,],[12,19,]),'open_var_declaration':([10,43,45,],[16,67,68,]),'main':([11,],[18,]),'simple_type':([14,16,67,68,126,],[21,27,90,90,90,]),'variables':([27,39,],[32,48,]),'variable':([27,39,40,52,65,69,71,75,82,85,89,98,104,122,129,133,137,138,140,149,150,161,162,167,168,169,178,179,182,185,186,187,189,199,200,],[33,33,57,57,57,57,57,57,57,57,121,57,121,57,57,148,57,57,57,121,57,171,121,57,121,121,121,121,121,57,121,121,121,121,121,]),'main_scope':([35,],[41,]),'function_scope':([36,37,],[43,45,]),'close_var_declaration':([38,91,94,],[46,125,127,]),'expression':([40,65,69,98,122,129,137,138,140,150,167,185,],[50,88,96,130,139,145,151,152,157,163,157,188,]),'t_expression':([40,52,65,69,98,122,129,137,138,140,150,167,185,],[51,74,51,51,51,51,51,51,51,51,51,51,51,]),'g_expression':([40,52,65,69,71,98,122,129,137,138,140,150,167,185,],[53,53,53,53,99,53,53,53,53,53,53,53,53,53,]),'m_expression':([40,52,65,69,71,75,98,122,129,137,138,140,150,167,185,],[54,54,54,54,54,100,54,54,54,54,54,54,54,54,54,]),'term':([40,52,65,69,71,75,82,98,122,129,137,138,140,150,167,185,],[55,55,55,55,55,55,101,55,55,55,55,55,55,55,55,55,]),'factor':([40,52,65,69,71,75,82,85,98,122,129,137,138,140,150,167,185,],[56,56,56,56,56,56,56,102,56,56,56,56,56,56,56,56,56,]),'cte':([40,52,65,69,71,75,82,85,98,122,129,137,138,140,150,167,185,],[58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,]),'expression_parenthesis':([40,52,65,69,71,75,82,85,98,122,129,137,138,140,150,167,185,],[59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,]),'invocation':([40,52,65,69,71,75,82,85,89,98,104,122,129,137,138,140,149,150,162,167,168,169,178,179,182,185,186,187,189,199,200,],[60,60,60,60,60,60,60,60,111,60,111,60,60,60,60,60,111,60,111,60,111,111,111,111,111,60,111,111,111,111,111,]),'boolean_operator':([51,74,],[71,71,]),'comparison_operator':([53,99,],[75,75,]),'addition_operator':([54,100,],[82,82,]),'multiplication_operator':([55,101,],[85,85,]),'parameters':([67,68,],[91,94,]),'parameter':([67,68,126,],[92,92,142,]),'expressions':([69,],[95,]),'statements':([89,149,168,169,182,186,199,],[104,162,178,179,187,189,200,]),'statement':([89,104,149,162,168,169,178,179,182,186,187,189,199,200,],[105,132,105,132,105,105,132,132,105,105,132,132,105,132,]),'read':([89,104,149,162,168,169,178,179,182,186,187,189,199,200,],[107,107,107,107,107,107,107,107,107,107,107,107,107,107,]),'do_while':([89,104,149,162,168,169,178,179,182,186,187,189,199,200,],[108,108,108,108,108,108,108,108,108,108,108,108,108,108,]),'while':([89,104,149,162,168,169,178,179,182,186,187,189,199,200,],[109,109,109,109,109,109,109,109,109,109,109,109,109,109,]),'if_else':([89,104,149,162,168,169,178,179,182,186,187,189,199,200,],[110,110,110,110,110,110,110,110,110,110,110,110,110,110,]),'if':([89,104,149,162,168,169,178,179,182,186,187,189,199,200,],[112,112,112,112,112,112,112,112,112,112,112,112,112,112,]),'assingation':([89,104,149,162,168,169,178,179,182,186,187,189,199,200,],[113,113,113,113,113,113,113,113,113,113,113,113,113,113,]),'return':([89,104,149,162,168,169,178,179,182,186,187,189,199,200,],[114,114,114,114,114,114,114,114,114,114,114,114,114,114,]),'print':([89,104,149,162,168,169,178,179,182,186,187,189,199,200,],[115,115,115,115,115,115,115,115,115,115,115,115,115,115,]),'breadcrumb':([117,118,],[134,136,]),'variable_list':([133,],[147,]),'print_arguments':([140,],[154,]),'print_argument':([140,167,],[155,177,]),'gotof':([164,173,],[174,181,]),'gotot':([191,],[194,]),'goto':([193,],[196,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID SEMICOLON global_scope var_declarations functions main END','program',8,'p_program','grammar.py',22),
  ('global_scope -> empty','global_scope',1,'p_global_scope','grammar.py',29),
  ('functions -> functions function','functions',2,'p_functions','grammar.py',39),
  ('functions -> function','functions',1,'p_functions','grammar.py',40),
  ('functions -> empty','functions',1,'p_functions','grammar.py',41),
  ('function -> FUNCTION simple_type ID LPAREN function_scope open_var_declaration parameters close_var_declaration RPAREN var_declarations LBRACE statements RBRACE','function',13,'p_function','grammar.py',46),
  ('function -> FUNCTION VOID ID LPAREN function_scope open_var_declaration parameters close_var_declaration RPAREN var_declarations LBRACE statements RBRACE','function',13,'p_function','grammar.py',47),
  ('function_scope -> empty','function_scope',1,'p_function_scope','grammar.py',52),
  ('main -> MAIN LPAREN RPAREN main_scope var_declarations LBRACE statements RBRACE','main',8,'p_main','grammar.py',62),
  ('main_scope -> empty','main_scope',1,'p_main_scope','grammar.py',67),
  ('var_declarations -> var_declaration var_declarations','var_declarations',2,'p_var_declarations','grammar.py',78),
  ('var_declarations -> var_declaration','var_declarations',1,'p_var_declarations','grammar.py',79),
  ('var_declarations -> empty','var_declarations',1,'p_var_declarations','grammar.py',80),
  ('var_declaration -> VARIABLE open_var_declaration simple_type variables SEMICOLON close_var_declaration','var_declaration',6,'p_var_declaration','grammar.py',90),
  ('open_var_declaration -> empty','open_var_declaration',1,'p_open_var_declaration','grammar.py',98),
  ('close_var_declaration -> empty','close_var_declaration',1,'p_close_var_declaration','grammar.py',104),
  ('variables -> variable','variables',1,'p_variables','grammar.py',111),
  ('variables -> variable COMMA variables','variables',3,'p_variables','grammar.py',112),
  ('variable -> ID','variable',1,'p_variable','grammar.py',126),
  ('variable -> ID LBRACK expression RBRACK','variable',4,'p_variable','grammar.py',127),
  ('variable -> ID LBRACK expression RBRACK LBRACK expression RBRACK','variable',7,'p_variable','grammar.py',128),
  ('parameters -> parameters COMMA parameter','parameters',3,'p_parameters','grammar.py',140),
  ('parameters -> parameter','parameters',1,'p_parameters','grammar.py',141),
  ('parameters -> empty','parameters',1,'p_parameters','grammar.py',142),
  ('parameter -> simple_type ID','parameter',2,'p_parameter','grammar.py',148),
  ('statements -> statements statement','statements',2,'p_statements','grammar.py',157),
  ('statements -> statement','statements',1,'p_statements','grammar.py',158),
  ('statements -> empty','statements',1,'p_statements','grammar.py',159),
  ('statement -> read','statement',1,'p_statement','grammar.py',164),
  ('statement -> do_while','statement',1,'p_statement','grammar.py',165),
  ('statement -> while','statement',1,'p_statement','grammar.py',166),
  ('statement -> if_else','statement',1,'p_statement','grammar.py',167),
  ('statement -> invocation','statement',1,'p_statement','grammar.py',168),
  ('statement -> if','statement',1,'p_statement','grammar.py',169),
  ('statement -> assingation','statement',1,'p_statement','grammar.py',170),
  ('statement -> return','statement',1,'p_statement','grammar.py',171),
  ('statement -> print','statement',1,'p_statement','grammar.py',172),
  ('do_while -> DO breadcrumb LBRACE statements RBRACE WHILE LPAREN expression RPAREN gotot SEMICOLON','do_while',11,'p_do_while','grammar.py',177),
  ('while -> WHILE breadcrumb LPAREN expression RPAREN gotof LBRACE statements RBRACE','while',9,'p_while','grammar.py',182),
  ('breadcrumb -> empty','breadcrumb',1,'p_breadcrumb','grammar.py',189),
  ('if -> IF LPAREN expression RPAREN gotof LBRACE statements RBRACE','if',8,'p_if','grammar.py',195),
  ('if_else -> IF LPAREN expression RPAREN gotof LBRACE statements RBRACE ELSE goto LBRACE statements RBRACE','if_else',13,'p_if_else','grammar.py',202),
  ('gotot -> empty','gotot',1,'p_gotot','grammar.py',208),
  ('goto -> empty','goto',1,'p_goto','grammar.py',214),
  ('gotof -> empty','gotof',1,'p_gotof','grammar.py',220),
  ('return -> RETURN expression SEMICOLON','return',3,'p_return','grammar.py',227),
  ('read -> READ LPAREN variable_list RPAREN SEMICOLON','read',5,'p_read','grammar.py',232),
  ('variable_list -> variable','variable_list',1,'p_variable_list','grammar.py',241),
  ('variable_list -> variable_list COMMA variable','variable_list',3,'p_variable_list','grammar.py',242),
  ('invocation -> ID LPAREN expressions RPAREN SEMICOLON','invocation',5,'p_invocation','grammar.py',252),
  ('expressions -> expressions COMMA expression','expressions',3,'p_expressions','grammar.py',257),
  ('expressions -> expression','expressions',1,'p_expressions','grammar.py',258),
  ('expressions -> empty','expressions',1,'p_expressions','grammar.py',259),
  ('print -> PRINT LPAREN print_arguments RPAREN SEMICOLON','print',5,'p_print','grammar.py',264),
  ('print_arguments -> print_argument','print_arguments',1,'p_print_arguments','grammar.py',269),
  ('print_arguments -> print_arguments COMMA print_argument','print_arguments',3,'p_print_arguments','grammar.py',270),
  ('print_argument -> CTES','print_argument',1,'p_print_argument','grammar.py',282),
  ('print_argument -> expression','print_argument',1,'p_print_argument','grammar.py',283),
  ('assingation -> variable ASSIGN expression SEMICOLON','assingation',4,'p_assingation','grammar.py',297),
  ('expression -> t_expression','expression',1,'p_expression','grammar.py',310),
  ('expression -> NOT t_expression','expression',2,'p_expression','grammar.py',311),
  ('t_expression -> g_expression','t_expression',1,'p_t_expression','grammar.py',321),
  ('t_expression -> t_expression boolean_operator g_expression','t_expression',3,'p_t_expression','grammar.py',322),
  ('g_expression -> m_expression','g_expression',1,'p_g_expression','grammar.py',333),
  ('g_expression -> g_expression comparison_operator m_expression','g_expression',3,'p_g_expression','grammar.py',334),
  ('m_expression -> term','m_expression',1,'p_m_expression','grammar.py',344),
  ('m_expression -> m_expression addition_operator term','m_expression',3,'p_m_expression','grammar.py',345),
  ('term -> factor','term',1,'p_term','grammar.py',356),
  ('term -> term multiplication_operator factor','term',3,'p_term','grammar.py',357),
  ('factor -> variable','factor',1,'p_factor','grammar.py',369),
  ('factor -> cte','factor',1,'p_factor','grammar.py',370),
  ('factor -> expression_parenthesis','factor',1,'p_factor','grammar.py',371),
  ('factor -> invocation','factor',1,'p_factor','grammar.py',372),
  ('expression_parenthesis -> LPAREN expression RPAREN','expression_parenthesis',3,'p_expression_parenthesis','grammar.py',385),
  ('comparison_operator -> LESS','comparison_operator',1,'p_comparison_operator','grammar.py',392),
  ('comparison_operator -> GREATER','comparison_operator',1,'p_comparison_operator','grammar.py',393),
  ('comparison_operator -> EQUALS','comparison_operator',1,'p_comparison_operator','grammar.py',394),
  ('comparison_operator -> NOTEQUAL','comparison_operator',1,'p_comparison_operator','grammar.py',395),
  ('comparison_operator -> GREATERTHAN','comparison_operator',1,'p_comparison_operator','grammar.py',396),
  ('comparison_operator -> LESSTHAN','comparison_operator',1,'p_comparison_operator','grammar.py',397),
  ('addition_operator -> PLUS','addition_operator',1,'p_addition_operator','grammar.py',403),
  ('addition_operator -> MINUS','addition_operator',1,'p_addition_operator','grammar.py',404),
  ('boolean_operator -> AND','boolean_operator',1,'p_boolean_operator','grammar.py',411),
  ('boolean_operator -> OR','boolean_operator',1,'p_boolean_operator','grammar.py',412),
  ('multiplication_operator -> TIMES','multiplication_operator',1,'p_multiplication_operator','grammar.py',419),
  ('multiplication_operator -> DIVIDE','multiplication_operator',1,'p_multiplication_operator','grammar.py',420),
  ('simple_type -> INT','simple_type',1,'p_simple_type','grammar.py',427),
  ('simple_type -> FLOAT','simple_type',1,'p_simple_type','grammar.py',428),
  ('simple_type -> CHAR','simple_type',1,'p_simple_type','grammar.py',429),
  ('simple_type -> BOOLEAN','simple_type',1,'p_simple_type','grammar.py',430),
  ('cte -> CTEI','cte',1,'p_cte','grammar.py',437),
  ('cte -> CTEF','cte',1,'p_cte','grammar.py',438),
  ('cte -> CTEC','cte',1,'p_cte','grammar.py',439),
  ('cte -> CTEB','cte',1,'p_cte','grammar.py',440),
  ('empty -> <empty>','empty',0,'p_empty','grammar.py',449),
]
