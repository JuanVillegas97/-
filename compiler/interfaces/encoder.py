from compiler.interfaces.quadruple import Quadruple
from compiler.interfaces.variable import variable
import json

class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Quadruple):
            return obj.__dict__
        if isinstance(obj, variable):
            return obj.__dict__
        return super().default(obj)