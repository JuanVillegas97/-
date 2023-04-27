import ply.lex as lex

# Tuple of reserved names.
reserved = {
    'プログラム':'PROGRAM',
    '整数': 'INT', 
    '浮動小数点数':'FLOAT', 
    '文字列': 'STRING', 
    '文字':  'CHAR',
    'もし' : 'IF',
    'ならば' : 'THEN',
    '違えば' : 'ELSE',
    '繰り返す' : 'WHILE', 
    'プリント':'PRINT',
    'メイン' : 'MAIN',
    'ブーリアン' : 'BOOLEAN',
    'トゥルー' : 'TRUE',
    'フォルス' : 'FALSE',
    'プリント' : 'PRINT',
    'リターン' : 'RETURN',
    '変数': 'VARIABLE',
    '関数': 'FUNCTION',
    'エンド' : 'END',
    '入力する' : 'READ',
}

# List of token names.
tokens = [
    'ASSIGN', #Done
    'PLUS',   #Done
    'MINUS',  #Done
    'TIMES',  #Done
    'DIVIDE', #Done
    'EQUALS', #Done
    'NOTEQUAL',#Done
    'LESS',   #Done 
    'GREATER',#Done 
    'LPAREN', #Done
    'RPAREN', #Done
    'LBRACE', #Done
    'RBRACE', #Done
    'SEMICOLON', #Done
    'COLON',#Done
    'COMMA',#Done
    'ID', #Done
    'CTEI',#Done
    'CTEF',#Done
    'CTES',#Done
    'CTEC',#Done
    'CTEB',#Done
    'RBRACK',#Done
    'LBRACK',#Done
    'COMMENT',#Done
    'AND',#Done
    'OR',#Done
]+ list(reserved.values())


# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_ASSIGN  = r'='
t_EQUALS  = r'=='
t_NOTEQUAL= r'!='
t_LESS    = r'<'
t_GREATER = r'>'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACE   = r'\{'
t_RBRACE  = r'\}'
t_LBRACK = r'\['
t_RBRACK  = r'\]'
t_SEMICOLON = r';'
t_COLON     = r':'
t_COMMA     = r','
t_AND     = r'&&'
t_OR = r'\|\|'

def t_ID(t):
    r'[\u30A0-\u30FF\u3040-\u309F\u4E00-\u9FFF]+|[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')   
    return t

def t_CTEF(t):
    r'([0-9]+[.])[0-9]+'
    t.value = float(t.value)
    return t

def t_CTEI(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_CTEB(t):
    r'\s*(true|false)\s*'
    t.type = 'CTEB'
    t.value = t.value.strip()# strip whitespace and convert to lowercase
    return t


def t_CTES(t):
    r'\".*?\"'
    t.value = t.value[1:-1]  # Remove quotes from value
    return t

def t_CTEC(t):
    r'\'[^\']\''
    t.value = t.value[1:-1]  # Remove quotes from value
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_COMMENT(t):
    r'\/\/.*'
    pass # ignore comments

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '{}' at: {}".format(t.value[0], t.lexer.lineno))
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# # Test it out
# data = '''
# 3.5
# 2
# "uwu"
# 'u'
# '''

# # Give the lexer some input
# lexer.input(data)

# # Tokenize
# while True:
#     tok = lexer.token()
#     if not tok: 
#         break      # No more input
#     print(tok)