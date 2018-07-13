__author__='eduh'

farm_animals = {'Sheep', 'Cow', 'Hen'}
print(farm_animals)

for animal in farm_animals:
    print(animal)

print('='* 30)

wild_animals = set(['Lion', 'Tiger', 'Panther', 'Elephant', 'Hare'])
print(wild_animals)
print('='* 30)

farm_animals.add('Horse')
wild_animals.add('Horse')
print(farm_animals)
print('='* 30)
print(wild_animals)
print('='* 30)

empty_set = set()
empty_set_2 = {}
empty_set.add('A')
#empty_set_2.add('A') NOT GONNA WORK

even = set(range(0,40,2))
print(even)
print('='* 30)
print(len(even))
print('='* 30)
squares_tuple = (4,6,9,16,25)
squares = set(squares_tuple)
print(squares)
print('='* 30)
print(len(squares))
print('='* 30)
print(even.union(squares))
print('='* 30)
print(len(even.union(squares)))
print('='* 30)
print(squares.union(even))
print('='* 30)
print(even.intersection(squares))
print('='* 30)
print(even & squares)
print('='* 30)
print(squares.intersection(even))
print('='* 30)
print(squares & even)
print('='* 30)


print(sorted(even))
print(sorted(squares))

print('even minus squares')
print (sorted(even.difference(squares)))
print (sorted(even - squares))

print('='* 30)

print('squares minus even')
print(sorted(squares.difference(even)))
print(sorted(squares - even))
print('='* 30)