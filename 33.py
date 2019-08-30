#global functions in python

name='Yuri'
student='lohit'

def names():
    global student
    student='lohit Badiger'
    print('the person is',student)

names()

print('grobal names are',name)
print('grobal names are',student)

# x=30
# y=40

# def ans():
#     global x,y 
#     ans=x*y
#     print(ans)

# ans()