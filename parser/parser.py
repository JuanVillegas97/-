import ply.yacc as yacc
from parser import grammar

class MyParser:
    def __init__(self):
        self.parser = yacc.yacc(module=grammar,debug=True)

    def parse(self, source_code):
        result = self.parser.parse(source_code)
        print(result)



