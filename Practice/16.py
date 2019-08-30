class human():

    def __init__(self,hand,leg):

        self.x=hand
        self.y=leg

    def part(self):

        x='right hand'
        y='left hand'
        print('part of the body',self.x)
        print('part of the body',self.y)


        print('this is own properties part',x)
        print('this is own properties part',y)

        xyz=100
        zxc=10
        print(xyz+zxc)
    
ok=human('right','left')
ok.part()

class person:

    def __init__(self,name,age,email):
        self.name=name
        self.age=age
        self.email=email

    def myfunc(self):
        print("Hello",self.name)

p1=person('yuri',21,'yuri@gmail.com')
p1.myfunc()



class member:
    def __init__ (self,name,date,age):
        self.name=name
        self.date=date
        self.age=age
    
    def members(self):
        print("Today is",self.date)

m1=member('Yuri','0608',21)
m1.members()


class bugs:
    def __init__(self,leg,touch):
        self.leg=leg
        self.touch=touch

    def bug(self):

        x='front'
        y='both side'
        print(self.leg,'are part of bugs body')
        print(self.touch,'are part of bugs body')

insect=bugs('legs','touches')
insect.bug()