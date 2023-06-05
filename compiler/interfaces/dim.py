class Dim:
    def __init__(self,lims):
        self.lims = lims
        self.m = None
        
    def get_string(self):
        return f"[s={self.lims}, m={self.m}]->"