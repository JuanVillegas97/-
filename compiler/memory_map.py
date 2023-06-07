class MemorySegment:
    def __init__(self, resources):
        self.segment = {
            "INT" : {}, 
            "FLOAT" : {}, 
            "CHAR" : {} , 
            "BOOLEAN" : {},
            "STRING" :{},
        }
        self.resources = resources
        self.is_debugging = False

    def print_memory(self):
        print("=== MEMORY ===")
        print("STRING:")
        for key, value in self.segment["STRING"].items():
            print(f"{key}: {value}")
        print("INT:")
        for key, value in self.segment["INT"].items():
            print(f"{key}: {value}")
        print("FLOAT:")
        for key, value in self.segment["FLOAT"].items():
            print(f"{key}: {value}")
        print("CHAR:")
        for key, value in self.segment["CHAR"].items():
            print(f"{key}: {value}")
        print("BOOLEAN:")
        for key, value in self.segment["BOOLEAN"].items():
            print(f"{key}: {value}")
        print("Resources:")
        print(self.resources)
        
    def __malloc(self,type,address):
        if self.resources > 0 :
            self.resources -= 1
            self.segment[type][address] = None
            print("Memory in the address", address, "of type", type, "has been allocated") if self.is_debugging else None
        else:
            address = str(address)
            raise Exception("Not enough memory with allocation for address" + address)
        
    def get_value(self, type, address):
        if type in self.segment and address in self.segment[type]:
            value = self.segment[type][address]
            return value
        else:
            self.__malloc(type,address)
            return None
        
    def set_value_at_address(self, type, address, value):
        if type in self.segment:
            self.segment[type][address] = value
        
    def get_memory(self):
        return self.segment
        
    
    def find_address_by_name(self,name):
        if name in self.__directory:
            return self.__directory[name].get("id")
        else:
            return None
    