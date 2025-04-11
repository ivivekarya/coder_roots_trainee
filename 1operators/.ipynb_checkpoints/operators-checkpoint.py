#user input 

a= input("Enter your name: ")
print(a)
print(type(a))

b=input("Enter ")

print("value of b is",b)
print(type(b))


b=int(input("Enter "))

print("value of b is",b)
print(type(b))


i=input("Enter i ")
j=input("Enter j ")

print(i+j)



i=int(input("Enter i "))
j=int(input("Enter j "))
# operator
# ,//,%
print(i+j)
print(i-j)
print(i*j)
print(i/j)
print(i//j)
print(i%j)


# Assignment Operator =,+=,-=,/=,*=

x=10

x+=20  #--- x= x+20 -- 30

x-=10  # --- x=x-10 --- 20

x*=10  # x=x*10 -200

x/=10

print(x)



x=25
x+=10
x-=5
x*=10
x/=25

print(x)


# comparision operator ==,!=,>,<,>=,<= --- True or False 
print(23==45)
print(23!=50)
print(12>10)
print(11>=11)
print(44<100)


# Logical operators and or not -- True or False 


print(True or True)
print(True or False)
print(False or False or True)

print(True and True and False and True)


print(11>12 or 12>15)

print(15<16 and 16<90 and 55<90)

# Membership operators in, not in -- True or False
naam="Gurminder"

print('mid' in naam)
print('mid' not in naam)


# identity operator -- is , is not

a=10
b=20

print(a is b)
print(a is not b)

a="yes"
b="yes"
print(a is b)
