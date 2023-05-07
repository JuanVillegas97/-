class functionsDirectory:   
    def __init__(self):
        self.__function_dictionary = {}
        self.__current_function_name = None
        self.__current_function_scope = None
        self.__current_function_type = None
    
    def get_function_dictionary(self):
        return self.__function_dictionary
    
    def set_current(self, name, type, scope):
        self.__current_function_name = name
        self.__current_function_type = type
        self.__current_function_scope=scope
    
    def print_current(self):
        print(self.__current_function_type," ",self.__current_function_name," ",self.__current_function_scope)

    def add_function(self):
        if self.__current_function_name in self.__function_dictionary:
            raise Exception("Function '{}' multiple declaration".format(self.__current_function_name))
        
        self.__function_dictionary[self.__current_function_name] = {
            "type": self.__current_function_type,
            "scope": self.__current_function_scope,
            "variable_table": {}
        }

    def add_variable(self, ids,type):
        if self.__current_function_name is None:
            raise Exception("No function defined to add variable '{}'".format(id))
        
        for id in ids:
            if id in self.__function_dictionary[self.__current_function_name]["variable_table"]:
                raise Exception("Variable '{}' multiple declaration".format(id))
            self.__function_dictionary[self.__current_function_name]["variable_table"][id] = type
    
    def print_function_dictionary(self):
        for function_name, function_details in self.__function_dictionary.items():
            print("Function Name: ", function_name)
            print("Function Type: ", function_details["type"])
            print("Function Scope: ", function_details["scope"])
            print("Variable Table: ", function_details["variable_table"])


    # other methods...

