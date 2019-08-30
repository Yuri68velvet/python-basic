# def greeting():
#     print('Hello')

# greeting()
# greeting()

# def selfintroduction():
#     print('My name is Yuri')

# greeting()
# selfintroduction()

# def exam(subject,score):
#     print(f'Your {subject} score is {score}')

# exam('math','45')
# exam('english','55')

# def member(name='yuri',task='clerical'):
#     print(f'{name} is in charge of {task}')

# member()
# member('merumo','accountant')
# member('mari','leader')


# def calculate(a,b):
#     return a+b

# x=calculate(100,200)
# print(x)

# def area(radius):
#     return 3.14*radius*radius

# r=area(2)
# print(r)

# def area(upper,base,height):
#     return ((upper+base)*height)/2

# a=area(1,2,3)
# print(a)

list=[1,2,3,4,5]
flag=0

for i in list:
    print("current element:",i,end="\n");
    if i==3:
        pass;
        print("\n Came out of pass\n");
        flag=1;
    if flag==1:
        print("\nCame out of pass\n");
        flag=0;


