import pickle

# imelda = ('More Mahyem',
#           'Imelda May',
#           '2011',
#           ((1, 'Pulling the rug'),
#            (2, 'Psycho'),
#            (3, 'Mahyem'),
#            (4, 'Kentish Town Waltz')))
#
# with open('imelda.pickle','wb') as pickle_file:
#     pickle.dump(imelda, pickle_file)



# LOADING THE FILE THAT WAS PREVIOUSLY WRITTEN

# with open('imelda.pickle','rb') as imelda_pickle:
#     imelda2 = pickle.load(imelda_pickle)
#     even_list = pickle.load(imelda_pickle)
#     odd_list = pickle.load(imelda_pickle)
#     x = pickle.load(imelda_pickle)
#
# print(imelda2)
#
# album, artist, year, track_list = imelda2
# print(album)
# print(artist)
# print(year)
# for track in track_list:
#     track_number, track_name = track
#     print(track_number, track_name)
# print("~"*80)
# for i in even_list:
#     print(i)
# for i in odd_list:
#     print(i)
# print(x)


# ADDING NEW THINGS TO THE BINARY FILE

imelda = ('More Mahyem',
          'Imelda May',
          '2011',
          ((1, 'Pulling the rug'),
           (2, 'Psycho'),
           (3, 'Mahyem'),
           (4, 'Kentish Town Waltz')))
even = list(range(0,10,2))      # once we have opened it for writing, we can dump as many things as we want.
odd = list(range(1,10,2))
with open('imelda.pickle','wb') as pickle_file:
    pickle.dump(imelda, pickle_file, protocol=pickle.HIGHEST_PROTOCOL)
    pickle.dump(even, pickle_file, protocol=0)  # once we have opened it for writing, we can dump as many things as we want.
    pickle.dump(odd, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)
    pickle.dump(2998302, pickle_file, protocol=pickle.HIGHEST_PROTOCOL)



# PRINTING THE ITEMS OF THE UPDATED FILE

with open('imelda.pickle','rb') as imelda_pickle:
    imelda2 = pickle.load(imelda_pickle)
    even_list = pickle.load(imelda_pickle)
    odd_list = pickle.load(imelda_pickle)
    x = pickle.load(imelda_pickle)

print(imelda2)

album, artist, year, track_list = imelda2
print(album)
print(artist)
print(year)
for track in track_list:
    track_number, track_name = track
    print(track_number, track_name)
print("~"*80)
for i in even_list:
    print(i)
print("~"*80)
for i in odd_list:
    print(i)
print("~"*80)
print(x)

print("~"*80)

# pickle.loads(b"cos\nsystem\n(S'del imelda.pickle'\ntR.")  -> this DELETES the file