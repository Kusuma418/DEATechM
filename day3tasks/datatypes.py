str="my name is kusuma"
print(type(str))
print(str[1])
print(str[2])
print(str[-1])

rev=""
for i in str:
    rev=i+rev
print(rev)

#list
lst=[1,2,3]
print(type(lst))
print(lst[-1])
print(lst[-2])

#set
s1=set()
s1=set("hello revature welcomes you")
print("set with string:",s1)
s2=set(["hello", "hello", "hii", "hi"])
print("set with list:",s2)

#slicing
st="kusuma"
print(st[2::1])
print(st[::-1])

#frozenset
#immutable version of set


#dictionary
dict={"name":"Kusuma","age":21,"city":"Kurnool"}
print(type(dict))
print(dict["name"])
print(dict["age"])
print(dict["city"])

#bytes
b=[65,66,67]
print(b)
c=bytes([65,66,67])
print(c)

#none 
x=None
print(type(x))

#arrays
import array
numbers = array.array('i', [3, 1, 4, 1, 5, 9])
numbers_sorted = sorted(numbers)
print(numbers_sorted)