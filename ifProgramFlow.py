# ifProgramFlow
# by PhoenixElijah
# 5/11/2018 9:48 AM
#
# name = input("Please enter your name: ")
# age = int(input("How old are you, {0}? ".format(name)))
# print(age)
#
# if age >= 18:
#     print("Your are old enough to vote.")
# else:
#     print("Please come back in {0} years".format(18 - age))
#
# the code here is clumsy but the course here was covering the flow


# print("Please guess a number between 1 and 10: ")
# guess = int(input())
#
# if guess <5:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == 5:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry you blew it")
#
# elif guess > 5:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == 5:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry you blew it")
#
# else:
#     print("you got it right away!")
#
# age = int(input("How old are you? "))
# if 16 <= age <= 65:
#     print("Have a good day at work.")
parrot = "Norwegian Blue"
letter = input("Enter a character: ")
if letter in parrot:
    print("Gimme a {}, Bob".format(letter))
else:
    print("I don't need that letter..")