import random
from turtledemo.chaos import jumpto

alphabet = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")

def get_random_code(num_letters):
    random_code2 = ""
    for i in range(0, num_letters):
        random_letter = alphabet[random.randint(0,24)]
        random_code2 += random_letter
    return random_code2
random_code = get_random_code(4)
print(random_code)