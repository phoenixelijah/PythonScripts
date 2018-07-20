import random

words = str(dir())
# for item in words:
#     print(item)
print(dir(random))

help(random.randint)
for obj in dir(random):
    if obj[0] != '_':
        print(obj)
