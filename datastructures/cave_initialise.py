__author__ = 'eduh'
import shelve

locations = shelve.open('locations')

locations['0'] = {'desc': 'You\'re sitting in front of your computer learning Python', 
                  'exits': {},
                  'namedExits': {}},
locations['1'] = {'desc': {'You\'re standing at the end of a road before a small brick building'}, 
                  'exits': {'W':'2', 'E': '3', 'N':'5', 'S':'4', 'Q':'0'},
                  'namedExits': {"2":'2', "3":'3', "5":'5', "4":'4'}},
locations['2'] = {'desc': {'You\'re at the top of a hill'}, 
                  'exits': {'N':'5', 'Q':'0'},
                  'namedExits': {"5":'5'}},
locations['3'] = {'desc': {'You\'re insie a building, a well house for a small stream'}, 
                  'exits': {'W':'1', 'Q':'0'},
                  'namedExits': {"1":'1'}},
locations['4'] = {'desc': {'You\'re in a valley beside a stream'}, 
                  'exits': {'N':'1', 'W':'2', 'Q':'0'},
                  'namedExits': {"1":'1', "2":'2'}},
locations['5'] = {'desc': {'You\'re in a forest'}, 
                  'exits': {'W':'2', 'S':'1', 'Q':'0'},
                  'namedExits': {"2":'2', "1":'1'}}


locations.close()

vocabulary = shelve.open("vocabulary")

vocabulary["QUIT"] = "Q"
vocabulary["NORTH"] = "N"
vocabulary["SOUTH"] = "S"
vocabulary["EAST"] = "E"
vocabulary["WEST"] = "W"
vocabulary["ROAD"] = "1"
vocabulary["HILL"] = "2"
vocabulary["BUILDING"] = "3"
vocabulary["VALLEY"] = "4"
vocabulary["FOREST"] = "5"


vocabulary.close()