class Human:
#constructor __init__
    def __init__(self, name, group):
        self.Name = name
        self.Group = group
    def ToString(self):
        print(f"Name: {self.Name}\n"
        f"Group: {self.Group}")