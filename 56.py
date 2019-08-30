#how to use init function

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
print(f'Name is:{lohit.age}')
print(f'Name is:{lohit.game}')

print(lohit.orbit())
print('--------------------------------------')

Nae=planet('Nae',22,'dance','macOs')

print(Nae.name)
print(Nae.age)
print(Nae.system)

naboo=planet('fgfd',666,'game of thrones','Mac Os')

takuma=planet('takuma',32,23,'Android')
print(f'name is {takuma.name}')
print(f'name is {takuma.age}')
print(f'name is {takuma.game}')
print(takuma.orbit())


yuri=planet("yuri",21,23,'Php')

print(f'name is {yuri.name}')
print(f'name is {yuri.age}')
print(yuri.orbit())
