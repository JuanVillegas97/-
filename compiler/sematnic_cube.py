from constants.constants import *
# Still missing the NOT
class SemanticCube:
    def __init__(self):
        self.__cube = {
            (INT, INT):        [INT   , INT  , INT  , FLOAT, ERROR, BOOLEAN,  INT    ],
            (INT, FLOAT):      [FLOAT , FLOAT, FLOAT, FLOAT, ERROR, BOOLEAN,  FLOAT  ],
            (INT, CHAR):       [INT   , INT  , INT  , INT  , ERROR, BOOLEAN,  INT    ],
            (INT, BOOLEAN):    [ERROR , ERROR, ERROR, ERROR, ERROR, ERROR  ,  ERROR  ],
            (INT, STRING):     [STRING, ERROR, ERROR, ERROR, ERROR, ERROR  ,  ERROR  ],
            (INT, VECTOR):     [VECTOR, ERROR, ERROR, ERROR, ERROR, ERROR  ,  ERROR  ],
            (FLOAT, FLOAT):    [FLOAT , FLOAT, FLOAT, FLOAT, ERROR, BOOLEAN,  FLOAT  ],
            (FLOAT, CHAR):     [STRING, ERROR, ERROR, ERROR, ERROR, ERROR  ,  ERROR  ],
            (FLOAT, BOOLEAN):  [ERROR , ERROR, ERROR, ERROR, ERROR, ERROR  ,  ERROR  ],
            (FLOAT, STRING):   [STRING, ERROR, ERROR, ERROR, ERROR, ERROR  ,  ERROR  ],
            (FLOAT, VECTOR):   [VECTOR, ERROR, ERROR, ERROR, ERROR, ERROR  ,  ERROR  ],
            (CHAR, CHAR):      [INT   , INT  , INT  , INT  , ERROR, BOOLEAN,   CHAR  ],
            (CHAR, BOOLEAN):   [ERROR , ERROR, ERROR, ERROR, ERROR, ERROR  ,  ERROR  ],
            (CHAR, STRING):    [STRING, ERROR, ERROR, ERROR, ERROR, ERROR  ,  ERROR  ],
            (BOOLEAN, BOOLEAN):[ERROR , ERROR, ERROR, ERROR, ERROR, BOOLEAN,  BOOLEAN],
            (STRING, STRING):  [STRING, ERROR, ERROR, ERROR, ERROR, ERROR  ,  ERROR  ],
            (VECTOR, VECTOR):  [VECTOR, ERROR, ERROR, ERROR, ERROR, ERROR  ,  ERROR  ],
        }
        self.__operator_index= {
            PLUS:0,MINUS:1,TIMES:2,DIVIDE: 3,
            AND: 4, OR: 4, NOT: 4,
            GREATER: 5, LESS: 5, GREATERTHAN: 5, LESSTHAN: 5, NOTEQUAL: 5, EQUALS:5,
            ASSIGN: 6,
        }
    
    def get_type(self, left_op, right_op, operator):
        result_type = self.__operator_index.get(operator, None)
        print(result_type)
        if result_type is not None:
            types = self.__cube.get((left_op, right_op), None)
            if not types:
                types = self.__cube.get((right_op, left_op), None)
            if types:
                return types[result_type]
        return ERROR  # Invalid operation or operand types
