__author__= 'eduh'

greeting = 'Hello'
a = 12
b = 23.5
print (a + b)
print (a - b)
print (a * b)
print (a/b)
print (b//a)
print (a%b)
print (greeting + ' ' + str(b))

for i in range(1 , int(b//a)):
    print(i)

parrot = "Norwegian Blue"
print(parrot[0:6])
#Same thing as 
print(parrot[:6])
#Start at 6
print(parrot[6:])
print(parrot[-4:-2])
print(parrot[:6:2])
print(parrot[:6:3])

number = "9,223,372,036,854,775,807"
print(number[1::4])
numbers = '1, 2, 3, 4, 5, 6, 7, 8, 9'
print(numbers[0::3])

string = 'shitty '
print(string + ' ' + greeting)
print(string * 5)

today = 'friday'
print('day' in today)
print('ass' in parrot)