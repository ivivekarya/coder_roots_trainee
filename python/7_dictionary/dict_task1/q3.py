# #Q3 Write a program for a number guessing game where the computer 
# randomly selects a number between 1 and 100, and 
# the user tries to guess it. The program should give hints if
#  the guess is too high or too low.
import random
print("welcome to the world of numbers")

dict2=int(input("enter you number:"))

comp=random.randint(1,100)

while True:

    if dict2>comp:
        print("too high")
        break;
    elif dict2<comp:
        print("too low")
        break;
    else :
        print("equal")

        break;