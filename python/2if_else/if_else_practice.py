# age=int(input("enter your age:"))

# if age>=18:
#     print("you are eligble")
#     print("you can vote")
# elif age<18:
#     print("wait until 18")
#     print("then vote")

# else:
#     print("fuck you bitch!")


#lets build a child
# In Python, if and else statements are used for decision-making.
#  They allow a program to execute different blocks of code depending on whether a condition is True or False.

v=int(input("enter first number: "))
b=int(input("enter second number: "))

operator=input("enter your operator(+,-,*,/,%): ")


if operator== "+":
    print(v+b)
elif operator=="-":
    print(v-b)
elif operator=="*":
    print(v*b)
elif operator=="/":
    print(v/b)
elif operator=="%":
    print(v%b)

else:
    print("enter a valid number")
