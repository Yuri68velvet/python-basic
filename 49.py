class family():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def son(self):
        print('Father name is ',self.name)
        print('Father age is ',self.age)

        son='yuri'
        print('my name is ',son)

  

call=family('naoki',52)
call.son()

print('-----------------------------------------------')

class Employee:
    id=10
    name="john"
    def display(self):
        print("ID: %d \nName: %s"%(self.id,self.name))

    #this is instance

emp=Employee()
emp.display()

print('--------------------------------------------------')


class members():
    name='Yuri'
    password='yuri68velvet'

    def myfun(self):
        print("name: %s \npassword: %s"%(self.name,self.password))

user=members()
user.myfun()



















