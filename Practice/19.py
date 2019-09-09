# class python():
#     name=""
#     age=""
#     month=""

#     def course1(stu):
#         comment=f'{stu.name} is {stu.age}old {stu.month}month take python course. '
#         return comment

#     def course2(stu):
#         comment=f'{stu.name} is {stu.age}old {stu.month}month take python course. '
#         return comment

#     def course3(stu):
#         comment=f'{stu.name} is {stu.age}old {stu.month}month take python course. '
#         return comment

# student1=python()
# student2=python()
# student3=python()

# student1.name='yuri'
# student1.age=21
# student1.month=3

# student2.name='kotaro'
# student2.age=20
# student2.month=5

# student3.name='yuki'
# student3.age=18
# student3.month=1

# print(student1.course1())
# print(student2.course2())
# print(student3.course3())

# print('--------------------------------')

# class bordingpass:

#     def __init__(self,name,number,seat):

#         self.name=name
#         self.number=number
#         self.seat=seat
#     def ticket1(self):
#         return f'{self.name} is----->{self.number},{self.seat}'
    
#     def ticket2(self):
#         return f'{self.name} is----->{self.number},{self.seat}'

#     def ticket3(self):
#         return f'{self.name} is----->{self.number},{self.seat}'

#     def ticket4(self):
#         return f'{self.name} is----->{self.number},{self.seat}'

# Yuri=bordingpass('Yuri Yasukawa',57,'aisle')

# print(f'Name:{Yuri.name}')
# print(f'Seat No.:{Yuri.number} {Yuri.seat} seat')
# print(Yuri.ticket1())


# Nae=bordingpass('Nae Iguchi',22,'window')
# print(f'Name:{Nae.name}')
# print(f'Seat No.:{Nae.number} {Nae.seat} seat')
# print(Nae.ticket2())


# Kota=bordingpass('Kota Yamada',66,'aisle')
# print(f'Name:{Kota.name}')
# print(f'Seat No.:{Kota.number} {Kota.seat} seat')
# print(Kota.ticket3())


# Fumiya=bordingpass('Fumiya Sato',32,'window')
# print(f'Name:{Fumiya.name}')
# print(f'Seat No.:{Fumiya.number} {Fumiya.seat} seat')
# print(Fumiya.ticket4())

# print('-----------------------------')

# class person1:

#     def __init__(self,id,password):
#         self.id=id
#         self.password=password
    
#     def myfunc(self):
#         print("Your ID : "+ self.id)

# p1=person1("yuri68velvet",21)

# del p1.id
# print(p1.id)

# class gym:
#     program='inhale'
#     def room1(self):
#         print("This is a message iniside the class.")


# first=gym()

# print(first.program)

# second=gym()

# second.program='battle'
# print(second.program)


# third=gym()
# third.program='voult'
# print(third.program)

# print('---------------------------------------')
# class exam:
#     subject='math'

#     def test1(self):
#         print("This is schedule of exam")

# first=exam()
# print(first.subject)

# second=exam()
# second.subject='english'
# print(second.subject)

# third=exam()
# third.subject='science'
# print(third.subject)

# print('------------------------------------------')

# class study():
#     exam='difficult'
#     def __init__(self,subject,score):
#         self.subject=subject
#         self.score=score

#     def test(self):
#         return "subject: %s ====> score: %d"% (self.subject,self.score) 

# instance1=study('japanese',80)

# print(f'The subject is{instance1.subject}')
# print(f'The score of this subject is {instance1.score}')
# print(instance1.exam)

# instance2=study('Spanish',70)

# print(f'The subject is{instance2.subject}')
# print(f'The score of this subject is {instance2.score}')
# print(instance2.exam)


# print(study.exam)

print('------------------------------------------------')
# class planet:
    

#     shape='squre'

#     def __init__(self,water,moon):
#         self.water=water
#         self.moon=moon
    
#     def orbit(self):
#         return f'{self.water}and satelite is {self.moon}'


#     @classmethod
#     def commons(cls):
#         return f'all the planets are {cls.shape}'

# naboo=planet('yes','moon is not present')

# print(planet.shape)

# print(planet.commons())

print('---------------------------------------')

# class animal:
#     type='animals'

    
#     def __init__(self,name,food):
#         self.name=name
#         self.food=food

#     def creature1(self):
#         comment1=f'{self.name} is eating {self.food}.'
#         return comment1

    
#     def creature2(self):
#         comment2=f'{self.name} is eating {self.food}.'
#         return comment2

#     @classmethod
#     def commons(anm):
#         print(f'They are all {anm.type}.')


# cornivore=animal('lion','meat')
# print(f'{cornivore.name} is eating {cornivore.food}.')

# hervivore=animal('zebra','grass')
# print(f'{hervivore.name} is eating {hervivore.food}.')


# print(animal.type)
# print(animal.commons())

print('------------------------------------')

# class planet:
    
#     country='Japan'


#     def __init__(self,city,place):

#         self.city=city
#         print('====================')

#     def waste(self):
#         return f'{self.city}--------------------'

#     @classmethod
#     def commons(yuri):
#         return f'{yuri.country}'

#     @staticmethod
#     def spin(speed='20000m/s speed'):
#         return f'Japan is not effected by {speed}'

# pass_value=planet('Tokyo','Osaka')

# print(planet.commons())

# print(planet.spin())

print('-------------------------------------')
# class space:
    
#     planet='earth'

#     def __init__(self,sea,continent):

#         self.sea=sea

#     def country(self):
#         return f'{self.continent}--------------'
#     @classmethod
#     def commons(cosmos):
#         return f'{cosmos.planet}'

#     @staticmethod
#     def area(surface='510.066*10km'):
#         return f'The surface of the earth is {surface}.'

# pass_value=space('Pacific ocean','Asia')
# print(f'There many islands in the {pass_value.sea}')

# print(space.commons())
# print(space.area())

print('--------------------------------------------')
class bonus:
    
    def __init__(self,name,grade,point):

        self.name=name
        self.grade=grade
        self.point=point

    def account(self):
        return '{} {}'.format(self.name,self.grade)

    def bonus_point1(self):
        self.point=int(self.point*5)
    
    def bonus_point2(self):
        self.point=int(self.point*2)

lohit=bonus('lohit','gold',50)
print(lohit.point)

lohit.bonus_point1()
print('lohit get the bonus point:',lohit.point)

yuri=bonus('yuri','silver',18)
print(yuri.point)

yuri.bonus_point2()
print('Yuri get the bonus point:',yuri.point)





