
from compiler.memory_map import MemoryMap
import json
#INT     1000-1999
#FLOAT   2000-2999
#CHAR    3000-3999
#BOOLEAN 4000-4999
class VirtualMachine:
    def __init__(self):
        directory, constant_table, quadruples = self.__deserialize_json_from_file()
        self.__memory = MemoryMap.get_instance(directory).get_memmory()
        self.__constant_table = constant_table
        self.__quadruples = quadruples
        
        self.__execute()        
        
        
    def __execute(self):
        instruction_pointer = 0
        print(self.__constant_table)
        # while instruction_pointer < len(quadruples):
        #     quadruple = quadruples[instruction_pointer]
        #     operator = quadruple["_Quadruple__operator"]
        #     left_operand = quadruple["_Quadruple__left_operand"]
        #     right_operand = quadruple["_Quadruple__right_operand"]
        #     result = quadruple["_Quadruple__avail"]

        #     if operator == 0:
        #         # Perform addition
        #         value1 = self._get_value(left_operand)
        #         value2 = self._get_value(right_operand)
        #         result_value = value1 + value2
        #         self._set_value(result, result_value)

        #     elif operator == 2:
        #         # Perform subtraction
        #         value1 = self._get_value(left_operand)
        #         value2 = self._get_value(right_operand)
        #         result_value = value1 - value2
        #         self._set_value(result, result_value)

        #     # Add more operators and their corresponding actions here

        #     elif operator == 32:
        #         # Exit the virtual machine
        #         break

        #     instruction_pointer += 1

    def _get_value(self, operand):
        if isinstance(operand, int):
            # Operand is a constant
            return operand
        else:
            # Operand is a variable, fetch its value from memory
            return self.memory.get(operand, 0)

    def _set_value(self, variable, value):
        # Store the value in memory
        self.memory[variable] = value

    
    def __determine_type(value):
        if 1000 <= value <= 1999:
            return "INT"
        elif 2000 <= value <= 2999:
            return "FLOAT"
        elif 3000 <= value <= 3999:
            return "CHAR"
        elif 4000 <= value <= 4999:
            return "BOOLEAN"
        else:
            return "UNKNOWN"
        
    def __deserialize_json_from_file(file_path):
        file_path = "ovejota.json"
        with open(file_path, 'r') as file:
            json_data = json.load(file)
        directory = json_data['directory']
        constant_table = json_data['constant_table']
        quadruples = json_data['quadruples']
        return directory,constant_table,quadruples
    

    
