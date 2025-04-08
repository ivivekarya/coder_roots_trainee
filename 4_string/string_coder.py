#Strings 
# str1="Gurminder"

# print(len(str1))


# str1= input("Enter String ")
# print(str1)
# print(type(str1))

st1= "hello how are you"

print(st1.capitalize()) #Return a capitalized version of the string.
print(st1.title()) #Return a version of the string where each word is titlecased.
print(st1.upper()) # upper case 
print(st1.lower()) # lower

print(st1.swapcase()) 

a="     hi     "
print(a.strip()) # remove extra spaces left or right
print(a.lstrip()) # remove extra spaces from left
print(a.rstrip()) # remove extra spaces from right

# st1= st1.replace('o','n')
# print(st1)
print(st1.replace('ow','n'))

print("------------")
print(st1)
print(st1.split('o'))

print(st1.count('o'))
print(st1.find('o')) # if word is repeated then it takes first occurence

# for i in st1:
#     print(i)

#slicing 
print("----------------")
print("----------------")

naam="CODER ROOTS"
print(naam[:])
print(naam[:7]) # start stop step 
print(naam[2:8]) # start stop step 
print(naam[::-1])
print(naam[::2])
print(naam[::-2])
print(naam[5:1:-1])