# Types
INT = 'INT'
FLOAT = 'FLOAT'
CHAR = 'CHAR'
BOOLEAN = 'BOOLEAN'
ERROR = 'ERROR'
STRING = 'STRING'
VECTOR = 'VECTOR'
# Operators
PLUS = '+'
MINUS = '-'
TIMES = '*'
DIVIDE = '/'
# Boolean
AND = 'AND'
OR = 'OR'
NOT = 'NOT'
# Comparison
EQUALS = '=='
NOTEQUAL = '!='
LESS = '<'
LESSTHAN = '<='
GREATERTHAN = '>='
GREATER = '>'
# Assignment
ASSIGN = '='

# Still missing the NOT
class SemanticCube:
    def __init__(self):
        self.cube = {
            (INT, INT): [INT, INT, INT, FLOAT, ERROR, ERROR, BOOLEAN, BOOLEAN, INT],
            (INT, FLOAT): [FLOAT, FLOAT, FLOAT, FLOAT, ERROR, ERROR, BOOLEAN, BOOLEAN, FLOAT],
            (INT, CHAR): [INT, INT, INT, INT, ERROR, ERROR, BOOLEAN, BOOLEAN, INT],
            (INT, STRING): [STRING, ERROR, ERROR, ERROR, ERROR, BOOLEAN, BOOLEAN, BOOLEAN, ERROR],
            (INT, VECTOR): [VECTOR, ERROR, ERROR, ERROR, ERROR, ERROR, BOOLEAN, BOOLEAN, ERROR],
            (FLOAT, FLOAT): [FLOAT, FLOAT, FLOAT, FLOAT, ERROR, ERROR, BOOLEAN, BOOLEAN, FLOAT],
            (FLOAT, CHAR): [STRING, ERROR, ERROR, ERROR, ERROR, ERROR, BOOLEAN, BOOLEAN, ERROR],
            (FLOAT, STRING): [STRING, ERROR, ERROR, ERROR, ERROR, BOOLEAN, BOOLEAN, BOOLEAN, ERROR],
            (FLOAT, VECTOR): [VECTOR, ERROR, ERROR, ERROR, ERROR, ERROR, BOOLEAN, BOOLEAN, ERROR],
            (CHAR, CHAR): [INT, INT, INT, INT, ERROR, ERROR, BOOLEAN, BOOLEAN, CHAR],
            (CHAR, STRING): [STRING, ERROR, ERROR, ERROR, ERROR, BOOLEAN, BOOLEAN, BOOLEAN, ERROR],
            (BOOLEAN, BOOLEAN): [ERROR, ERROR, ERROR, ERROR, BOOLEAN, BOOLEAN, ERROR, ERROR, BOOLEAN],
            (STRING, STRING): [STRING, ERROR, ERROR, ERROR, ERROR, BOOLEAN, BOOLEAN, BOOLEAN, ERROR],
            (VECTOR, VECTOR): [VECTOR, ERROR, ERROR, ERROR, ERROR, BOOLEAN, BOOLEAN, BOOLEAN, ERROR]
        }
    
    def get_type(self, left_op, right_op, operator):
        operator_index = {
            PLUS: 0, MINUS: 1, TIMES: 2, DIVIDE: 3,
            AND: 6, OR: 7,
            GREATER: 8, LESS: 8, GREATERTHAN: 8, LESSTHAN: 8, NOTEQUAL: 8, EQUALS: 8,
            ASSIGN: 9
        }.get(operator, None)
        
        if operator_index is not None:
            types = self.cube.get((left_op, right_op), None)
            if not types:
                types = self.cube.get((right_op, left_op), None)
            if types:
                return types[operator_index]
        return ERROR  # Invalid operation or operand types
