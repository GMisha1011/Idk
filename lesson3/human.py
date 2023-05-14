class Human:
#constructor __init__
    def __init__(self, name, role):
        self.Name = name
        self.Role = role
    def ToString(self):
        print(f"Name: {self.Name}\n"
        f"Role: {self.Role}")