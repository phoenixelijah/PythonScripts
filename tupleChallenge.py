# Given the tuple below that represents the Imelda May album "More Mayhem", write
# code to print the album details, followed by a listing of all the tracks in the album.
#
# Indent the tracks by a single tab stop when printing them (remember that you can pass
# more than one item to the print function, separating them with a comma).

imelda = "More Mayhem", "Imelda May", 2011, (
    (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))

length = len(imelda)
print(length)
title, artist, year, tracks = imelda


print(title)
print(artist)
print(year)
for i in tracks:
    print("\t", i)

# for e:
#     print(i)
# print(imelda)

numbers = range(13)
new_range = numbers[1::2]
for i in new_range:
    print(i, end=', ')
