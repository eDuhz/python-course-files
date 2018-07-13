__author__ = 'eduh'

t = 'a', 'b', 'c'
print (t)

print ('a', 'b', 'c')
print (('a', 'b', 'c'))

welcome = 'Welcome to my Nightmare', 'Alice Cooper', 1975
bad = 'Bad Company', 'Bad Company', 1974
budgie = 'Nightflight', 'Budgie', 1981
imelda = 'More Mayhem', 'Emilda May', 2011
metallica = 'Ride the Lightning', 'Metallica', 1984

print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])

#tuple is a immutable object
imelda = imelda[0], 'Imelda May', imelda[2]
print(imelda)

#list is a mutable object
metallica2 = ['Ride the Lightning', 'Metallica', 1984]
print(metallica2)
metallica2[0] = 'Master of Puppets'
print(metallica2)

#unpacking the tuple
title, artist, year = imelda
print('Title: {}, Artist: {}, Year: {}'.format(title, artist, year))

imelda2 = 'More Mayhem', 'Imelda May', 2011, ((1, 'Pulling the Rug'), (2, 'Psycho'), (3, 'Mayhem'), (4, 'Kentish Town Waltz'))
title, artist, year, tracks = imelda2
print(title)
print(artist)
print(year)
print(tracks)