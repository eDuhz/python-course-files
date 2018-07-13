__author__ = 'eduh'

string = 'my name is Eduardo Lemos'
vowels = 'aeiou '
result = ''
for char in string.lower():
    if char not in vowels:
        result += char

mySet = set(result)
print(sorted(mySet))

vowels2 = frozenset('aeiou')
finalSet = set(string.lower()).difference(vowels)
#print(finalSet)
finalList = sorted(finalSet)
print(finalList)