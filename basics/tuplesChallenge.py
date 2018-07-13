__author__ = 'eduh'

imelda2 = 'More Mayhem', 'Imelda May', 2011, ((1, 'Pulling the Rug'), (2, 'Psycho'), (3, 'Mayhem'), (4, 'Kentish Town Waltz'))

title, artist, year, tracks = imelda2
print('Title: {}\nArtist: {}\nYear: {}'.format(title, artist, year))
for song in tracks:
    track, title = song
    print('\tTrack number: {}, Title: {}'.format(track, title))