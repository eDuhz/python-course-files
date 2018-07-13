__author__ = 'eduh'

my_list = list(range(10))
print(my_list)

even = list(range(0,10,2))
odd = list(range(1,10,2))

print(even)
print(odd)

my_string = 'iuaodaskjiohllkdsjwueiukjsdlzxcr'
print(my_string.index('e'))
print(my_string[4])

print(my_list.index(3))

sevens = range(7, 1000000, 7)
x = int(input('Please enter a positive number less than one million:'))
if x in sevens:
    print('{} is divisible by seven'.format(x))

my_range = my_list[::2]
print(my_range)
print(my_range.index(4))

decimals = range(0,100)
print(decimals)

in_between = decimals[3:40:3]
print(in_between)

for i in in_between:
    print(i)
print('=' * 40)

for i in range(3,40,3):
    print(i)

print('=' * 40)

print(range(0,5,2) == range(0,6,2))
print(list(range(0,5,2)))
print(list(range(0,6,2)))
r = range(0,100)

for i in r[::-2]:
    print(i)
print('=' * 40)
for i in range(99,0,-2):
    print(i)
print('=' * 40)

print(range(0,100)[::-2] == range(99,0,-2))

print('=' * 40)

backString = 'egaugnal lufrewop yrev a si nohtyP'
print(backString[::-1])

new_r = range(0,10)
for i in new_r[::-1]:
    print(i)