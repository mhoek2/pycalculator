import random
from turtledemo.chaos import jumpto

# tuple instead of list because tuple allows you to access individual elements by using index and can't be changed.
alphabet = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")

random_code2 = ""
for i in range(0, 4):
    random_letter = alphabet[random.randint(0,24)]
    random_code2 += random_letter
print(random_code2)