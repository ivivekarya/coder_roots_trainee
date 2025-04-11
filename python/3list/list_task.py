#Create a list of 10 number and print the list

li=[1,2,3,4,5,67,78,66,64,22]
print(li)
print(len(li))


# Q2. Create a list [1,10,100,3,6,8] and add 59 on 3 location after
# that append 5 and print list and length of list

li1=[1,10,100,3,6,8]
li1.insert(3,59)
print(li1)
li1.append(5)
print(li1)
print(len(li1))


# Q3. create a list of 10 elements and print all elements are even
# locations
# Example:
#     x = [1,4,2,42,4,6,2,56,4,56,2]
#     Result is: 1 2 4 6 56 56
x = [1,4,2,42,4,6,2,56,4,56,2]

print(x[::2])




# Q4. create a list with values ["Gaurav",12,23,33.33,"Sharma",True]
# and print only elements which are string


li3=["Gaurav",12,23,33.33,"Sharma",True]


for i in li3:
    if type(i)==str: 
        print(i)


# Q5. add all the number present in above list

sum=0
for i in li3:
    if type(i)==float or type(i) == int:
        sum=sum+i 
print(sum)   

# Q6. Create a list with 5 friends and ask user a friend name and
# add that name in the friend list,
# and print the list
# after that ask user to most important friend and add that friend
# at user choice


frnd=["mota","billa","raju","amba","nikka"]

add=input("enter a friend name:")
frnd.append(add)
print(frnd)

dd=input("enter best friend name:")
frnd.append(dd)
ad=int(input("enter the location of best friend:"))

frnd[ad]=dd
print(frnd)


# Ex: [1,2,3,4,5]
# -> Enter anothe fiend: Raju
# [1,2,3,4,5,"Raju"]
# --> Most import afiedn: Billa
# --> Please location for billa: 1
# [1,"Billa",3,4,5,"Raju"]

