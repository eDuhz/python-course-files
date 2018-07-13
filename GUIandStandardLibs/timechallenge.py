__author__ = 'eduh'

import datetime
import pytz

dateObj = datetime.datetime

available_zones = {'1': "Africa/Tunis",
                  '2': 'Asia/Kolkata',
                  '3': 'Australia/Adelaide',
                  '4': 'Europe/Brussels',
                  '5': 'Europe/London',
                  '6': 'Japan',
                  '7': 'Pacific/Tahiti',
                  '8': 'US/Hawaii',
                  '9': 'Zulu'}

print('Please choose a time zone from 1 to 9 or 0 to quit')



while True:
    for place in sorted(available_zones):
        print('\t{}. {}'.format(place, available_zones[place]))
    choice = input()
    
    if choice == '0':
        break

    if choice in available_zones.keys():
        tz_to_display = pytz.timezone(available_zones[choice])
        world_time = dateObj.now(tz=tz_to_display)
        print('The time in {} is {} {}'.format(available_zones[choice], world_time.strftime('%A %x %X %z'), world_time.tzname()))
        print('The local time is {}'.format(dateObj.now().strftime('%A %x %X')))
        print('The local time is {}'.format(dateObj.now().strftime('%A %x %X')))
        print('-' * 40)