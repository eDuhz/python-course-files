__author__= 'eduh'


fruit = {"orange": "a sweet, orange citrus fruit",
         "apple":"good for making cinder",
         "lemon":"a sour, yellow citrus fruit",
         "grape":"a small, sweet fruit growing in bunches",
         "lime":"a sour, green citrus fruit"}

print(fruit)
print('-' *40)
ordered_keys = list(fruit.keys())
ordered_keys.sort()
#ordered_keys = sorted(list(fruit.keys()))
#for f in ordered_keys:
#   print(f + " - " + fruit[f])

#fruit_keys = fruit.keys()
#fruit_values = fruit.values()
#print(fruit_keys)
#print(fruit_values)

print(fruit.items())
print('-' *40)
f_tuple = tuple(fruit.items())
print (f_tuple)
print('-' *40)
for snack in f_tuple:
    item, description = snack
    print(item + ' is ' + description)
print('-' *40)
print(dict(f_tuple))
print('-' *40)