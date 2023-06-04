from compiler.sematnic_cube import SemanticCube
from lexer.lexer import MyLexer
from parser.parser import MyParser
from parser.grammar import directory
from parser.grammar import inter_rep
from compiler.neural_points_handler import NeuralPointsHandler
from compiler.virtual_machine import VirtualMachine

neural = NeuralPointsHandler.get_instance()
def _main():
    file  = "tests/while_test.txt"
    lexer = MyLexer()
    # with open(file, "r",encoding="utf-8") as file:
    #     tokens = file.read()
    # lexer.tokenize(tokens)

    parser = MyParser()
    with open(file, "r",encoding="utf-8") as file:
        code = file.read()

    parser.parse(code)
    
    inter_rep.print_stacks()
    directory.print_function_dictionary()
    
    if inter_rep.get_virtual_address():
        neural.convert_to_json()
        vm = VirtualMachine()
    
if __name__ == '__main__':
    _main()
