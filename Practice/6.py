age=int(input('How old are you?: '))
if age>20 or age==20:
    print('You can drink alcohol')
elif age<20:
    print('You cannot drink alcohol')

food=input("Do you eat meat? Yes/No: ")
if food!='Yes':
    print('You are vegitarian')
else:
    print('You are non-vegitarian')

restaulant=input("How about the food? ")
if restaulant!='Tasty':
    print('Bad restaulant')
else:
    print('Good restaulant')



x=20
 
if x < 50 :
    print('(first suite)')
    print('x is small')
    print('x is small')
    
else:
    print('(second suite)')
    print('x is large')

x=100
 
if x < 50 :
    print('(first suite)')
    print('x is small')
    print('x is small')
    
else:
    print('(second suite)')
    print('x is large')

size=int(input('Enter your foot size:'))

if size<=23:
    print('Your size is S')
elif size<=25 and size>23:
    print('Your size is M')
elif size<=27 and size>25:
    print('Your size is L')
else:
    print('You donot have suitable shoes')

name=input('Enter your name: ')
if name=='Yuri':
    print('Hello Yuri!')
elif name=='lohit':
    print('Hello lohit!')
else:
    print('Nice to meet you!',name)

marks=int(input('Enter your score: '))
if marks<=100 and marks>=80:
    print('Congratsrations!You got A')
elif marks<=79 and marks>=60:
    print('Goodjob!You got B')
elif marks<=59 and marks>=40:
    print('Just a little more! You got C')
else:
    print('Work hard!You are fail')
