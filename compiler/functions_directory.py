from lexer.tokens import reserved
from compiler.variable import variable

class functionsDirectory:   
    def __init__(self):
        self.__function_dictionary = {}
        self.__current_function_name = None
        self.__current_function_scope = None
        self.__current_function_type = None
    
    def get_function_dictionary(self):
        return self.__function_dictionary
    
    def get_current_function_name(self):
        return self.__current_function_name

    def get_variable(self, function_name, variable_id):
        if function_name not in self.__function_dictionary:
            raise Exception("Function '{}' was not declared".format(function_name))
        elif variable_id not in self.__function_dictionary[function_name]["variable_table"]:
            raise Exception("Variable '{}' was not declared '{}'".format(variable_id, function_name))
        else:
            return self.__function_dictionary[function_name]["variable_table"][variable_id]
    
    def set_current(self, name, type, scope):
        self.__current_function_name = name
        self.__current_function_type = type
        self.__current_function_scope= scope
    
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

    def add_variable(self, ids,type):
        if self.__current_function_name is None:
            raise Exception("No function defined to add variable '{}'".format(id))
        
        if type in reserved:
            type = reserved[type]

        for id in ids:
            if id in self.__function_dictionary[self.__current_function_name]["variable_table"]:
                raise Exception("Variable '{}' multiple declaration".format(id))
            
            new_variable = variable(id,type)
            self.__function_dictionary[self.__current_function_name]["variable_table"][id] = new_variable
        
    def search_variable(self, ids):
        if self.__current_function_name is None:
            raise Exception("No function defined to add variable '{}'".format(id))
        for id in ids:
                if id not in self.__function_dictionary[self.__current_function_name]["variable_table"]:
                    raise Exception("Variable '{}' was not declared".format(id))
    
    def print_function_dictionary(self):
            print("{:15} {:10} {:20} {}".format("Function Name", "Type", "Scope", "Variables"))
            for name, function in self.__function_dictionary.items():
                variable_table = ", ".join("{}:{}".format(var_name, var_type) for var_name, var_type in function["variable_table"].items())
                print("{:15} {:10} {:20} {}".format(name, function["type"], function["scope"], variable_table))

    def print_current(self):
            print(self.__current_function_type," ",self.__current_function_name," ",self.__current_function_scope)


    # other methods...

