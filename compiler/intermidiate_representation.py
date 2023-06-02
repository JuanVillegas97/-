from compiler.sematnic_cube import SemanticCube
from compiler.interfaces.quadruple import Quadruple
from constants.constants import *

class IntermediateRepresentation:
    __instance = None

    @staticmethod
    def get_instance():
        if IntermediateRepresentation.__instance is None:
            IntermediateRepresentation()
        return IntermediateRepresentation.__instance

    def __init__(self):
        if IntermediateRepresentation.__instance is not None:
            raise Exception("This class is a singleton. Use get_instance() method to get the instance.")
        else:
            IntermediateRepresentation.__instance = self
            self.__semantic_cube = SemanticCube()
            self.__stacks = {
                "operators": [],
                "types": [],
                "operands": [],
                "quadruples": [],
                "jumps": []
            }
            self.__temporal_counter = 0
            self.__temporal_counter_b = 0
            self.__k = 0

            self.__is_conditional = False
            self.__is_invocation = False
            self.__invocation_signature = []
            
    def generate_parameter(self):
        return f'par{self.__k+1}'
    
    def move_to_next_parameter(self):
        self.__k += 1
    
    def reset_paramter_counter(self):
        self.__k = 0
        
    def set_parameter_counter(self, value):
        self.__k = value
    
    def get_paramater_counter(self):
        return self.__k
    
    def set_is_condtional_false(self):
        self.__is_condtional = False
        
    def set_is_condtional_true(self):
        self.__is_condtional = True
        
    def generate_temporal_counter_b(self):
        self.__temporal_counter_b += 1
        return f'tb{self.__temporal_counter_b}'
    
    def reset_temporal_counter_b(self):
        self.__temporal_counter_b = 0
        
    def __set_temporal_info(self, name, type):
        self.__temporal_info = (name, type)
    
    def get_temporal_info(self):
        return self.__temporal_info
    
    def get_stack(self, name):
        return self.__stacks[name]
    

    

        
    def get_is_invocation(self):
        return self.__is_invocation
    
    def set_is_invocation_false(self):
        self.__is_invocation = False
        
    def set_is_invocation_true(self):
        self.__is_invocation = True
        
    def get_stack(self,stack_name):
        return self.__stacks[stack_name]
    
    def push(self, stack_name, value):
        if stack_name in self.__stacks:
            if stack_name == OPERATORS:
                if value not in ["+", "-", "*", "/", "<", ">","=","!","!="]:
                    raise ValueError("Invalid operator")
            elif stack_name == TYPES:
                if value not in [BOOLEAN, CHAR, STRING, FLOAT, INT]:
                    raise ValueError("Invalid type")
            self.__stacks[stack_name].append(value)
        else:
            raise ValueError(f"Invalid stack name: {stack_name}")

    def top(self, stack_name):
        if stack_name in self.__stacks:
            return self.__stacks[stack_name][-1]
        else:
            raise ValueError(f"Invalid stack name: {stack_name}")
        
    def pop(self, stack_name):
        if stack_name in self.__stacks:
            return self.__stacks[stack_name].pop()
        else:
            raise ValueError(f"Invalid stack name: {stack_name}")
        
    def print_stacks(self):
        print('-' * 50)
        print("Operators stack:", self.__stacks[OPERATORS])
        print("Types stack:", self.__stacks[TYPES])
        print("Operands stack:", self.__stacks[OPERANDS])
        print("Jumps stack:", self.__stacks[JUMPS])
        print("Quadruples stack:")
        for i, quad in enumerate(self.__stacks[QUADRUPLES]):
            print(f"  {i+1}: {quad.get_operator()} {quad.get_left_operand()} {quad.get_right_operand()} {quad.get_avail()}")
        print('-' * 50)
        print('\n')
    
    def generate_avail(self):
        self.__temporal_counter += 1
        return f't{self.__temporal_counter}'
    
    def reset_temporal_counter(self):
        self.__temporal_counter = 0
    
        
    def create_quadruple(self):
        operator = self.__stacks[OPERATORS].pop()
        if operator == '=':
            last_operand = self.__stacks[OPERANDS].pop()
            assignation_operand = self.__stacks[OPERANDS].pop()
            last_type = self.__stacks[TYPES].pop()#!Still do not know what do with this one, maybe I gotta update it in the var table (TYPE)
            new_quadruple = Quadruple(operator, assignation_operand, "", last_operand)
            self.__stacks[QUADRUPLES].append(new_quadruple)
        else:
            try:
                right_operand = self.__stacks[OPERANDS].pop()
                left_operand = self.__stacks[OPERANDS].pop()
                right_type = self.__stacks[TYPES].pop()
                left_type = self.__stacks[TYPES].pop()
            except IndexError:
                raise IndexError("Error: Pop from empty stack")
            result_type = self.__semantic_cube.get_type(left_type,right_type,operator)
            if result_type != "ERROR":
                result = self.generate_avail() 
                new_quadruple = Quadruple(operator,left_operand,right_operand,result)
                self.__stacks[QUADRUPLES].append(new_quadruple)
                self.__stacks[OPERANDS].append(result)
                self.__stacks[TYPES].append(result_type)

                self.__set_temporal_info(result,result_type) #?HANDLES RESOURCES FOR TEMPORALS
                # if self.__is_invocation: #?Handles generation of parameters AND respect to the same signature
                #     self.__invocation_signature.append(self.__stacks[TYPES].pop()) #!Don't know what to do with them
                    

            else:
                raise TypeError(f"Type mismatch with: {left_type}{operator}{right_type}")
    
    def gotof_if(self):
        conditional_element = self.__stacks[OPERANDS].pop()
        type_conditional = self.__stacks[TYPES].pop()
        if type_conditional != BOOLEAN:
            raise TypeError(f"Type mismatch")
        new_quadruple = Quadruple(GOTOF,"",conditional_element,'_')
        self.__stacks[JUMPS].append(len(self.__stacks[QUADRUPLES])+1)
        self.__stacks[QUADRUPLES].append(new_quadruple)
    
    def fill_while(self):
        false = self.__stacks[JUMPS].pop()-1
        return_ = self.__stacks[JUMPS].pop()
        new_quadruple = Quadruple(GOTO,"","",return_)
        self.__stacks[QUADRUPLES].append(new_quadruple)
        self.__stacks[QUADRUPLES][false].set_avail(len(self.__stacks[QUADRUPLES])+1)
        
    def fill(self):
        end = self.__stacks[JUMPS].pop()-1
        self.__stacks[QUADRUPLES][end].set_avail(len(self.__stacks[QUADRUPLES])+1)
    
        
    def push_breadcrumb(self):
        self.__stacks[JUMPS].append(len(self.__stacks[QUADRUPLES])+1)
        
    def gotof_if_else(self):
        end = self.__stacks[JUMPS].pop()-1
        self.__stacks[QUADRUPLES][end].set_avail(len(self.__stacks[QUADRUPLES])+2)
        new_quadruple = Quadruple(GOTO,"","",'_')
        self.__stacks[JUMPS].append(len(self.__stacks[QUADRUPLES])+1)
        self.__stacks[QUADRUPLES].append(new_quadruple)
    
    def gotot_while(self):
        conditional_element = self.__stacks[OPERANDS].pop()
        type_conditional = self.__stacks[TYPES].pop()
        if type_conditional != BOOLEAN:
            raise TypeError(f"Type mismatch")
        end = self.__stacks[JUMPS].pop()
        new_quadruple = Quadruple(GOTOT,"",conditional_element,end)
        self.__stacks[QUADRUPLES].append(new_quadruple)
        
    def generate_gosub(self,func_id):
        new_quadruple = Quadruple(GOSUB,"","",func_id)
        self.__stacks[QUADRUPLES].append(new_quadruple)
    
        

            



