import keyword
import datetime


print('Hello World')

def is_adult(age):
    if age >= 16:
        return True
    else:
        return False
result1 = is_adult(45)

def is_adult(age):
    return age >= 16
result1 = is_adult(15)
print(result1)

print(type(()))
print(type([]))

print(keyword.kwlist)

number1 = 10
if number1  > 0:
    print('positive')
else:
    print(') or positive')

message ='positive' if number1 > 0 else '0 or negative'
print(message)

# list is arrays []
number2 = [2,1,3,5,4,6,8,7,0,9]
#number2.sort()
#number2.reverse()
#number2.remove(item)
# del numbers [index
#numbers2.pop()
#number2.append(1000)
value1 = number2.__len__()
value2 = number2[2]
print(value2)

# sets {}
# dupilcates not allowed
numberList = [1,1]
numberSet = {1,1}
print(numberList)
print(numberSet)

# Dictionaries - Key, Value pair data structure

person = {
    'name': 'Jamal',
    'age': 20,
    'address': 'USA'
}
print(person['address'])

# BREAK AND CONTINUE

"""
number3 =0
while number3 < 10:
    if number3 ==5:
        break
#        print('number is 5 hooray')
    number3 += 1
    print(number3)
"""
number3 =0
while number3 < 10:
    number3 += 1
    if number3 < 5:
        continue
    print(number3)

# CLASSES AND OBJECTS

class Phone:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def call(self, phoneNumber):
        print(f'{self.brand} is calling {phoneNumber}')

iphone = Phone("Iphone 7", 300)
samsung = Phone("S20", 1400)

print(iphone.brand)
print(iphone.price)
iphone.call('999')

# DATE TIME
print(datetime.datetime.now())
print(datetime.datetime.now().time())

# WORKING WITH FILES

'''
file = open('./data.csv', 'w')
file.write('id,name,email\n')
file.write('1,Jamilah,test1\n')
file.write('2,Wendy,test2\n')
file.write('3,Louise,test3\n')
file.close()
'''

file = open('./data.csv', 'r')
# print(file.read())
#for line in file:
#    print(line)
print(file.readlines())
file.close()

