class SemanticCube:
    def __init__(self):
        self.semantic = {
            ('int', 'int'): ['int', 'int', 'int', 'float', 'boolean', 'boolean'],
            ('int', 'float'): ['float', 'float', 'float', 'float', 'boolean', 'boolean'],
            ('int', 'char'): ['int', 'int', 'int', 'int', 'boolean', 'boolean'],
            ('int', 'boolean'): ['NaN', 'NaN', 'NaN', 'NaN', 'NaN', 'NaN'],
            ('int', 'string'): ['string', 'NaN', 'NaN', 'NaN', 'boolean', 'boolean'],
            ('int', 'vector'): ['NaN', 'NaN', 'NaN', 'NaN', 'NaN', 'NaN'],
            ('float', 'float'): ['float', 'float', 'float', 'float', 'boolean', 'boolean'],
            ('float', 'char'): ['string', 'NaN', 'NaN', 'NaN', 'boolean', 'boolean'],
            ('float', 'boolean'): ['NaN', 'NaN', 'NaN', 'NaN', 'NaN', 'NaN'],
            ('float', 'string'): ['NaN', 'NaN', 'NaN', 'NaN', 'boolean', 'boolean'],
            ('float', 'vector'): ['NaN', 'NaN', 'NaN', 'NaN', 'NaN', 'NaN'],
            ('char', 'char'): ['int', 'int', 'int', 'int', 'boolean', 'boolean'],
            ('char', 'boolean'): ['NaN', 'NaN', 'NaN', 'NaN', 'NaN', 'NaN'],
            ('char', 'string'): ['string', 'NaN', 'NaN', 'NaN', 'boolean', 'boolean'],
            ('boolean', 'boolean'): ['NaN', 'NaN', 'NaN', 'NaN', 'boolean', 'boolean'],
            ('string', 'string'): ['string', 'NaN', 'NaN', 'NaN', 'NaN', 'boolean'],
            ('vector', 'vector'): ['vector', 'NaN', 'NaN', 'NaN', 'NaN', 'boolean']
        }

    def get_type(self, left_op, right_op, operator):
        types = self.semantic.get((left_op, right_op), None)
        if types:
            operator_index = {'+': 0, '-': 1, '*': 2, '/': 3, 'AND': 4, 'OR': 5}.get(operator, None)
            if operator_index is not None:
                return types[operator_index]
        return 'ERROR'  # Invalid operation or operand types
