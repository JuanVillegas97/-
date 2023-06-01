from constants.constants import *
from compiler.interfaces.quadruple import Quadruple
from compiler.functions_directory import FunctionsDirectory
from compiler.intermidiate_representation import IntermediateRepresentation

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
          if self.__directory.is_function_name(invocation_id):
               pass
          
     def invocation_2(self,invocation_id):
          # Generate action ERA size (Activation Record expansion –NEW—size).
          new_quadruple = Quadruple(ERA,"","",invocation_id)
          self.__inter_rep.push(QUADRUPLES,new_quadruple)
          
          # Start the parameter counter (k) in 1.
          self.__inter_rep.set_parameter_counter(1)
          
          # Add a pointer to the first parameter type in the ParameterTable.
          global parameter
          parameter = self.__directory.get_function_dictionary()[invocation_id][PARAMETERS][0]
          
     def invocation_3(self):
          # Argument = PilaO.Pop() ArgumentType= PTypes.Pop().
          argument = self.__inter_rep.pop(OPERANDS)
          argumentType = self.__inter_rep.pop(TYPES)
          
          # Verify ArgumentType against current Parameter (#k) in ParameterTable.
          global parameter
          if parameter == argumentType:
               pass
          else:
               raise Exception("Invocation does not has the same signature")
          
          #Generate action PARAMETER, Argument, Argument#k
          arg_num = self.__inter_rep.generate_parameter()
          new_quadruple = Quadruple(PARAM,argument,"",arg_num)
          self.__inter_rep.push(QUADRUPLES,new_quadruple)
     
     def invocation_4(self):
          # K = K + 1, move to next parameter.
          self.__inter_rep.move_to_next_parameter()
          
     def invocation_5(self):
          # Verify that the last parameter points to null.
          global parameter 
          parameter = None
          
     def invocation_6(self,invocation_id):
          # Generate action GOSUB, procedure-name, , initial-address.
          self.__inter_rep.reset_paramter_counter()
          self.__inter_rep.generate_gosub(invocation_id)
          
     def function_1(self,function_name,function_type,scope):
          # Insert Function name into the DirFunc table (and its type, if any), verify semantics.
          self.__directory.set_current(function_name,function_type,scope)
          self.__directory.add_function(len(self.__inter_rep.get_stack(QUADRUPLES))+1)
          