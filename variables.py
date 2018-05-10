__author__ = 'phoenixelijah'
greeting = "Bruce"
_myName = "Tim"
Tim45 = "Good"
age = 24

# this throws an error
#print(greeting + age)

a = 12
b = 3
print(a + b)
print(a * b)
# returns float
print(a / b)
# returns int
print(a // b)

for i in range(1, a//b):
    print(i)

# operator precedence below equals -35
print(a + b / 3 -4 * 12)
# to fix
print((((a + b) / 3) -4) * 12)

bun_price = 2.40
money = 15
print(money // bun_price)


# STRING NOTES
# see below for how to use "::" to step through a sequence
# the example will pring the character at "0" and then every 3rd from there!
number = "1, 2, 3, 4, 5, 6, 7, 8, 9"
print(number[0::3])
print("hello " *5)
print("hello " *(5+4))
print("hello " *5 + "4")

