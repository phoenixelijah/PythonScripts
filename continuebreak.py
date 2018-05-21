# shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
# for item in shopping_list:
#     if item == 'spam':
#         break
#
#     print("Buy " + item)

meal = ["egg", "bacon", "spam", "beans", "sausages", "spams"]
nasty_food_item = ''

for item in meal:
    print(item)
    if item == 'spam':
        nasty_food_item = item
        break
else:
    print("I'll have a plate of that, then, please")

if nasty_food_item:
    print("Can't I have anything without spam in it")




# Modify this loop to stop when i is exactly divisible by 11
for i in range(0, 20):
    if (i > 0) and ((i%3 == 0) or (i%5 == 0)):
        continue
    print(i)
