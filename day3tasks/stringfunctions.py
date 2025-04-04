#day3 task string functions
st="my name is kusuma and i'm currently undergoing revature training program"
#len() function
print(len(st))

#upper() 
print(st.upper())

#lower()
print(st.lower())

#captilize()
print(st.capitalize())

#title()  it converts to uppercase  of each word in sentence
print(st.title())

#count function counts the no of times the character/word appears 
print(st.count('i'))

#endswith() 
print(st.endswith('m'))

#startswith()
print(st.startswith('m'))

#join()
mystr= "John Peter Vicky"
x = "#".join(mystr)
print(x)

#replace()
print(st.replace('my','mine'))

#split()
txt = "apple banana cherry orange"
x = txt.split(" ")
print(x)

#strip()
text="    revature    "
print(text.strip())

#find() and index() they find the first occurrence and returns position of a value from string the only difference between them is find() return -1 if value not found meanwhile index() gives error substring not found

print(st.find('a'))
print(st.find('z'))

print(st.index('a'))
print(st.index('z'))   


