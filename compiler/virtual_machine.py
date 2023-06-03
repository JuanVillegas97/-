from compiler.proccessor import Processor
from compiler.memory_map import MemoryMap

import json
class VirtualMachine:
    def __init__(self):
        directory, constant_table, quadruples = self.__deserialize_json_from_file()
        self.__processor = Processor.get_instance(quadruples)
        self.__memory = MemoryMap.get_instance(directory,constant_table)
    
    def __deserialize_json_from_file(file_path):
        file_path = "ovejota.json"
        
        with open(file_path, 'r') as file:
            json_data = json.load(file)
        directory = json_data['directory']
        constant_table = json_data['constant_table']
        quadruples = json_data['quadruples']
        return directory,constant_table,quadruples