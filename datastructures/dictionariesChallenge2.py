__author__='eduh'

locations = {0:{'desc': 'You\'re sitting in front of your computer learning Python', 
                'exits': {},
                'namedExits': {}},
             1:{'desc': {'You\'re standing at the end of a road before a small brick building'}, 
                'exits': {'W':2, 'E': 3, 'N':5, 'S':4, 'Q':0},
                'namedExits': {"2":2, "3":3, "5":5, "4":4}},
             2:{'desc': {'You\'re at the top of a hill'}, 
                'exits': {'N':5, 'Q':0},
                'namedExits': {"5":5}},
             3:{'desc': {'You\'re insie a building, a well house for a small stream'}, 
                'exits': {'W':1, 'Q':0},
                'namedExits': {"1":1}},
             4:{'desc': {'You\'re in a valley beside a stream'}, 
                'exits': {'N':1, 'W':2, 'Q':0},
                'namedExits': {"1":1, "2":2}},
             5:{'desc': {'You\'re in a forest'}, 
                'exits': {'W':2, 'S':1, 'Q':0},
                'namedExits': {"2":2, "1":1}}
             }

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

while loc != 0:

    availableExits = ', '.join(locations[loc]['exits'].keys())
    print(locations[loc]['desc'])

    allExits = locations[loc]['exits'].copy()
    allExits.update(locations[loc]['namedExits'])
    print(allExits)

    direction = input('Available exits are '+availableExits+ ' ').upper()
    print()

    if len(direction) >1:
        words = direction.split()
        for word in words:
            if word in vocabulary:
                direction = vocabulary[word]
                break

    if direction in allExits.keys():
        loc = allExits[direction]
    else:
        print('You cannot go in that direction')

print(locations[loc]['desc'])