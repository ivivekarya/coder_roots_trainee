#1. Find all of the words in a string that are less than 4 letters
# user=input("enter a string:")
# short=[word for word in user.split() if len(word)<4]
# print(short)

# 2.Given numbers = range(20), produce a list containing the word ‘even’ 
# if a number in the numbers is even, and the word ‘odd’ if the number is odd. 
# Result would look like ‘odd’,'even',........

numbers = range(20)
v3=["even" if i %2==0 else "odd" for i in numbers]
print(v3)

# 3.Find all of the numbers from 1-1000 that are divisible by 7

v34=[i for i in range(1,1000) if i%7==0]
print(v34)
#4. Count the number of spaces in a string
# 5.Find the common numbers in two lists 
# (without using a tuple or set) list_a = 1, 2, 3, 4, list_b = 2, 3, 4, 5