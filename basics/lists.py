
__author__ = 'eduh'

list_1 = []
list_2 = list()

print('List 1: {}'.format(list_1))
print('List 2: {}'.format(list_2))

if list_1 == list_2:
    print('lists are equal')

even = [2,4,6,8]
#points to even
another_even = even
#to create another list with the even content, use list(even)
another_list = list(even)

print(another_even is even)
print(another_list is even)

another_even.sort(reverse=True)
print(even)

odd = [1,3,5,7,9]

numbers = [even,odd]
print(numbers)
for lists in numbers:
    print(lists)
    for value in lists:
        print(value)