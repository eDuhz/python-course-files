__author__='eduh'

import random
highest = 10
answer = random.randint(1, highest)

print('Please guess a number between 1 and {}'.format(highest))

guess = int(input())

while guess != answer:
    if guess < answer:
        print('Guess Higher')
    if guess > answer:
        print('Guess lower')
    guess = int(input())
    if guess == 0:
        print('booooh quitter')
        break

else:
    print('You got it bruuh!')