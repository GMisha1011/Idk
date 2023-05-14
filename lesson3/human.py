class Human:
    def __init__(self, name, role):
        self.Name = name
        self.Role = role

    def ToString(self):
        if(self.Name != None or self.Name != ""):
            print(f"Name: {self.Name}")
        else:
            print("Attribute name is none or empty")