#Insert a function that prints a greeting,and execute it on the name object:


class person:

    def __init__(self,name,id,adress):
        self.name=name
        self.id=id
        self.adress=adress


    def myfun(self):
        print("HELLO MY DEAR",self.name)

name=person("lohit",20,"India")


name.myfun()






# class person:

#     def __init__(self,name,age,email):
#         self.name=name
#         self.age=age
#         self.email=email

#     def myfunc():
#         print("Hello",self.name)

# p1=person('yuri',21,'yuri@gmail.com')

# p1.myfunc()






















