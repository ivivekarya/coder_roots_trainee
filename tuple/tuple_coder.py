# tuple-- () imutable cannot change indexed ordered
#heterogenours
a=(12,True,'hello',9.90)
print(a)
print(type(a))

b=(12,)
print(type(b))

print(a.count(12))
print(a.index(9.90))

print(a[:])
print(a[1:])

print(a[2])
# a[2]="hi"-- imutable

print(a)

a=list(a)
# print(a)
a[2]='hi'

# print(a)
a=tuple(a)
print(a)

for i in a:
    print(i)