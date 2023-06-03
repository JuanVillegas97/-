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
                    "resources" : None 
                }
            self.__set_resources()

    def __malloc(self,type,address):
        if self.__memory["resources"] > 0 :
            self.__memory["resources"] -= 1
            self.__memory[type] = {address : None}
        
    def get_value(self, type, address):
        if type in self.__memory and address in self.__memory[type]:
            value = self.__memory[type][address]
            return value
        else:
            self.__malloc(type,address)
        
    def set_value_at_address(self, type, address, value):
        if type in self.__memory:
            self.__memory[type][address] = value
        
    def __set_resources(self):
        total_resources = 0
        for program in self.__directory.values():
            resources = program.get("resources")
            for value in resources.values():
                total_resources += value
        self.__memory["resources"] = total_resources
    
    def get_memory(self):
        return self.__memory
        
    def print_memory(self):
        print("Memory:")
        for key, value in self.__memory.items():
            if key != "resources":
                print(key + ":")
                for address, data in value.items():
                    print(f"  {address}: {data}")
        print("Current memory:", self.__memory["resources"],"\n")
