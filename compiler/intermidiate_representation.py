from constants.constants import *

from compiler.sematnic_cube import SemanticCube
from compiler.interfaces.quadruple import Quadruple
from constants.virtual_constants import virtual_operators
from compiler.functions_directory import FunctionsDirectory
directory = FunctionsDirectory.get_instance()

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
            self.__k = 0
            self.__is_virtual_address = False
    
    def get_virtual_address(self):
        return self.__is_virtual_address
    
    def set_virtual_address (self, value):
        self.__is_virtual_address = value
        
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
    
    def get_stack(self, name):
        return self.__stacks[name]
    
    def get_stack(self,stack_name):
        return self.__stacks[stack_name]

    def generate_avail(self):
        self.__temporal_counter += 1
        return f't{self.__temporal_counter}'
    
    def reset_temporal_counter(self):
        self.__temporal_counter = 0
        
    def get_temporal_counter(self):
        return self.__temporal_counter
        
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
    

    def convert_operator_to_address(self, operator):
        if operator in virtual_operators:
            operator = virtual_operators[operator]
        return operator
    
    def convert_temporal_to_address(self, type):
        result = directory.get_next_virtual_address_var_and_temp(type)
        return result
    
    def convert_operand_to_address(self, operand):
        constant_table = directory.get_constant_table()
        variable_table = directory.get_variable_table()
        global_var_table = directory.get_global_variable_table()

        if operand in constant_table:
            operand = constant_table[operand].virtual_address
        elif operand in variable_table:
            operand = variable_table[operand].virtual_address
        elif operand in global_var_table:
            operand = global_var_table[operand].virtual_address
            
            
        return operand

    def create_quadruple(self):
        operator = self.__stacks[OPERATORS].pop()
        if operator == '=':
            last_operand = self.__stacks[OPERANDS].pop()
            assignation_operand = self.__stacks[OPERANDS].pop()
            variable = directory.get_variable(directory.get_current_function_name(),last_operand)
            last_type = self.__stacks[TYPES].pop()
            result_type = self.__semantic_cube.get_type(last_type,variable.type,operator)
            
            if result_type == "ERROR":
                raise TypeError(f"Type mismatch with: {left_type}{operator}{right_type}")
            
            #* HANDELS THE CONVERTION TO ADDRESSS
            virtual_address = self.get_virtual_address()
            if virtual_address:
                operator = self.convert_operator_to_address(operator)
                last_operand = self.convert_operand_to_address(last_operand)
                assignation_operand  = self.convert_operand_to_address(assignation_operand)
                
            #*
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
                #* HANDELS THE CONVERTION TO ADDRESSS
                virtual_address = self.get_virtual_address()
                if virtual_address:
                    operator = self.convert_operator_to_address(operator)
                    result = self.convert_temporal_to_address(result_type)
                    left_operand = self.convert_operand_to_address(left_operand)
                    right_operand = self.convert_operand_to_address(right_operand)
                #*
                new_quadruple = Quadruple(operator,left_operand,right_operand,result)
                self.__stacks[QUADRUPLES].append(new_quadruple)
                self.__stacks[OPERANDS].append(result)
                self.__stacks[TYPES].append(result_type)
            else:
                raise TypeError(f"Type mismatch with: {left_type}{operator}{right_type}")
    
    def gotof_if(self):
        conditional_element = self.__stacks[OPERANDS].pop()
        type_conditional = self.__stacks[TYPES].pop()
        if type_conditional != BOOLEAN:
            raise TypeError(f"Type mismatch")
        #* HANDELS THE CONVERTION TO ADDRESSS
        if self.__is_virtual_address:
            conditional_element = self.convert_operand_to_address(conditional_element)
        #*
            
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
    


