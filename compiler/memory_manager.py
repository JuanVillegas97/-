#VARIABLES AND TEMPORALS
#INT     1000-1999
#FLOAT   2000-2999
#CHAR    2000-2999
#BOOLEAN 3000-3999

#CTES
#INT     4000-4499
#FLOAT   4500-4999
#CHAR    5000-5499
#BOOLEAN 5000-5001
from compiler.interfaces.pointer import Pointer
from constants.constants import *
class MemoryManager:
    def __init__(self):
        self.__data_segment = {
            VARIABLES_TEMPORALS:{
                INT:{},
                FLOAT:{},
                CHAR:{},
                BOOLEAN:{},
            },
            CTES:{
                INT:{},
                FLOAT:{},
                CHAR:{},
                BOOLEAN:{},
            }
        }

