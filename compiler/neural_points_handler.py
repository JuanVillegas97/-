from constants.constants import *
from constants.virtual_constants import virtual_operators
from compiler.interfaces.quadruple import Quadruple
from compiler.functions_directory import FunctionsDirectory
from compiler.intermidiate_representation import IntermediateRepresentation
from compiler.interfaces.encoder import Encoder

import json
import os

class NeuralPointsHandler:
     __instance = None
     
     @staticmethod
     def get_instance():
          if NeuralPointsHandler.__instance is None:
               NeuralPointsHandler()
          return NeuralPointsHandler.__instance
     
     def __init__(self):
          if NeuralPointsHandler.__instance is not None:
               raise Exception("This class is a singleton. Use get_instance() method to get the instance.")
          else:
               NeuralPointsHandler.__instance = self
               self.__directory = FunctionsDirectory.get_instance()
               self.__inter_rep = IntermediateRepresentation.get_instance()
               
     def invocation_1(self,invocation_id):
          # Verify that the procedure exists into the DirFunc.
          global global_invocation_id
          if self.__directory.is_function_name(invocation_id):
               global_invocation_id = invocation_id
          
     def invocation_2(self):
          # Generate action ERA size (Activation Record expansion –NEW—size).
          global global_invocation_id
          new_quadruple = Quadruple(ERA,"","",global_invocation_id)
          self.__inter_rep.push(QUADRUPLES,new_quadruple)
          
          # Start the parameter counter (k) in 0.
          self.__inter_rep.set_parameter_counter(0)
          
     def invocation_3(self):
          # Add a pointer to the first parameter type in the ParameterTable.
          global global_invocation_id
          
          global parameter
          k = self.__inter_rep.get_paramater_counter()
          parameter = self.__directory.get_function_dictionary()[global_invocation_id][PARAMETERS][k]
          
          
          # Argument = PilaO.Pop() ArgumentType= PTypes.Pop().
          argument = self.__inter_rep.pop(OPERANDS)
          argumentType = self.__inter_rep.pop(TYPES)
          
          # Verify ArgumentType against current Parameter (#k) in ParameterTable.
          if parameter == argumentType:
               pass
          else:
               raise Exception("Invocation does not has the same signature")
          
          #Generate action PARAMETER, Argument, Argument#k
          arg_num = self.__inter_rep.generate_parameter()
          #* HANDELS THE CONVERTION TO ADDRESSS
          virtual_address = self.__inter_rep.get_virtual_address()
          if virtual_address:
               argument = self.__inter_rep.convert_operand_to_address(argument)
          #*
          new_quadruple = Quadruple(PARAM,argument,"",arg_num)
          self.__inter_rep.push(QUADRUPLES,new_quadruple)
     
     def invocation_4(self):
          # K = K + 1, move to next parameter.
          self.__inter_rep.move_to_next_parameter()
          
     def invocation_5(self):
          # Verify that the last parameter points to null.
          global parameter 
          parameter = None
          
     def invocation_6(self):
          # Generate action GOSUB, procedure-name, , initial-address.
          global global_invocation_id
          self.__inter_rep.generate_gosub(global_invocation_id)
          
          # If invocation has a type generate quadruple for invocation and push new temporal
          invocation_type = self.__directory.get_invocation_type(global_invocation_id)
          if invocation_type is not "VOID":
               new_temporal = self.__inter_rep.generate_avail()
               assign = ASSIGN 
               
               #* HANDELS THE CONVERTION TO ADDRESSS
               virtual_address = self.__inter_rep.get_virtual_address()
               if virtual_address:
                    if assign in virtual_operators:
                         assign = virtual_operators[assign]
                    new_temporal = self.__inter_rep.convert_temporal_to_address(invocation_type)
                    global_invocation_id = self.__inter_rep.convert_operand_to_address(global_invocation_id)
               #*
               self.__inter_rep.push(OPERANDS,new_temporal)
               self.__inter_rep.push(TYPES,invocation_type)
               new_quadruple = Quadruple(assign,global_invocation_id,"",new_temporal)
               self.__inter_rep.push(QUADRUPLES,new_quadruple)
          
     def function_1(self,function_name,function_type,scope):
          # Insert Function name into the DirFunc table (and its type, if any), verify semantics.
          self.__directory.set_current(function_name,function_type,scope)
          self.__directory.add_function(len(self.__inter_rep.get_stack(QUADRUPLES))+1)
     
     def convert_to_json(self):
          self.__directory.kill_variable_table()
          directory = self.__directory.get_function_dictionary()
          constant_table = self.__directory.get_constant_table()
          quadruples = self.__inter_rep.get_stack(QUADRUPLES)
          
          # Create a dictionary to store both objects
          data = {
               "directory": directory,
               "constant_table":constant_table,
               "quadruples": quadruples,
          }
          
          # Serialize the dictionary to JSON
          
          json_data = json.dumps(data, indent=4, cls=Encoder)
          
          # Specify the file path
          file_path = os.path.join("vm_files", "programs", "data.json")
          
          # Write the JSON data to the file
          with open(file_path, 'w') as json_file:
               json_file.write(json_data)