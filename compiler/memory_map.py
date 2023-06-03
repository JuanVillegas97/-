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
            self.__memmory ={
                    "int" : {}, 
                    "float" : {}, 
                    "char" : {} , 
                    "boolean" : {},
                    "resources" : None
                }
            self.__malloc()
            
    def __malloc(self):
        total_resources = 0
        for program in self.__directory.values():
            resources = program.get("resources")
            for value in resources.values():
                total_resources += value
        self.__memmory["resources"] = total_resources
    
    def get_memmory(self):
        return self.__memmory
        
            
