from math import *
from student import Student
from Chef import Chef
from Chef import ChineseChef

phrase = "Giraffe Academy"
print(phrase.upper())
print(phrase[2])
print(phrase.index("r"))
print(pow(4, 6))
# name = input("Enter your name: ")
# print("My name is " + name)

number_grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [0]]
print(number_grid[2][2])
for row in number_grid:
    for col in row:
        print(col)

i = 1
while i <= 10:
    print(i)
    i += 1
print("Done with While Loop")

friends = ["Jim", "Karen", "Kevin"]
for friend in friends:
    print(friend)

student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Mike", "Journalism", 2.5, False)
student3 = Student("Sally", "Economics", 3.7, False)
student4 = Student("Will", "Chemistry", 1.9, True)
student5 = Student("John", "Petroleum", 1.1, True)
print(student2.gpa)

myChef = Chef()
myChef.make_chicken()

myChineseChef = ChineseChef()
myChineseChef.make_special_dish()
