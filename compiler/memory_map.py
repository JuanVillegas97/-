class MemoryMap:
    __instance = None

    @staticmethod
    def get_instance(directory):
        """Static method to retrieve the singleton instance."""
        if MemoryMap.__instance is None:
            MemoryMap.__instance = MemoryMap(directory)
        return MemoryMap.__instance
    
    def __init__(self, directory):
        if MemoryMap.__instance is not None:
            raise Exception("This class is a singleton. Use get_instance() method to get the instance.")
        else:
            MemoryMap.__instance = self
            self.__directory = {'my_program': {'type': 'PROGRAM', 'scope': 'GLOBAL', 'starting_address': None, 'resources': {'parameters': 0, 'variables': 0, 'temporals': 0}, 'parameters': [], 'id': 0}, 'MAIN': {'type': 'MAIN', 'scope': 'LOCAL', 'starting_address': None, 'resources': {'parameters': 0, 'variables': 1, 'temporals': 0}, 'parameters': [], 'id': 0}}
            self.__memory = {
                    "INT" : {}, 
                    "FLOAT" : {}, 
                    "CHAR" : {} , 
                    "BOOLEAN" : {},
                    "resources" : {},
                    "current" : ""
                }
            self.__set_resources()

    def print_memory(self):
        print("=== MEMORY ===")
        print("INT:")
        for key, value in self.__memory["INT"].items():
            print(f"{key}: {value}")
        print("FLOAT:")
        for key, value in self.__memory["FLOAT"].items():
            print(f"{key}: {value}")
        print("CHAR:")
        for key, value in self.__memory["CHAR"].items():
            print(f"{key}: {value}")
        print("BOOLEAN:")
        for key, value in self.__memory["BOOLEAN"].items():
            print(f"{key}: {value}")
        print("Resources:")
        for key, value in self.__memory["resources"].items():
            print(f"{key}: {value}")
        print("Current:",f"{self.__memory['current']}")

    def set_current(self,current):
        self.__memory["current"] = current
        
    def load_resources(self,name):
        self.__memory["resources"][name] = sum(self.__directory[name]["resources"].values())
        
    def __malloc(self,type,address):
        current = self.__memory["current"]
        if self.__memory["resources"][current] > 0 :
            self.__memory["resources"][current] -= 1
            self.__memory[type] = {address : None}
        else:
            print("Not enough memory")
        
    def get_value(self, type, address):
        if type in self.__memory and address in self.__memory[type]:
            value = self.__memory[type][address]
            print("hiii",value,address)
            
            # if self.__memory["resources"] > 0 :
            #     self.__memory["resources"] -= 1
            return value
        else:
            self.__malloc(type,address)
            return None
        
    def set_value_at_address(self, type, address, value):
        if type in self.__memory:
            self.__memory[type][address] = value
        
    def __set_resources(self):
        pass
        # total_resources = 0
        # for program in self.__directory.values():
        #     resources = program.get("resources")
        #     for value in resources.values():
        #         total_resources += value
        # self.__memory["resources"] = total_resources
    
    def get_memory(self):
        return self.__memory
        
    # def print_memory(self):
    #     print("Memory:")
    #     for key, value in self.__memory.items():
    #         if key != "resources":
    #             print(key + ":")
    #             for address, data in value.items():
    #                 print(f"  {address}: {data}")
    #     print("Current memory:", self.__memory["resources"],"\n")
        
    def get_directory(self):
        return self.__directory
    
    def __find_key_by_id(self, dictionary, target_id):
        for key, value in dictionary.items():
            if value.get('id') == target_id:
                return key
        return None  # ID not found
    
    