from cs50 import get_int
from cs50 import get_string
from sys import argv
import sys
import csv

"""

answer = input("What is your name ? ")
print(f"Hello, {answer}")

print("Enter only integers.")
try:
    x = int(input("x: "))
except ValueError:
    print("That is not an int!")
    exit()
try:
    y = int(input("y: "))
except ValueError:
    print("That is not an int!")
    exit()
print(x + y)

print("Enter only integers.")
from cs50 import get_int

a = get_int("a: ")
b = get_int("b: ")
c = a / b
print(f"{c:.50f}")

print("Enter only integers.")
points = get_int("How many points did you lose ? ")
if points < 2:
    print("You lost fewer points than me.")
elif points > 2:
    print("You lost more points than me.")
else:
    print("You lost same points than me.")

print("Enter only integers.")
n = get_int("n: ")
if n % 2 == 0:
    print("even")
else:
    print("odd")

# MEOW
def main():
    meow(3)
def meow(n):
    for i in range(n):
        print("meow")
main()



# AGREE

s = get_string("Do you agree ? ").lower()
if s in ("y", "e", "s,", "ye", "yes"):
    print("Agreed.")
elif s in ("n", "o", "no"):
    print("Not Agreed.")
    



def main():
    height = get_height()
    for i in range(height):
        print("#")


def get_height():
    while True:
        try:
            n = int(input("Height: "))
            if n > 0:
                break
        except ValueError:
            print("That is not an integer! ")
    return n

main()

scores = []
for i in range(3):
    score = get_int("Score: ")
    scores += [score]
average = sum(scores) / len(scores)
print(f"Average: {average}")

before = get_string("Before: ")
print(f"After: {before.upper()}")



if len(sys.argv) != 2:
    print("Missing command-line argument")
    sys.exit(1)
print(f"hello, {sys.argv[1]}")
sys.exit(0)



numbers = [4, 6, 8, 2, 7, 5, 0]
if 0 in numbers:
    print("Found")
    sys.exit(0)
print("Not Found")



names = ["Bill", 'Chatlie', 'Fred', 'George', 'Ginny', 'Percy', 'Ron']
if "Ron" in names:
    print("Found")
    sys.exit(0)
    print("Not Found")
    sys.exit(0)
    


people = {"Carter": "+1-617-495-1000", "David": "+1-949-468-2750"}

name = get_string("Name: ")
if name in people:
    number = people[name]
    print(f"Number: {number}")



name = get_string("Name: ")
number = get_string("Number: ")
with open("phonebook.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, number])



import pyttsx3
engine = pyttsx3.init()
name = input("What is your name ? ")
engine.say(f"hello. {name}")
engine.runAndWait()

"""

import qrcode
import os

img = qrcode.make(
    "https://www.youtube.com/watch?v=SjKEV8sDIAA&list=PLM6zHRlcg3CZ8gb7S55v_Ag1_FlNi0XKA&index=2&t=6299spytho"
)
img.save("qr.png", "PNG")
os.system("open qr.png")
