from compiler.sematnic_cube import SemanticCube
from lexer.lexer import MyLexer
from parser.parser import MyParser
from parser.grammar import directory

def _main():
    lexer = MyLexer()
    parser = MyParser()

    with open("tests/lexer_test.txt", "r",encoding="utf-8") as file:
        tokens = file.read()

    with open("tests/parser_test.txt", "r",encoding="utf-8") as file:
        code = file.read()

    # Tokenize the source code
    parser.parse(code)

    directory.print_function_dictionary()
if __name__ == '__main__':
    _main()
