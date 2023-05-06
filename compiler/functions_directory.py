
class functionsDirectory:
    def __init__(self):
            self.function_dictionary = {}
            self.current_function_name = None
            self.current_variable_type = None #To be able to handle multiple declarations with the same type


    def add_function(self, function_name, type):
        if function_name in self.function_dictionary:
            raise Exception("Function '{}' multiple declaration".format(function_name))
        
        self.current_function_name = function_name
        self.function_dictionary[function_name] = {
            "type": type,
            "variable_table": None
        }

    def has_variable_table(self, function_name):
        if function_name not in self.function_dictionary:
            raise Exception("Function '{}' not found in directory".format(function_name))
    
        self.function_dictionary[function_name]["variable_table"] = {}
    
    def add_variable(self,id,type):
        if id in self.function_dictionary:
            raise Exception("Function '{}' not found in directory".format(self.current_function_name))
        
        
