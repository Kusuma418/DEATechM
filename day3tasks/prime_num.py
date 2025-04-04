#check for prime number
num=4
c=0
for i in range(1,num+1):
    if num%i==0:
        c+=1
if c==2:
    print("given number is prime number")
else:
    print("given number is not prime number")

#another method
num=int(input("enter a number: "))
c=0
for i in range(2,num):
    if num%i==0:
        c+=1
if c>0 and num!=1:
    print("given number is prime number")
else:
    print("given number is not prime number")