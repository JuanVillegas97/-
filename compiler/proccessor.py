class Processor:
    __instance = None

    @staticmethod
    def get_instance(quadruples):
        """Static method to retrieve the singleton instance."""
        if Processor.__instance is None:
            Processor.__instance = Processor(quadruples)
        return Processor.__instance

    def __init__(self, quadruples):
        if Processor.__instance is not None:
            raise Exception("This class is a singleton. Use get_instance() method to get the instance.")
        else:
            Processor.__instance = self
            self.__quadruples = quadruples

