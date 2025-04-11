#functions- args- arbitrary arguments, kwargs- keyword arbitrary arguments

# def summ(a,b):
#     print(a+b)
# *args
# def summ(*a):
#     print(a)
#     sum=0
#     for i in a:
#         sum+=i
        
#     print(sum)

# # summ(12,13,45)
# # summ((12,13,45))

# summ(12,34,56)
# summ(12,14,15,18,90,89)

def answer(**a):
    print(a)
    s=0
    for i in a.values():
        s+=i
        
    return s
    
# answer(b=10,a=20,c=30)
# answer(b=10,a=20,c=30,d=40)
# print(answer(b=10,a=20,c=30,d=40,e=33))

# Global and local variable


# i=10
# print("Value before function",i)

# def check():
#     global i
#     i=20
#     print("Value in function",i)

# check()

# print("Value after function",i)


#lambda function, single line function, anonymous

#syntax 

# def sum(a,b):
#     print(a+b)
# odd= lambda a,b: a+b return
# odd= lambda a,b: print(a+b)
# odd(12,11)

# oddEven=lambda a: "Even" if a%2==0 else "odd"
# i=int(input('Enter Number '))
# print(oddEven(i)) 
# functions_2.py
# Displaying functions_2.py.
# args, kwargs, lambda functions
# Coder Roots
# •
# 4 Feb

# functions_2.py
# Text
