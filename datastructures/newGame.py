__author__='eduh'

locations = {0:'You\'re sitting in front of your computer learning Python',
             1:'You\'re standing at the end of a road before a small brick building',
             2:'You\'re at the top of a hill',
             3:'You\'re insie a building, a well house for a small stream',
             4:'You\'re in a valley beside a stream',
             5:'You\'re in a forest'}

#exits = {0: {'Q':0},
#         1: {'W':2, '2':2, 'E':3, '3':3, 'N':5, '5':5, 'S':4, '4':4, 'Q':0},
#         2: {'N':5, '5':5, 'Q':0},
#         3: {'W':1, '1':1, 'Q':0},
#         4: {'N':1, '1':1, 'W':2, '2':2,'Q':0},
#         5: {'W':2, '2':2, 'S':1, '1':1,'Q':0}}

exits = {0: {'Q':0},
         1: {'W':2, 'E': 3, 'N':5, 'S':4, 'Q':0},
         2: {'N':5, 'Q':0},
         3: {'W':1, 'Q':0},
         4: {'N':1, 'W':2, 'Q':0},
         5: {'W':2, 'S':1, 'Q':0}}

namedExits = {1:{"2":2, "3":3, "5":5, "4":4},
              2:{"5":5},
              3:{"1":1},
              4:{"1":1, "2":2},
              5:{"2":2, "1":1}}

vocabulary = {'QUIT':   'Q',
              'NORTH':  'N',
              'SOUTH':  'S',
              'EAST':   'E',
              'WEST':   'W',
              'ROAD':   '1',
              'HILL':   '2',
              'BUILDING':'3',
              'VALLEY': '4',
              'FOREST': '5'}

loc = 1
while True:
    availableExits = ', '.join(exits[loc].keys())
    print(locations[loc])

    if loc == 0:
        break
    else:
        allExits = exits[loc].copy()
        allExits.update(namedExits[loc])

    direction = input('Available exits are '+availableExits+ ' ').upper()
    print()

    if len(direction) > 1:
        words = direction.split()
        for word in words:
            direction = vocabulary[word]
            break

    if direction in allExits:
        loc = allExits[direction]
    else:
        print('You cannot go in that direction')
