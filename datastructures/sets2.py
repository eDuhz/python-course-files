__author__ = 'eduh'

even = set(range(0,40,2))
print(even)
squares_tuple = (4,6,9,16,25)
squares = set(squares_tuple)
print(squares)
print('='* 30)

print('symmetric even minus squares')
print(sorted(even.symmetric_difference(squares)))
print('symmetric squares minus even')
print(sorted(squares.symmetric_difference(even)))

print('='* 30)

squares.discard(9)
squares.remove(25)
#squares.discard(8) #no error, does nothing

#print(squares)
#squares.remove(8) should be an error

if squares.issubset(even):
    print('squares is a subset of even')
if even.issuperset(squares):
    print('even is a superset of squares')

try:
    squares.remove(8)
except KeyError:
    print('The item 8 is not a member of the set')

newset = frozenset(range(0,100,2))
print(newset)

