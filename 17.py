#For loops in python used for lists

students=['lohit','yuri','yuki','kotaro']

#print(student)
#print(student[1])
#print(student[2])
#print(student[3])

for stu in students:
    print(stu)

print('--------------------------')
#slice in for loop

for xyz in students[1:4]:
    print(xyz)

print('-----------------for lohit-----------------------')
boxes=['lohit','rohit','ken','lohit','lohit','chihiro']

for box in boxes[0:5]:
    if box=='lohit':
        print('lohit is',box)
    else:
        print('these are not lohit',box)

print('--------------------------')

boxes=['lohit','rohit','ken','lohit','lohit','chihiro']

for box in boxes[0:5]:
    if box=='lohit':
        print(f'{box}-say hello')
    else:
        print('these are not lohit',box)

print('--------------------------')

for val in 'yuripython':
    if val=='p':
        print(f'hello {val}')

print('--------------------------')

for val in 'yuripython':
    if val=='p':
        break
    print(f'hello {val}')
print('the end')

print('------------------------')
for val in 'yuripython':
    if val=='p':
        continue
    print(f'hello {val}')
print('the end')

print('---------------------------')

for val in "string":
    if val =="i":
        continue
    print(val)

print("The end")

print('-----------------------')

sounds=['fan','chair','myself']

for sound in sounds[1:]:
    if sound=='chair':

        print(f'{sound}-hello')
    elif sound=='myself':
        print('its', sound)

    else:
        print(sound)

list=[1,2,3,4,5,6,7]
count=1
for i in list:
    if i==4:
        print('item matched')

        count=count+1
        break
print('found at',count,"location")


for x in range(6):
    print('print',x)

for x in range(6,20):
    print('print',x)
for x in range(6,50,2):
    print('print',x)

# i want to find out the values of factorial 

number=int(input('Enter the number to find the factorial of'))

fac=1

for i in range(1,number+1):
    fac=fac*i
print("facorial of this ",number,"is",fac)

print('-----------------------')
# nested
adj=["red","big","tasty"]
fruits=['apple','banana','cherry']

for x in adj:
    for y in fruits:
        print(x,y)

print('--------------------------')

for i in range(3,16,3):
    quotient=i/3
    print(f"{i} divided by 3 is {int(quotient)}.")

number=int(input("Enter the number"))

for yuri in range(1,11):

    print("%d X %d=%d"%(number,yuri,number*yuri))

    # print(number,'X',yuri,'=',number*yuri)


