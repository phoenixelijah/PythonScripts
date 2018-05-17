# capExtractor
# by PhoenixElijah
# 5/17/2018 3:41 PM
# capExtractor will take the capitals from quote and represent them only

quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

# Use a for loop and an if statement to print just the capitals in the quote above.
for word in quote:
    if word in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
       print(word)
