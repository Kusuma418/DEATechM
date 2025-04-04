#reverse a string and check for palindrome
st=input("enter a word: ")
rev=st[::-1]
if (st==rev):
    print("Given string is palindrome ")
else:
    print("Given string is not palindrome")
    
#also can be done by for loop