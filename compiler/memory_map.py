import json
class MemoryMap:
    __instance = None

    @staticmethod
    def get_instance(directory, constant_table):
        """Static method to retrieve the singleton instance."""
        if MemoryMap.__instance is None:
            MemoryMap.__instance = MemoryMap(directory, constant_table)
        return MemoryMap.__instance
    
    def __init__(self, directory, constant_table):
        if MemoryMap.__instance is not None:
            raise Exception("This class is a singleton. Use get_instance() method to get the instance.")
        else:
            MemoryMap.__instance = self
            self.__directory = directory
            self.__constant_table = constant_table
        
        self.__print_directory()
        
    def __print_directory(self):
        formatted_directory = json.dumps(self.__directory, indent=4)
        print(formatted_directory)