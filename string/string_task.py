# Write a Python program to get a string made of the first 2 and the last 2
#  chars from a given a string. If the string length is less than 2,
#  return ‘not a valid string’ instead of the empty string
# Sample string: - “Coder roots”
# Expected result - “cots”
# Sample string - “New year”
# Expected result - “near”

sttr=input("enter a string: ")

if len(sttr)<2:
    print("enter a valid string")
else:
    a=sttr[:8:2]
    # b=sttr[-2:]

    print(a)
# Write a Python program to get a single string from two given strings, 
# separated by a space and swap the first characters of each string
# Sample String : 'coder', 'roots'
# Expected Result : 'roder coots'

str_1=input("enter 1st string:")
str_2=input("enter 2nd string:")

a=str_2[0]+str_1[1:]
b=str_1[0]+str_2[1:]

print(a,"",b)
# Write a Python program to add 'ing' at the end of a given string 
# (length should be at least 3). If the given string already ends with 'ing'
#  then add 'ly' instead. If the string length of the given string 
# is less than 3, leave it unchanged
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'

strr3=input("enter a string:")

if len(strr3)<3:
    print(strr3)
elif strr3.endswith("ing"):
    print(strr3+"ly")

else:
    print(strr3+"ing")



# Write a Python program to remove the nth index character from a 
# nonempty string

strrr4=input("enter a string:")
indx=int(input("enter a index number:"))

# i want to apply slicing on a string

