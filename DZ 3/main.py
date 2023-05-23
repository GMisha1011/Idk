from human import Human
from group import Group

kyrylo = Human("Kyrylo", 1)
nikita = Human("Nikita", 1)
mykhailo = Human("Mykhailo", 0)
pavlo = Human("Pavlo", 0)
humans = list()
humans.append(kyrylo)
humans.append(mykhailo)
humans.append(pavlo)
humans.append(nikita)
group = Group("B2011")
for human in humans:
    if(human.Role == 1):
        group.AddB2011(human.Name)
    else:
        group.AddV2011(human.Name)
for B2011 in group.B2011:
    group.ToStringB2011(B2011)
for V2011 in group.V2011:
    group.ToStringV2011(V2011)