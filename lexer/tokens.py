# Tuple of reserved names.
reserved = {
    'プログラム':'PROGRAM',
    'から' : 'FROM',
    '整数': 'INT', 
    '浮動小数点数':'FLOAT', 
    '文字列': 'STRING', 
    '文字':  'CHAR',
    '繰り返し': 'FOR',
    '実行': 'DO',
    'ブール' : 'BOOLEAN',
    'もし' : 'IF',
    'ならば' : 'THEN',
    '違えば' : 'ELSE',
    'ワイル' : 'WHILE', 
    'プリント':'PRINT',
    'メイン' : 'MAIN',
    'プリント' : 'PRINT',
    'リターン' : 'RETURN',
    '変数': 'VARIABLE',
    '関数': 'FUNCTION',
    'エンド' : 'END',
    '入力する' : 'READ',
    '無効': 'VOID',
    '鍵生成': 'GENKEY'
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
    'GREATERTHAN',
    'LESSTHAN',
    'NOT'
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
t_LESSTHAN    = r'<='
t_GREATERTHAN = r'>='
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
t_NOT= r'!'
t_AND     = r'&&'
t_OR = r'\|\|'



def t_CTEB(t):
    r'[真偽]'
    if t.value == '真':
        t.value = True
    elif t.value == '偽':
        t.value = False
    else:
        raise ValueError("Invalid value encountered")
    return t

def t_CTEF(t):
    r'([0-9]+[.])[0-9]+'
    t.value = float(t.value)
    return t

def t_CTEI(t):
    r'\d+'
    t.value = int(t.value)
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

def t_ID(t):
    r'[\u30A0-\u30FF\u3040-\u309F\u4E00-\u9FFF]+|[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')   
    return t

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '{}' at: {}".format(t.value[0], t.lexer.lineno))
    t.lexer.skip(1)
