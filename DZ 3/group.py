class Group:
    def __init__(self, group):
        self.Group = group
        self.B2011 = list()
        self.V2011 = list()
    def AddB2011(self, human):
        self.B2011.append(human)
    def AddV2011(self, human):
        self.V2011.append(human)
    def ToStringB2011(self, B2011Name):
        print(f"This guy: {B2011Name} is from {self.Group} group")
    def ToStringV2011(self, V2011Name):
        print(f"This guy: {V2011Name} is from {self.Group} group")