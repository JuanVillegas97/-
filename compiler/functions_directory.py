import copy
from lexer.tokens import reserved
from compiler.variable import variable
from constants.constants import *

class functionsDirectory:   
    def __init__(self):
        self.__constants_table = {}
        self.__function_dictionary = {}
        self.__current_function_name = None
        self.__current_function_scope = None
        self.__current_function_type = None
        self.__is_variable_declaration = False
        self.__program_name = None
    
    def add_resource(self, ids, type, resource_type):
        if self.__current_function_name is None:
            raise Exception("No function defined to add variable '{}'".format(id))
        
        if type in reserved:
            type = reserved[type]
        for id in ids:
            self.__function_dictionary[self.__current_function_name][RESOURCES][resource_type][type] +=1
    
    def is_same_signature(self, signature):
        func_name = signature.pop()
        if func_name in self.__function_dictionary:
            parameters = copy.deepcopy(self.__function_dictionary[func_name]["parameters"])
            while signature and signature[-1] == parameters[-1]:
                signature.pop()
                parameters.pop()
        if len(signature) != 0 and len(parameters) != 0:
            raise Exception("Invocation does not has the same signature")
            
    def is_function_name(self,function_name):
        if function_name in self.__function_dictionary:
            return True
        else:
            raise Exception("Function being called does not exist")
        
    def set_program_name(self, name):
        self.__program_name = name
    
    def __check_value_type(self, value):
            if isinstance(value, bool):
                return BOOLEAN
            elif isinstance(value, int):
                return INT
            elif isinstance(value, float):
                return FLOAT
            else:
                return ERROR
        
    def add_constant(self, constant):
        type = self.__check_value_type(constant)
        if type == ERROR:
            raise Exception("Constant is ERRROR type")
        if constant not in self.__constants_table:
            new_variable = variable(constant,type)
            self.__constants_table[constant] = new_variable
            
        
    def set_is_variable_declaration_true(self):
        self.__is_variable_declaration = True
        
    def set_is_variable_declaration_false(self):
        self.__is_variable_declaration = False
    
    def get_is_variable_declaration(self):
        return self.__is_variable_declaration
        
    def get_function_dictionary(self):
        return self.__function_dictionary
    
    def get_current_function_name(self):
        return self.__current_function_name
    
    def add_parameters(self, type):
        if type in reserved:
            type = reserved[type]
        self.__function_dictionary[self.__current_function_name]["parameters"].append(type)

    def set_current(self, name, type, scope):
        self.__current_function_name = name
        self.__current_function_type = type
        self.__current_function_scope= scope
    
    def add_function(self, starting_address=None):
        if self.__current_function_name in self.__function_dictionary:
            raise Exception("Function '{}' multiple declaration (functions can only have unique ID)".format(self.__current_function_name))

        if self.__current_function_type in reserved:
            self.__current_function_type = reserved[self.__current_function_type]
        self.__function_dictionary[self.__current_function_name] = {
            "type": self.__current_function_type,
            "scope": self.__current_function_scope,
            "starting_address": starting_address,
            RESOURCES:{
                "parameters":{INT:0,CHAR:0,FLOAT:0,BOOLEAN:0},
                "variables":{INT:0,CHAR:0,FLOAT:0,BOOLEAN:0},
                "temporal":{INT:0,CHAR:0,FLOAT:0,BOOLEAN:0}
            },
            "parameters": [],
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
        
        #? First check for the variable in local scope
        local_variable_table = self.__function_dictionary[self.__current_function_name]["variable_table"]
        
        #? Secondly, check the variable in the constant table
        constant_table = self.__constants_table
        
        #? Lastly, check variables in the global scope (program variable table)
        program_variable_table = self.__function_dictionary[self.__program_name]["variable_table"]
        
        for id in ids:
            if id not in local_variable_table and \
            id not in constant_table and \
            id not in program_variable_table:
                raise Exception("Variable '{}' was not declared".format(id))

    def get_variable(self, function_name, variable_id):
        if function_name not in self.__function_dictionary:
            raise Exception("Function '{}' was not declared".format(function_name))
        
        local_variable_table = self.__function_dictionary[function_name]["variable_table"]
        
        if variable_id in local_variable_table:
            return local_variable_table[variable_id]
        
        constant_table = self.__constants_table
        
        if variable_id in constant_table:
            return constant_table[variable_id]
        
        program_variable_table = self.__function_dictionary[self.__program_name]["variable_table"]
        
        if variable_id in program_variable_table:
            return program_variable_table[variable_id]

        raise Exception("Variable '{}' not found".format(variable_id))

    
    def print_function_dictionary(self):
        print("{:15} {:10} {:17} {:8} {:10} {:15}".format("Function Name", "Type","Starting Address","Scope", "Signature", "Variables"))

        for function_name, function_details in self.__function_dictionary.items():
            function_type = function_details["type"]
            function_scope = function_details["scope"]
            variable_table = function_details["variable_table"]
            parameters_list = function_details["parameters"]
            starting_address = str(function_details["starting_address"])
            
            parameters_types = ", ".join(str(types) for types in parameters_list)
            variable_names = ", ".join(str(name) for name in variable_table.keys())

            print("{:15} {:10} {:17} {:8} {:10} {:15}".format(function_name, function_type, starting_address, function_scope, parameters_types, variable_names))
        
        print("\nConstants Table:")
        print("{:10} {}".format("Type","Constant"))
        
        for constant, variable in self.__constants_table.items():
            constant_type = variable.type
            print("{:10} {}".format(constant_type, constant))


    def print_current(self):
            print(self.__current_function_type," ",self.__current_function_name," ",self.__current_function_scope)

    


