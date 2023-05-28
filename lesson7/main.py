from counter import Counter
from generator import Generator
"""
name = "Andrii"
for i in range(1, 15 , 3):#iter(name):
    print(i)

try:
    iterator = iter(name)
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
except StopIteration:
    print("A")
counter = Counter(9)
for i in counter:
    print(i)
"""
generator = Generator(0)
res = generator.Raise_to_the_degrees_F(12345, 500)
print(res)
for item in generator.Raise_to_the_degrees_F(12345, 500):
    print(f"{item}\n")