__author__ = 'eduh'
#ways to read files

#jabber = open('C:\Coding\Python - Course\Python Course Files\PythonUdemyCourse\PythonUdemyCourse\Classes 8 to 15\sample.txt', 'r')

#for line in jabber:
#    if 'jabberwock' in line.lower():    
#        print(line)
#
#jabber.close()

#with open('Classes 8 to 15\sample.txt', 'r') as jabba:
#    for line in jabba:
#        if 'JAB' in line.upper():
#            print(line)

#with open("Classes 8 to 15\sample.txt", 'r') as jabber:
#    lines = jabber.readlines()
#    
#print(lines)

#for line in lines:
#    print(line, end = '')

with open('Classes 8 to 15\sample.txt', 'r') as jabber:
    lines = jabber.read()

for line in lines[::-1]:
    print (line, end = '')