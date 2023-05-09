from compiler.sematnic_cube import SemanticCube

class intermediateRepresentation:
    class Quadruples:
        def __init__(self, operator, left_operand, right_operand, avail):
            self.__operator  = operator
            self.__left_operand = left_operand
            self.__right_operand = right_operand
            self.__avail = avail
        
        def updateresult(self, newr):
            self.res = newr

    def __init__(self):
        self.__semantic_cube = SemanticCube()
        self.__stacks = {
            "operators": [],#PilaO
            "types": [],    #PTYpes
            "operands": [], #POper
            "quadruples": [],
            "jumps": []
        }

        def push(self, stack_name, value):
            if stack_name in self.__stacks:
                self.__stacks[stack_name].append(value)
            else:
                raise ValueError(f"Invalid stack name: {stack_name}")

        def pop(self, stack_name):
            if stack_name in self.__stacks:
                return self.__stacks[stack_name].pop()
            else:
                raise ValueError(f"Invalid stack name: {stack_name}")
            



