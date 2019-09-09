# class Vehicle():
#     name="Fir"
#     kind="car"
#     color="red"
#     value=100.00

#     def description1(self):
#         desc_str="%s is a %s %s worth $%.2f." %(self.name,self.color,self.kind,self.value)
#         return desc_str

#     def description2(self):
#         desc_str="%s is a %s %s worth $%.2f." %(self.name,self.color,self.kind,self.value)
#         return desc_str

#     def description3(self):
#         desc_str="%s is a %s %s worth $%.2f." %(self.name,self.color,self.kind,self.value)
#         return desc_str

# car1=Vehicle()       
# car2=Vehicle()    
# car3=Vehicle()

# car1.name="Fir"
# car1.kind="car"
# car1.color="red"
# car1.value=100.00

# car2.name="jump"
# car2.color="blue"
# car2.kind="van"
# car2.value=60.00

# car3.name="speed"
# car3.color="pink"
# car3.kind="truck"
# car3.value=90.00

# print(car1.description1())
# print(car2.description2())
# print(car3.description3())

print('----------------------------------------')
class planet:
    
    def __init__(self,name,age,game,system):
        self.name=name
        self.age=age
        self.game=game
        self.system=system

    def orbit(self):
        return f'{self.name} is-------> {self.age}'

#lohit is ine instance
lohit=planet('lohit',23,'counter strike','windows')

print(f'Name is :{lohit.name}')
print(f'Age is:{lohit.age}')
print(f'Game is:{lohit.game}')

print(lohit.orbit())
print('--------------------------------------')

Nae=planet('Nae',22,'dance','macOs')

print(f'Name is :{Nae.name}')
print(f'Age is:{Nae.age}')
print(f'Game is:{Nae.game}')

print(Nae.orbit())

print('--------------------------------------')
Naboo=planet('Naboo',666,'game of thrones','Mac Os')

print(f'name is {Naboo.name}')
print(f'Age is {Naboo.age}')
print(f'Game is {Naboo.game}')
print(Naboo.orbit())

