# myIfChallenge
# by PhoenixElijah
# 5/11/2018 2:11 PM

name = input("What's your name? ")
age = int(input("How old are ya'? "))
if (age <= 18) or (age > 30):
    print("no go, {0}".format(name))

else:
    print("welcome to the show {0}!".format(name))