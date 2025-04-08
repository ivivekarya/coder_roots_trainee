li=[12,56,'hi',True, 88.9]
print(li)
print(type(li))

print(li[1])

# mutable
li[2]='Hello'

print(li)

# li.pop() # by default it removes last element
# li.pop(3)
# print(li)

# li.remove(56)
# print(li)


# li.append(45)
# li.append([45,44])
# print(li)

li.extend([44,33,67])
print(li)

li.insert(2,[43,55,78])
print(li)


# access
print(li[2][1])

li1=[11,23,5,7,87,56,89,5]
li1.sort()
print(li1)


# li.clear()
# print(li)

print(li1.count(5))
print("-----for----")

# for i in li:
#     print(i)


print(len(li))

for i in range(len(li)):
    print(li[i])
    

# Slicing 
print("------------------")
print("------------------")
print("------------------")
li2=[67,89,45,33,12,34,90]
print(li2)    

# start stop step [::]

print(li2[:5])
print(li2[1:7])
print(li2[2:6])
print(li2[3:])
print(li2[::])
print(li2[::2])
print(li2[0:5:3]) 

print(li2[::-1])
print(li2[:5:-1])
print(li2[5:1:-1])
