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
        
    def __malloc(self,type,address):
        if self.resources > 0 :
            self.resources -= 1
            self.segment[type][address] = None
            print("Memory in the address", address, "of type", type, "has been allocated") if self.is_debugging else None
        
        
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
        

        