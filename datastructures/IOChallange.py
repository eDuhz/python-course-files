__author__ = 'eduh'

with open('Classes 8 to 15\sample.txt', 'a') as jabba_file:
    for i in range (1,13):
        for j in range (2,13):
            print('{0:2} times {1} is {2:<2}'.format(i,j,i*j), file=jabba_file, flush=True)
        print('-'*20, file= jabba_file, flush= True)