
from compiler.memory_map import MemoryMap
import json
#INT     1000-1999
#FLOAT   2000-2999
#CHAR    3000-3999
#BOOLEAN 4000-4999
class VirtualMachine:
    def __init__(self):
        directory, constant_table, quadruples = self.__deserialize_json_from_file()
        self.__memory = MemoryMap.get_instance(directory)
        self.__constant_table = constant_table
        self.__quadruples = quadruples
        self.__insctruction_pointers = []
        self.__context = []
        self.__execute()        
        
        
    def __execute(self):
        instruction_pointer = 0
        quadruples = self.__quadruples
        
        print("\n")
        print("My program/memory in execution")
        print(20*"-")
        while instruction_pointer < len(quadruples):
            quadruple = quadruples[instruction_pointer]
            operator = quadruple["_Quadruple__operator"]
            left_operand = quadruple["_Quadruple__left_operand"]
            right_operand = quadruple["_Quadruple__right_operand"]
            result = quadruple["_Quadruple__avail"]
            
            if self.__memory.is_debuging:
                print(10*"-")
                self.__memory.print_memory()
                print("My memory is about ot perform -> ",quadruple.values())
                print(10*"-")
            
            if operator == 0: #! Perform ADDITION
                left_operand =  self.__get_value(left_operand) 
                right_operand =  self.__get_value(right_operand)
                memory_allocation = self.__get_value(result)
                address = result                                    # Saving the addres for later
                result = left_operand + right_operand               # Performin addition
                type = self.__get_variable_type(result)
                self.__memory.set_value_at_address(type,address,result)
            elif operator == 1:  #! Perform SUBSTRACTION
                left_operand =  self.__get_value(left_operand) 
                right_operand =  self.__get_value(right_operand)
                memory_allocation = self.__get_value(result)
                address = result                                    # Saving the addres for later
                result = left_operand - right_operand               # Performin addition
                type = self.__get_variable_type(result)
                self.__memory.set_value_at_address(type,address,result)
            elif operator == 2:  #! Perform MULTIPLICATION
                left_operand =  self.__get_value(left_operand) 
                right_operand =  self.__get_value(right_operand)
                memory_allocation = self.__get_value(result)
                address = result                                    # Saving the addres for later
                result = left_operand * right_operand               # Performin addition
                type = self.__get_variable_type(result)
                self.__memory.set_value_at_address(type,address,result)
            elif operator == 3:  #! Perform DIVISION
                left_operand =  self.__get_value(left_operand) 
                right_operand =  self.__get_value(right_operand)
                memory_allocation = self.__get_value(result)
                address = result                                    # Saving the addres for later
                result = left_operand / right_operand               # Performin addition
                type = self.__get_variable_type(result)
                self.__memory.set_value_at_address(type,address,result)
            elif operator == 9:  #! Perform LESS
                left_operand =  self.__get_value(left_operand) 
                right_operand =  self.__get_value(right_operand)
                memory_allocation = self.__get_value(result)
                address = result                                    # Saving the addres for later
                result = left_operand < right_operand               # Performin addition
                type = self.__get_variable_type(result)
                self.__memory.set_value_at_address(type,address,result)
            elif operator == 10:  #! Perform LESS THAN
                left_operand =  self.__get_value(left_operand) 
                right_operand =  self.__get_value(right_operand)
                memory_allocation = self.__get_value(result)
                address = result                                    # Saving the addres for later
                result = left_operand <= right_operand               # Performin addition
                type = self.__get_variable_type(result)
                self.__memory.set_value_at_address(type,address,result)
            elif operator == 11:  #! Perform GREATER THAN
                left_operand =  self.__get_value(left_operand) 
                right_operand =  self.__get_value(right_operand)
                memory_allocation = self.__get_value(result)
                address = result                                    # Saving the addres for later
                result = left_operand >= right_operand               # Performin addition
                type = self.__get_variable_type(result)
                self.__memory.set_value_at_address(type,address,result)
            elif operator == 12:  #! Perform GREATER
                left_operand =  self.__get_value(left_operand) 
                right_operand =  self.__get_value(right_operand)
                memory_allocation = self.__get_value(result)
                address = result                                    # Saving the addres for later
                result = left_operand > right_operand               # Performin addition
                type = self.__get_variable_type(result)
                self.__memory.set_value_at_address(type,address,result)
            elif operator == 13: #!Perform ASSIGNATION
                left_side =  self.__get_value(left_operand) # Get the value 
                memory_allocation = self.__get_value(result)    
                address = result                            # Address where is going to bet set
                type = self.__get_type(address)
                self.__memory.set_value_at_address(type,address,left_side)
            elif operator == 33: #!Perform PRINT
                addres_to_print = result 
                memory_allocation = self.__get_value(result)
                value_to_print = self.__get_value(addres_to_print)
                print(value_to_print)
            elif operator == 21: #!Perform GOTF
                address_to_evaluate = self.__get_value(right_operand) 
                conditional_element = address_to_evaluate
                if not conditional_element:
                    instruction_pointer = result - 2
            elif operator == 22: #!Perform GOTV
                address_to_evaluate = self.__get_value(right_operand) 
                conditional_element = address_to_evaluate
                if conditional_element:
                    instruction_pointer = result - 2
            elif operator == 23: #!Perform GOTO
                instruction_pointer = result - 2
            elif operator == 24: #!Perform GOTOMAIN
                self.__memory.load_resources("my_program")
                self.__memory.load_resources("MAIN")
                self.__memory.set_current("MAIN")
                instruction_pointer = result - 2
            elif operator == 29: #!Perform ERA
                id = result
                name = self.__memory.find_key_by_id(id)
                
                #*I need to know the previous context so...
                self.__context.append(name)
                
                self.__memory.set_current(name)
                self.__memory.load_resources(name)
                #! LEFT TO DO SAVE MEMORY POINTER
            elif operator == 30: #!Perform PARAMETERS
                addres_paramater = result
                address_argument = left_operand
                
                argument = self.__get_value(address_argument)
                memory_allocation = self.__get_value(result)
                
                type = self.__get_type(addres_paramater)
                self.__memory.set_value_at_address(type,addres_paramater,argument)
            elif operator == 31: #!Perform GOSUB
                self.__insctruction_pointers.append(instruction_pointer)
                id = result
                name = self.__memory.find_key_by_id(id)
                starting_address = self.__memory.get_func_starting_address(name)
                
                instruction_pointer = starting_address - 2
            elif operator == 25: #!Perform END FUNC
                stacked_instruction_pointer = self.__insctruction_pointers.pop()
                instruction_pointer = stacked_instruction_pointer
            elif operator == 28: #!Perform Return
                pass
            elif operator == 34: #!Perform READ
                addres = result
                memory_allocation = self.__get_value(result)
                type = self.__get_type(addres)
                my_input = input("Write the input -> ")
                self.__memory.set_value_at_address(type,addres,my_input)
                pass
            elif operator == 32: #!perfrom END
                break
            
            instruction_pointer += 1
        print(20*"-")
        print("\n")

    
    def __get_value(self, address):
        if address > 4999:
            for constant_id, constant_data in self.__constant_table.items():
                virtual_address = constant_data['virtual_address']
                if virtual_address == address:
                    return constant_data['id']
                
        if 1000 <= address < 5000:
            if 1000 <= address <= 1999:
                type =  "INT"
            elif 2000 <= address <= 2999:
                type =  "FLOAT"
            elif 3000 <= address <= 3999:
                type =  "CHAR"
            elif 4000 <= address <= 4999:
                type =  "BOOLEAN"
            value = self.__memory.get_value(type,address)
            return value
        return "ERROR"
    

        
    def __deserialize_json_from_file(file_path):
        file_path = "ovejota.json"
        with open(file_path, 'r') as file:
            json_data = json.load(file)
        directory = json_data['directory']
        constant_table = json_data['constant_table']
        quadruples = json_data['quadruples']
        return directory,constant_table,quadruples
    
    def __get_type(self, address):
        if 1000 <= address < 5000:
            if 1000 <= address <= 1999:
                return  "INT"
            elif 2000 <= address <= 2999:
                return  "FLOAT"
            elif 3000 <= address <= 3999:
                return "CHAR"
            elif 4000 <= address <= 4999:
                return  "BOOLEAN"
        return "ERROR"
    
    def __get_variable_type(self, variable):
        variable_type = type(variable).__name__
        if variable_type == 'bool':
            return 'BOOLEAN'
        elif variable_type == 'str' and len(variable) == 1:
            return 'CHAR'
        elif variable_type == 'float':
            return 'FLOAT'
        elif variable_type == 'int':
            return 'INT'
        else:
            return variable_type.upper()
    
