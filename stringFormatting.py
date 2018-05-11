age = 24
# the following breaks python
# print("My age is " + age + " years")
# so instead
print("My age is " + str(age) + " years")

# replacement fields
print("My age is {0} years".format(age))
print("there are {0} days in {1}, {2}, {3}, {4}, {5}".format(31, "January", "March", "May", "July", "August"))

# string formatter operators
print("My age is %d years" % age)

# loop with formatting - the number in %2d means to use 2 characters regardless of value
# run it if you can't remember
for i in range(1, 12):
    print("No. %2d squared is %4d and cubed is %4d" % (i, i ** 2, i ** 3))

# setting precision. the 50 after the decimal says to allow 50 spaces after decimal in result
print("Pi is approximately %12f" % (22/7))  # allocates 12 spaces total
print("Pi is approximately %12.50f" % (22/7))  # allocates 50 decimal places

# new way of formatting - the numbers in the colon are value:space
for i in range(1, 12):
    print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i, i ** 2, i ** 3))

# same thing to left justify
for i in range(1, 12):
    print("No. {0:<2} squared is {1:<4} and cubed is {2:<4}".format(i, i ** 2, i ** 3))

data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"
print(data[::5])