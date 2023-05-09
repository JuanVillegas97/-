from lexer.tokens import reserved

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
        
        if self.__current_function_type in reserved:
            self.__current_function_type = reserved[self.__current_function_type]
        self.__function_dictionary[self.__current_function_name] = {
            "type": self.__current_function_type,
            "scope": self.__current_function_scope,
            "variable_table": {}
        }

    def search_variable(self, ids):
        if self.__current_function_name is None:
            raise Exception("No function defined to add variable '{}'".format(id))
        for id in ids:
                if id not in self.__function_dictionary[self.__current_function_name]["variable_table"]:
                    raise Exception("Variable '{}' was not declared".format(id))

    def add_variable(self, ids,type):
        if self.__current_function_name is None:
            raise Exception("No function defined to add variable '{}'".format(id))
        
        if type in reserved:
            type = reserved[type]

        for id in ids:
            if id in self.__function_dictionary[self.__current_function_name]["variable_table"]:
                raise Exception("Variable '{}' multiple declaration".format(id))
            self.__function_dictionary[self.__current_function_name]["variable_table"][id] = type
    
    def print_function_dictionary(self):
            print("{:15} {:10} {:20} {}".format("Function Name", "Type", "Scope", "Variables"))
            for name, function in self.__function_dictionary.items():
                variable_table = ", ".join("{}:{}".format(var_name, var_type) for var_name, var_type in function["variable_table"].items())
                print("{:15} {:10} {:20} {}".format(name, function["type"], function["scope"], variable_table))



    # other methods...

