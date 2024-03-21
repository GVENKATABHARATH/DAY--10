# DAY -10

# Method  Over-riding
# Polymorphism in classes

# Eg:1
class bank:
    def ratio(self):
        print("All banks has repo rate")

class SBI(bank):
    def ratio(self):
        print("SBI rate is 9%")

class IOB(bank):
    def ratio(self):
        print("IOB rate is 7.5%")

i = IOB()
i.ratio()

s = SBI()
s.ratio()

# Eg:2

class USA:
    def language(self):
        print("English")

    def capital(self):
        print("washington DC")

class India(USA):
    def langauge(self):
        print("None")

    def capital(self):
        print("New delhi")

I = India()
I.langauge()
I.capital()

# Eg:3
#Polymorphism using objects

# c1, c2 --> c1 = print(c1),print(c2)

# f1,f2

class c1:
    def f1(self):
        print("class 1")

class c2(c1):
    def f1(self):
        super().f1()
        print("class 2")

obj1 = c2()
obj1.f1()

#Eg: 4
class c1:
    def f1(self):
        print("class 1")

class c2(c1):
    def f1(self):
        super().f1()
        print("class 2")

obj1 = c2()
obj2 =c1()

def display(a):
    a.f1()
display(obj1)
display(obj2)

# changing the functionality of builtin functions

class shooping:
    def __init__(self, l1):
        self.items = l1

    def __len__(self):
        length = len(self.items)
        return length

s = shooping([1,2,3,4,5])
print(len(s))


# !---> Method overloading
# Eg:1
class suming:
    def add(self, a,b,c):
        print(a+b+c)
s = suming()
s.add(4,5,1)
    

# Eg:2
class suming:
    def add(self, a=None, b=None, c=None):
        if a!=None and b!=None and c!=None:
            print(a+b+c)
        elif a!=None and b!=None:
            print(a+b)
        else:
            print(a)

obj = suming()
obj.add(2)
obj.add(3,4)
obj.add(1,2,3)
    

# !-----> Abstractions
# The process of hiding the implimentation

#? Eg:1

# from abc import ABC, abstract method
# @abstractmethod
class shapes():
    def sides(self):
        print('All shapes have sides except circle')

class triangle(shapes):
    def triangle_sides(self):
        print("3 sides")
    def name(self):
        print("Iam triangle")

    def sides(self):
        pass

class square(shapes):
    def square(self):
        print("4 sides")

tr = triangle()
tr.triangle_sides()
tr.name()

# !Rules to define abstract class 1

# 1.)Abstract class cnnot be instantined
# 2.)From abc import ABC, abstractmethd
# 3.)subclass the normal class with ABC
# 4.)convert the normal method inside the abstract class to abstract method
# 5.)All the child classes have to be subclassed with abstract class
# 6.)The abstract method should be present in the child classes


# Eg:2
# super() ---> used to access the parent class method from child class method
#from abc import ABC, abstractmethod

class c1:
    def m1(self):
        print("This is abstract class")

class c2(c1):
    def m2(self):
        super().m1()
        print("I am child 1")

    def m1(self):
        pass
        

class2 = c2()
class2.m2()

# Eg:3
#from abc import ABC, abstractmethod
class password:
   # @abstractmethod
    def pwd(self):
        pswd = "Bharath1994$"
        return pswd

class login(password):
    def validate(self,name, password):
        if super().pwd() == password:
           print("Welcome", name,'!!')
           print("Login Successfull")
        else:
           print("Please check the password")
        def pwd(self):
            pass

Login = login()
name = input("Enter the name: ")
pwd = input("Enter the password: ")
Login.validate(name, pwd)



# ! Encapsulation
class car:
    name = "BMW" # privite variable

c1 = car()
print(c1.name)
c1.name = "Audi"
print(c1.name)

# Eg:2
# Accessing privite date outside the class
class c1:
    ___phone = '8790845607'


    def display(self):
        print(self.__phone)
c = c1()
c.display()


# --> Eg:3
# ?decleare privite method
class class1:
    def __m1(self):
        print("Iam privite method")

    def ___init__(self):
        self.___m1()
c=class1()


# Nested class
class class1:
    class class2:
        name = "bharath"

        def display(self):
            print(self.name)
obj1 = class1()
print(obj.obj1.name)
obj.obj1.display()
        
d1 ("shirt":1000, "pant": 1500, "Shoes": 900, "handkey": 30
for val in d1:
if d1 [val] = min(d1.values());
print(val)
for val in d1:
if d1 [val] max(d1.values()):
print(val)
for val in d1:
if val.startswith('s') or val.startswith('S'): print(val)c









##a = 9
##b = 6
##print(a+b)
##print(a.__add__(b))#? dunder method or mafic method
##
##int()
##print(a.__sub__(b))
##
##

















#) Tasks
#Write the code for the below tasks using function
#!)>d1 = {"shirt": 1000, "pant"; 1500, "Shoes"; "900", "handkey": 30}
#a.) Find the min ans max priced product
#b.) Find the product starts with 's' and 'S'

#2.) Find then 67, is strong number or not

#3.) 11 [1,2,3,4,5,6]
#n=2> [5, 6, 1,2,3,4]
#n=3--> [4,5,6, 1,2,3]
