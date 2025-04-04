#List Functions
l1=['a','b','c']
#append()
l1.append('d')
print(l1)

#copy()
l2 = l1.copy()
print(l2)

#count()
print(l2.count('a'))

#extend
l2.extend('e')
print(l2)

#index
print("Index",l2.index('b'))

#insert
l2.insert(4,'f')
print(l2)
#pop
print(l2.pop(4))
#remove
print(l2.remove('c'))
print(l2)
#reverse
l2.reverse()
print(l2)
#sort
l2.sort()
print(l2)
#clear
l2.clear()
print(l2)