# Given a tuple, write a Python function to remove all 
# duplicate elements and return a new tuple.  
tup=(1,1,2,3,4,56,8,96,6,4,56,2,8)

elements=tuple(set(tup))
print(elements)
#   Write a list comprehension to flatten a 2D list into a 1D list
#               Input: [[1, 2], [3, 4], [5, 6]] → Output: [1, 2, 3, 4, 5, 6]

flat=[item for sublist in [[1, 2], [3, 4], [5, 6]] for item in sublist]

print(flat)
# Write a Python program to find the maximum 
# and minimum elements in a tuple.
# Input: (3, 5, 1, 8, 2) → Output: Max: 8, Min: 1

Inp=(3, 5, 1, 8, 2)
print("max: ",max(Inp))
print("min: ",min(Inp))


# Create a list of tuples using list comprehension,
# where each tuple contains a number and its cube for numbers from 1 to 5.

# tp=[1,2,3,4,5]
rr=[(tp,tp**3) for tp in  range(1,6)]
print(rr)