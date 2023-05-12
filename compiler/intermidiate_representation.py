from compiler.sematnic_cube import SemanticCube
from compiler.quadruple import Quadruple
OPERATORS  ="operators"
TYPES      ="types"
OPERANDS   ="operands"
QUADRUPLES ="quadruples"
JUMPS      ="jumps"


class intermediateRepresentation:
    def __init__(self):
        self.__semantic_cube = SemanticCube()
        self.__stacks = {
            "operators": [],#POper
            "types": [],    #PTYpes
            "operands": [], #PilaO
            "quadruples": [],
            "jumps": []
        }
        self.__temporal_counter = 0
        self.__i=0
    
        
    def push(self, stack_name, value):
        if stack_name in self.__stacks:
            if stack_name == "operators":
                if value not in ["+", "-", "*", "/", "<", ">"]:
                    raise ValueError("Invalid operator")
            elif stack_name == "types":
                if value not in ["BOOLEAN", "CHAR", "STRING", "FLOAT", "INT"]:
                    raise ValueError("Invalid type")
            self.__stacks[stack_name].append(value)
        else:
            raise ValueError(f"Invalid stack name: {stack_name}")

    def pop(self, stack_name):
        if stack_name in self.__stacks:
            return self.__stacks[stack_name].pop()
        else:
            raise ValueError(f"Invalid stack name: {stack_name}")
        
    def print_stacks(self):
        print('-' * 50)
        print("Operators stack:", self.__stacks["operators"])
        print("Types stack:", self.__stacks["types"])
        print("Operands stack:", self.__stacks["operands"])
        print("Quadruples stack:")
        for i, quad in enumerate(self.__stacks["quadruples"]):
            print(f"  {i}: {quad.get_operator()} {quad.get_left_operand()} {quad.get_right_operand()} {quad.get_avail()}")
        # print("Jumps stack:", self.__stacks["jumps"])
        print('-' * 50)
        print('\n')
    
    def __generate_avail(self):
        self.__temporal_counter += 1
        return f't{self.__temporal_counter}'
    
    def reset_temporal_counter(self):
        self.__temporal_counter = 0
        
    def create_quadruple(self):
        self.__i += 1
        print(self.__i)
        operator = self.__stacks[OPERATORS].pop()
        right_operand = self.__stacks[OPERANDS].pop()
        left_operand = self.__stacks[OPERANDS].pop()
        right_type = self.__stacks[TYPES].pop()
        left_type = self.__stacks[TYPES].pop()

        result_type = self.__semantic_cube.get_type(left_type,right_type,operator)

        if result_type != "ERROR":
           if operator == "=":
                result_type = left_operand
                new_quadruple = Quadruple(operator, None, right_operand, result_type)
           else:
               result = self.__generate_avail()
               new_quadruple = Quadruple(operator,left_operand,right_operand,result)
               self.__stacks[QUADRUPLES].append(new_quadruple)
               self.__stacks[OPERANDS].append(result)
               self.__stacks[TYPES].append(result_type)
        else:
            raise TypeError(f"Type mismatch with: {left_type}{operator}{right_type}")

            



