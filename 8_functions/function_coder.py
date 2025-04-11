
# Functions 
# Coder Roots
# •
# 30 Jan

# functions.py
# Text
# Class comments
# Material details
# user defined functions , pre defined functions -- input(), len()

# function bnaaye jaande aa with def keyword de naal 

# def func_name(paramters):
    # block of code 
    # -------------
    # -------------
    # block of code 
a=10
b=20
def sums():
    # a=10
    # b=20
    print("hello ")
    print(a+b)
    
# sums()


# function with arguments and parameter
# def add(i,j):
#     print(i+j)
    
#     return True

# function with return
def add(i,j):
    # a=i+j
    return i+j
    
# x=int(input("Enter x "))
# y=int(input("Enter y "))

# add(x,y)  # arguments

# n=add(x,y)
# print(n)

# def evenOdd(i):
#     if i%2==0:
#         return "Even"
#     else:
#         return "Odd"

# number= int(input("Check Number "))
# print(evenOdd(number))


# a='hi'
# b='hi'
# # print(a is b)
# print(id(a))
# print(id(b))

# i=input("Enter i ")
# j=input("Enter j ")
# print( i is j)
# print("----")
# print(id(i))
# print(id(j))

# keyword arguments 
# def answer(a,b,c):
#     print(a,b,c)


# # a=10
# # b=20
# # c=30
# # answer(b,a,c)
# answer(b=10,c=20,a=30)

def listSum(i):
    # print(i)
    sum=0
    for j in i:
        # print(j)
        sum+=j  #or sum=sum+j
        
    return sum
    
li=[23,45,32,55,67,89]
ans= listSum(li)
print(ans)