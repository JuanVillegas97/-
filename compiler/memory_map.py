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
            self.__directory = directory
            self.__memory = {
                    "INT" : {}, 
                    "FLOAT" : {}, 
                    "CHAR" : {} , 
                    "BOOLEAN" : {},
                    "STRING" :{},
                    "resources" : {},
                    "current" : ""
                }
            self.is_debuging = True


    def print_memory(self):
        print("=== MEMORY ===")
        print("STRING:")
        for key, value in self.__memory["STRING"].items():
            print(f"{key}: {value}")
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
    
    def get_current(self):
        return self.__memory["current"]
        
    def load_resources(self,name):
        self.__memory["resources"][name] = sum(self.__directory[name]["resources"].values())
        
    def __malloc(self,type,address):
        current = self.__memory["current"]
        if self.__memory["resources"][current] > 0 :
            self.__memory["resources"][current] -= 1
            self.__memory[type][address] = None
            if self.is_debuging:
                print("Memory in the address", address, "of type", type, "has been allocated") if self.is_debuging else None
                print("From the context ",current, " current memory ",self.__memory["resources"][current])
        elif self.__memory["resources"]["my_program"] > 0:
            self.__memory["resources"]["my_program"] -= 1
            self.__memory[type][address] = None
            if self.is_debuging:
                print("Memory in the address", address, "of type", type, "has been allocated ") 
                print("From the context my_program, current memory ",self.__memory["resources"]["my_program"])
        else:
            address = str(address)
            raise Exception("Not enough memory with allocation for address" + address)
        
    def get_value(self, type, address):
        if type in self.__memory and address in self.__memory[type]:
            value = self.__memory[type][address]
            return value
        else:
            self.__malloc(type,address)
            return None
        
    def set_value_at_address(self, type, address, value):
        if type in self.__memory:
            self.__memory[type][address] = value
        
    def get_memory(self):
        return self.__memory
        
    def find_key_by_id(self, id):
        for key, value in self.__directory.items():
            if value["id"] == id:
                return key
        return None
    
    def find_address_by_name(self,name):
        if name in self.__directory:
            return self.__directory[name].get("id")
        else:
            return None
    
    def get_func_starting_address(self,name):
        return self.__directory[name]["starting_address"]