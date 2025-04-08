# sets -- {}, unordered, heterogenous, unique elements

a={15,67,True,15,89,98,67,'hello'}
print(a)

a.add('hi')
print(a)

a.update((12,45,67)) # tuple, list, set
print(a)

a.remove(67)  
print(a)
# Remove an element from a set; it must be a member.
# If the element is not a member, raise a KeyError.
print("---------")
print(a)


a.discard(44)
# Remove an element from a set if it is a member.
# Unlike set.remove(), the discard() method does not raise an exception when an element is missing from the set.

print(a)

a.pop()  #randomaly remove a random member from set 
print(a)
a.pop()
print(a)


b={1,2,3,4}
c={2,3,6,5}

print(b.union(c))#  2 sets ko jodta hai bina duplicate keee


print(b.intersection(c)) # 2 se jada sets ka common element nikalta hai

b.clear() # sara kuch saaf krr deta hai
print(b)

d=set()
print(type(d))

d.add(12)
print(d)

