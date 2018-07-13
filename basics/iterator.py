__author__= 'eduh'

#string = '123456789'
#my_iterator = iter(string)
#print(my_iterator)
#print(next(my_iterator))


#same thing
#for char in string:
#    print(char)

#for char in iter(string):
#    print(char)

even = [2,4,6,8]
odd = [1,3,5,7,9]

even_iter = iter(even)
odd_iter = iter(odd)

for numbers in range(0, len(even)):
    next_number = next(even_iter)
    print(next_number)
