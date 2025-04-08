#Create a List of Squares of numbers from 1 to 10

li=[1,2,3,4,5,6,7,8,9,10]
square=[i**2 for i in li]
print(square)

# Create a List of Even numbers from 1 to 20
# Sample Output
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

li2=[i for i in range(0,20) if i %2==0]
print(li2)


# Generate a list of characters from a string
# Sample Output
# ['H', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']

vi="hello world"
vi2=[char for char in (vi)]
print(vi2)


# Create a list of lengths of words in a sentence
# Sample Output
# This is a sample sentence.
# [4, 2, 1, 6, 9]

w="This is a sample sentence."
print(len(w))
w1=w.split()
print(w1)

# lenth=[len(w1) for each(w1)]
# print(lenth)