class Quadruple:
    def __init__(self, operator, left_operand, right_operand, avail):
        self.__operator  = operator
        self.__left_operand = left_operand
        self.__right_operand = right_operand
        self.__avail = avail
        
    def get_operator(self):
        return self.__operator
    
    def get_left_operand(self):
        return self.__left_operand
    
    def get_right_operand(self):
        return self.__right_operand
    
    def get_avail(self):
        return self.__avail