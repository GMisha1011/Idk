from human import Human
from speak import Speak
class CatOrDog(Human, Speak):
    def __init__(self, catordog):
        self.Cat = list()
        self.Dog = list()
        self.SayName(catordog)
    def __str__(self):
        return f"{super().__str__()}Cat or dog?: {self.CatOrDog}"