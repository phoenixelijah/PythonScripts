a = b = c = d = 12
print(a)

a, b = 12, 13
print(b, a)

# the following concept is called "unpacking the tuple"
# it assigns variables to the values from the tuple
# this will fail if all values are not unpacked
imelda = "More Mayhem", "Imilda May", 2011
title, artist, year = imelda

print(title)
print(artist)
print(year)
