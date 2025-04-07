li1= [23,56,55,43,44,78]

print(li1[:4:2])
print(li1[::-1])
print(li1[4:1:-1])


# list comprehension 
li=[23,43,22,11,45]
print(li)
li2=[]
for i in li:
    li2.append(i+2)
print(li2)

li=[i+2 for i in li]
print(li)


li1= [i for i in range(1,20)]
print(li1)


li2= [i for i in range(1,25) if i%2==0]


for i in range(1,25):
    if i%2==0:
        print(i)
    else:
        print(i**2)
li2= [i if i%2==0 else i**2 for i in range(1,25)]
print(li2)

li1=[2,3,4,5,6]
li2=[3,5,6,7,8,3]

li3= []
for i in li1:
    for j in li2:
        if i==j:
            li3.append(i)
        
print(li3)

li=[i for i in li1 for j in li2 if i==j]
print(li)



# List_21.py
# Displaying List_21.py.
# List Comprehension 
# Coder Roots
# •
# 22 Jan (Edited 22 Jan)

# List_21.py
# Text
# Class comments

# Add class comment…