class Human:
    def __init__(self, name, age):
        self.Name = name
        self.Age = age
    def __str__(self):
        return f"Name: {self.Name}\nAge: {self.Age}"