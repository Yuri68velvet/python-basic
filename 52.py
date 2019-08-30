class Calculation1:
    def Summation(self,a,b):
        return a+b;

# class Calculation2:
#     def Multiplication(self,a,b):
#         return a*b;


# class Derived(Calculation1,Calculation2):
#     def Divide(self,a,b):
#         return a/b


# d=Derived()
# print(d.Summation(10,20))
# print(d.Multiplication(10,20))
# print(d.Divide(10,20))



class Calculation1:
    def Sum(self,a,b):
        return a+b;
class Calculation2:
    def Multiply(self,a,b):
        return a*b;

class Devided(Calculation1,Calculation2):
    def Divide(self,a,b):
        return a/b

x=Devided()
print(x.Sum(1,2))
print(x.Multiply(1,2))
print(x.Divide(1,2))