from compiler.sematnic_cube import SemanticCube
from lexer.lexer import MyLexer
from parser.parser import MyParser
from parser.grammar import directory

def _main():
    quadruples  = "tests/quadruples.txt"
    directory   = "tests/parser_test.txt"
    lexer = MyLexer()
    # with open(file_name, "r",encoding="utf-8") as file:
    #     tokens = file.read()
    # lexer.tokenize(tokens)

    parser = MyParser()
    with open(quadruples, "r",encoding="utf-8") as file:
        code = file.read()

    parser.parse(code)

    # directory.print_function_dictionary()
if __name__ == '__main__':
    _main()
