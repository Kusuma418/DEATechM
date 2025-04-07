#program for all types of inheritance
# Single Level Inheritance

class Animal():
    def food(self):
        print("Eat biscuits")
        
class Dog(Animal):
    def sound(self):
        print("Dog Barks")

a = Animal()
dog = Dog()
dog.food()
dog.sound()
a.food()

#Multi Level Inheritance

class House():
    def place(self):
     print("It is a place to live")
class kitchen(House):
    def place1(self):
     print("It is a place to cook")
class DiningHall(kitchen):
    def place2(self):
     print("It is a place to have food")
    
d = DiningHall()
d.place()
d.place1()
d.place2()

# Multiple Inheritance
class Animal:
    def sound(self):
        print("Animal makes a sound")
class Bird:
    def fly(self):
        print("Bird can fly")
# Child class inheriting from both Animal and Bird
class Bat(Animal, Bird):
    def info(self):
        print("I am a Bat")

# Create an object of Bat
b = Bat()
b.info()     # Output: I am a Bat
b.sound()    # Output: Animal makes a sound
b.fly()      # Output: Bird can fly


# Hierarchical Inheritance

class Animal():
    def sound(self):
        print("Animals makes sound")
        
class Dog(Animal):
    def barks(self):
        print("Dogs barks")
        
class Cat(Animal):  
    def meow(self):
        print("Cat Meow")

d = Dog()
c = Cat()

d.barks()
d.sound()
c.meow()
c.sound()      

# Hybrid Inheritance

class A:
    def method_a(self):
        print("Method from A")

class B(A):
    def method_b(self):
        print("Method from B")

class C:
    def method_c(self):
        print("Method from C")

class D(B, C):
    def method_d(self):
        print("Method from D")

d = D()
d.method_a()
d.method_b()
d.method_c()
d.method_d()


#OVERLOADING
class overloading:
    def Details(self,name=None,age=None):
        if name and age:
            print(f"name : {name}, age : {age}")
        elif name:
            print(f"name : {name}")
        else:
            print("No details provided")

s = overloading()
s.Details("Alice",25)
s.Details("Bob")
s.Details()

#OVERRIDING

class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("The dog barks")
    
class cat(Animal):
    def sound(self):
        print("The cat Meows")
        
A = Animal()
A.sound()

D = Dog()
D.sound()

C = cat()
C.sound()


#encapsulation for all modifiers
class person:
    def Details(self,name,age,salary):
        self.name = name
        self._age = age
        self.__salary = salary
    
    def info(self):
        print("Name :",self.name)
        print("Age :",self._age)
        print("Salary :",self.__salary)
        
    def getSalary(self):
        return self.__salary
    
    def setSalary(self,Salary):
        self.__salary = Salary
        
P = person()
P.Details("Kusuma Indla",21,50)
P.info()
print("GetSAlary:",P.getSalary())
P.setSalary(500)
P.info()


#polymorphism
class Circle:
    def area(self):
        print("Area = π *r * r")

class Rectangle:
    def area(self):
        print("Area = length * width")

class Triangle:
    def area(self):
        print("Area = 0.5 * base * height")

def print_area(shape):
    shape.area()


c = Circle()
r = Rectangle()
t = Triangle()

print_area(c) 
print_area(r)   
print_area(t)