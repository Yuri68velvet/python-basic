# class family():
#     def __init__ (self,name,age):
#         self.name=name
#         self.age=age
    
#     def daughter(self):
#         print('Father name is ',self.name)
#         print('Father age is ',self.age)

#         daughter='yuri'
#         print('my name is ',daughter)

# x=family('Naoki',52)
# x.daughter()

# class family():
#     name='naoki'
#     age=52

#     def father(self):
#         print('Fathers name is %s age is %d'%(self.name,self.age))

# member=family()
# member.father()


# class Student:
#     count=0
#     def __init__(self):
#         Student.count=Student.count+2

# s1=Student()
# s2=Student()
# s3=Student()
# s4=Student()

# print("The number of stundents:",Student.count)

# class add():
#     def __init__(self,name):
#         print('this is non parameter contructor',name)

#     def show(self,name):
#         print("hello",name)

# student=add('Yuri')
# student.show("mark")


# class Calculation1:
#     def Summation(self,a,b):
#         return a+b;

# class Calculation2:
#     def Multiplication(self,a,b):
#         return a*b;


# class Derived:
#     def Divide(self,a,b):
#         return a/b


# d=Calculation1()
# a=Calculation2()
# c=Derived()

# print(d.Summation(10,20))
# print(a.Multiplication(10,20))
# print(c.Divide(10,20))

# class Person1:
#     def __init__(mysillyobject,name,age,lohit):
#         mysillyobject.name=name
#         mysillyobject.age=age
#         mysillyobject.lohits=lohit


#     def myfunc(abc):
#         print("Hello my name is ",abc.lohits)

# p1=Person1("John",36,33)
# p1.myfunc() 



# class Person2:
#         def __init__(number,name,year,month):
#             number.a=name
#             number.b=year
#             number.c=month

#         def data(person):
#             print("You are",person.a,person.b)

# p2=Person2("Yuri",2019,8)
# p2.data()


# class Myclass:
#     variable="blah"

#     def function(self):
#         print("This is a message inside the class.")


# myobjectx=Myclass()
# myobjecty=Myclass()

# myobjecty.variable="yackity"

# #Then print out both values

# print(myobjectx.variable)
# print(myobjecty.variable)



# class members():
#     name='Yuri'
#     password='yuri68velvet'

#     def myfun(self):
#         print("name: %s \npassword: %s"%(self.name,self.password))

#     def myfun2(self):
#         print("name: %s \npassword: %s"%(self.name,self.password))

# myfun=members()
# myfun2=members()

# myfun2.name='Keiko'
# myfun2.password='keikoangel7'


# user=members()
# user.myfun()

class family():
    name='Naoki'
    age=52

    def parent(self):
        comment='my father is %s his age is%d'%(self.name,self.age)
        return comment
    def kids(self):
        comment='my brother is %s his age is%d'%(self.name,self.age)
        return comment


father=family()
son=family()


son.name='Takato'
son.age=18

father=family()
father.parent()

print(father.parent())
print(son.kids())


