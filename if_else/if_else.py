cel= input("Enter Temperature ")

cel= float(cel)

fah= (cel*9/5)+32

print(fah,"°F")


#Conditional Statements if , else, elif 

a=int(input("Enter any number "))

if a>20: 
    print("a is greater than 20")
elif a==20:
    print("a is equal to 20")
else:
    print("a is smaller ")
    
marks=int(input("Enter marks "))

if marks>=90 and marks<=100:
    print("A++")
elif marks>=80 and marks<90:
    print("A")
elif marks>=70 and marks<80:
    print("B")
elif marks>=60 and marks<70:
    print("C")
elif marks<60:
    print("Fail")
else:
    print("Enter valid marks")
    
    
    
if marks>=90:
    if marks>100:
        print("Enter valid marks")
    else:
        print("A++")



#Looping statements

for i in range(0,11):  # start stop 
    print(i)
    
    
for i in range(7):  # start default to 0, need to mention only stop
    print(i)



for i in range(0,20):
    # if i%2!=0:
    #     print(i)
    if i%3==0:
        print(i)

# for i in range(1,20,4):
#     print(i)

# for i in range(20,1,-1):
#     print(i)
# for i in range(20,1,-3):
#     print(i)