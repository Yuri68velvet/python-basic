class Future:

    fun='very happy'
        #creating a class level object
    def __init__(self,name,age,game,system):
        self.name=name
        self.age=age
        self.game=game
        self.system=system

    def orbit(self):
        return f'{self.name}is->>>>>>>>{self.age}'

instance=Future('lohit',22,'baseball','liner-system')

print(f'Name is :{instance.name}')
print(f'Age is :{instance.age}')
print(f'Game is :{instance.game}')
print(f'System is :{instance.system}')

first=Future('Yuri',21,'baseball','liner-system')

print(f'Name is :{first.name}')
print(f'Age is :{first.age}')
print(f'Game is :{first.game}')
print(f'System is :{first.system}')
print(first.fun)


#Im writing "class_name".'variable_name'
print(Future.fun)

#Im writing "instance_name".'variable_name'
print(instance.fun)

