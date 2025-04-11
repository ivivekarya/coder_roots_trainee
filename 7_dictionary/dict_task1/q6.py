#Q6 WAP to insert values value in the list
#li=[20,30,40,[57,66,30,[70,80],"Hello"],50,True]
#Add value 76 before 80
#Add value 88 after 57
#print the letter H from the list li

li=[20,30,40,[57,66,30,[70,80],"Hello"],50,True]
print(li)
print(li[3])
print(li[3][3])

li[3][3].insert(1,76)
print(li)
li[3].insert(1,88)
print(li)

print(li[3][5][0])