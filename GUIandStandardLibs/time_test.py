import time

#help(time)

#print(time.gmtime(0))
#print(time.localtime())
#print(time.time())

#actualtime= time.localtime()
#print(actualtime)
#print("Year: ", actualtime[0], actualtime.tm_year)
#print("Month: ", actualtime[1], actualtime.tm_mon)
#print("Day: ", actualtime[2], actualtime.tm_mday)
#print("Hours: ", actualtime[3], actualtime.tm_hour)
#print("Minutes: ", actualtime[4], actualtime.tm_min)

import random

input('Press enter to start')

wait_time = random.randint(1,6)
time.sleep(wait_time)
start_time = time.time()

input('Press enter to start')

end_time = time.time()

print('Started at '+ time.strftime("%X", time.localtime(start_time)))
print('Ended at '+ time.strftime("%X", time.localtime(end_time)))

print('Your reaction time was {} seconds'.format(start_time - end_time))