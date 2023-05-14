from human import Human
from auto import Auto
Kirril = Human("Kirril", 1)
Nikita = Human("Nikita", 0)
Mykhail = Human("Mykhail", 0)
Pavlo = Human("Pavlo", 0)
humans = list()
humans.append(Kirril)
humans.append(Nikita)
humans.append(Mykhail)
humans.append(Pavlo)
auto = Auto("BMW X7")
for Human in humans:
    if(Human.Role == 1):
        auto.AddDrivers(Human)
    else:
        auto.AddPassengers(Human)
for driver in auto.Drivers:
    print(f"Driver of {auto.Brand} is {driver}")
for Passenger in auto.Passengers:
    print(f"Passengers: {Passengers}")