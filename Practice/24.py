class audition:
    name='yuri'
    age=21
    skills='sing a song'

    def entryno1(self):
        introduction=(f"I am {self.name} and {self.age} years old.and I am good at {self.skills}")
        return introduction

    def entryno2(self):
        introduction=(f"I am {self.name} and {self.age} years old.and I am good at {self.skills}.")
        return introduction

    def entryno3(self):
        introduction=(f"I am {self.name} and {self.age}  years old.and I am good at {self.skills}.")
        return introduction

person1=audition()
person2=audition()
person3=audition()

person2.name='biyonce'
person2.age=26
person2.skills='dancing'

person3.name='emmawatson'
person3.age=25
person3.skills='act'



print(person1.entryno1())
print(person2.entryno2())
print(person3.entryno3())