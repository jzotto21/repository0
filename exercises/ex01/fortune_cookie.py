"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730163077"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...


print("Your fortune cookie says...")
fortune = randint(0, 4)
if fortune == 0:
    print("Speak your mind, even if your voice shakes.")
else:
    if fortune == 1:
        print("Do not forget to look at the stars once in awhile.")
    else:
        if fortune == 2:
            print("Buy the squishmallow!")
        else:
            if fortune == 3:
                print("'Take what you can. Give nothing back.' - Captain Jack Sparrow")
            else:
                if fortune == 4:
                    print("Never give up. Never surrender.")

print("Now, go spread positive vibes!")