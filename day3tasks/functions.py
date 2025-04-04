#create a function userdetails and get details from user
def Userdetails():
    name = input("Enter the name : ")
    age = int(input("Enter Your Age :"))
    location = input("Enter your Location : ")
    return name,age, location

a,b,c = Userdetails()
print(f"Name:{a} age:{b} location:{c}")

#another method using arguments
def userdetails(name,age,location):
    return name,age,location

a,b,c=userdetails("Kusuma",22,"Kurnool")
print(f"Name:{a} age:{b} location:{c}")