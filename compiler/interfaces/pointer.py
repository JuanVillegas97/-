class Pointer:
    def __init__(self, memory_address, value):
        self.__memory_address = memory_address
        self.__value = value

    def get_memory_address(self):
        return self.__memory_address

    def set_memory_address(self, memory_address):
        self.__memory_address = memory_address

    def get_value(self):
        return self.__value

    def set_value(self, value):
        self.__value = value
