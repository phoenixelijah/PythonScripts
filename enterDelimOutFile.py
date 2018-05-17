# enterDelimOutFile
# by PhoenixElijah
# 5/15/2018 11:03 AM
# enterDelim takes 2 inputs - the delimeter and the file path
# output to screen items from file with each on a new line

delim = input("what's the delimiter?: ")
file = input("whats the file path?: ")

f = open(file)
for l in f.readlines():
    # print("\n")
    for x in (l.strip().split(delim)):
        print(str(x))
    f.close()
