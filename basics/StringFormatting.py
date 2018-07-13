__author__= 'eduh'

age = 24
print('My age is ' + str(age) + ' years')

#replacement field examples
print('My age is {0} years'.format(age))

print(""" January: {2}
February: {0}
March: {2}
April: {1}
May: {2}
June: {1}
July: {2}
August: {2}
September: {1}
October: {2}
November: {1}
December: {2}""".format(28, 30, 31))
#right format
for i in range(1,5):
    print('{0:2} squared, {1:4} squared, {2:4} cubed'.format(i, i**2, i**3))
#left format
for i in range(1,5):
    print('{0:<2} squared, {1:<4} squared, {2:<4} cubed'.format(i, i**2, i**3))

#unformatted
for i in range(1,5):
    print('{0} squared, {1} squared, {2} cubed'.format(i, i**2, i**3))
#unnasigned
for i in range(1,5):
    print('{:2} squared, {:4} squared, {:4} cubed'.format(i, i**2, i**3))


#old format
print('My age is %d years' % age)
print('My age is %d %s, %d %s' % (age, 'years', 6, 'months'))

for i in range(1,5):
    print('%2d squared, %4d squared, %4d cubed' % (i, i**2, i**3))

print('Pi is approximately %12.50f' % (22/7))


