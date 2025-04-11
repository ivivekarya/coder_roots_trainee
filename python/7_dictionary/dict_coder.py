 #key value pair, {}, key and value -- data type 
# {key:value,key:value __ __}

dict1={'name':'Gurminder', 'class':'btech'}
print(dict1)
print(type(dict1))

d={'name':'arshvir','class':'btech','rollno':23,'isownapet':True,12:'Yes'}
print(d)

#access
# print(d['name'])
# print(d['class'])
# print(d['names'])

# print(d.get('names','Not Present'))  # not raises error if key is not present 

user= input("Enter Key ")
print(d.get(user))

print("hello")

d['rollno']=45
print(d)

d.update(rollno=44)
print(d)

d.pop(12)
print(d)


d['pankaj']='late aunda'
print(d)

print(d.keys())
print(d.values())
print(d.items())


for i in d.keys():
    print(i)
for i in d.values():
    print(i)
for i,j in d.items():
    print(i,'==',j)
    

details={
    'Name':{
        'First Name':'Pankaj',
        'last Name':'Mehra'
    },
    'Address':{
        'Permanent Address':'Hoshiarpur',
        'Temp Add':'Mohali'
    },
    'College':'Rayat Bahra Hoshiarpur',
    'Data':[12,45,67]
}

print(details)
print(details['Name'])
print(details['Name']['last Name'])

print(details['Data'][1])