from pygments.style import Style
from pygments.token import Token
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexer import RegexLexer

# Define your reserved words and token types
reserved = {
    'プログラム': 'PROGRAM',
    '整数': 'INT',
    '浮動小数点数': 'FLOAT',
    # Add other reserved words...
}

# Define your custom token types
tokens = [
    'ASSIGN',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'EQUALS',
    'NOTEQUAL',
    'LESS',
    'GREATER',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'SEMICOLON',
    'COLON',
    'COMMA',
    'ID',
    'CTEI',
    'CTEF',
    'CTES',
    'CTEC',
    'CTEB',
    'RBRACK',
    'LBRACK',
    'COMMENT',
    'AND',
    'OR',
] + list(reserved.values())

# Define your custom style class
class MyCustomStyle(Style):
    tokens = {
        Token.Keyword: '#FF0000',  # Red color for keywords
        Token.Name: '#0000FF',  # Blue color for identifiers
        Token.Operator: '#00FF00',  # Green color for operators
        # Define styles for other custom token types as per your requirement
    }

# Define your custom lexer class
class MyCustomLexer(RegexLexer):
    tokens = {
        'root': [
            (r'プログラム|整数|浮動小数点数', Token.Keyword),
            # Add other token patterns...
            (r'\w+', Token.Name),
            # ...
        ]
    }

def get_token_type(word):
    return reserved.get(word, Token.Name)

def highlight_code(code):
    language = 'mylang'  # Specify the name of your custom lexer

    lexer = MyCustomLexer(stripall=True, ensurenl=False, func=get_token_type)
    formatter = TerminalFormatter(style=MyCustomStyle)
    highlighted_code = highlight(code, lexer, formatter)

    return highlighted_code

# Example usage
code = '''
プログラム
整数 x = 10;
もし x > 5 ならば
    プリント("大きい数です");
違えば
    プリント("小さい数です");
エンド
'''

highlighted_code = highlight_code(code)
print(highlighted_code)
