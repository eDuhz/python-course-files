__author__ = 'eduh'


fruit = {"orange": "a sweet, orange citrus fruit",
         "apple":"good for making cinder",
         "lemon":"a sour, yellow citrus fruit",
         "grape":"a small, sweet fruit growing in bunches",
         "lime":"a sour, green citrus fruit"}

veg = {'cabbage': 'every child\'s favourite',
       'sprouts': 'hmmm, lovely',
       'spinach': 'can i have some more fruit, please'}

print(veg)
print('-'*40)
veg.update(fruit)
print(veg)
print('-'*40)

nice_and_nasty = fruit.copy()
nice_and_nasty.update(veg)
print(nice_and_nasty)
print('-'*40)