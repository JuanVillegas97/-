import ply.lex as lex
from lexer import tokens

class MyLexer:
    def __init__(self):
        self.lexer = lex.lex(module=tokens)

    def tokenize(self, source_code):
        self.lexer.input(source_code)
        while True:
            token = self.lexer.token()
            if not token:
                break
            print(token)

    # Lexer rules
    # ...

    # Other lexer methods
    # ...


