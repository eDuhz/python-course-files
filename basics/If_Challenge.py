__author__ = 'eduh'
name = str(input('Type your name: '))
age = int(input('Type your age: '))

if 18 <= age < 31:
    print("""You're allowed to enter the holiday {0}""".format(name))
else:
    print('Fuck you bro, get outta here {0} you wanker'.format(name))

