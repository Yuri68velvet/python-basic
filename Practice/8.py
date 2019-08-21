list=[1,2,3,4,5,6,7]
count=1
for i in list:
    if i==4:
        print('item matched')

        count=count+1
        break
print('found at location')
print(count)

list=[1,2,3,4,5,6,7]
count=2
for i in list:
    if i==5:
        print('present')

        count=count+3
    
print('found at location')
print(count)


print('-------------------')

for x in range(6):
    print(x)
for x in range(6,10):
    print(x)
for x in range(6,20,2):
    print(x)

print('------------------------')
family=['naoki','keiko','yuri','takato']

for name in family:
    print(name)
for xyz in family[0:1]:
    print(xyz)

family_age=[18,21,49,52]

for age in family_age:
    if age>20:
        print(age)

boxes=['red','white','red','white','pink','blue']

for team in boxes[2:6]:
    if team=='red':
        print(f'This is Team,{team}')
    elif team=='white':
        print(f'This is Team,{team}')
    else:
        print(f'This Team is pink or blue')

for word in 'python':
    if word=='p':
        print(word)
        break
    print(f'hello{word}')
    print('The end')

print('---------------------------')
for word in 'python':
    if word=='p':
        print(f'hello{word}')
        continue
    print(f'hello{word}')

sounds=['fan','chair','myself']

for sound in sounds[1:]:
    if sound=='chair':

        print(f'{sound}-hello')
    elif sound=='myself':
        print('its', sound)

    else:
        print(sound)

animals=['dog','cat','rabbit','zebra']
for animal in animals:
    if animal=='dog':
        print(f'{animal} is-inu')
    elif animal=='cat':
        print(f'{animal} is-cat')
    elif animal=='rabbit':
        print(f'{animal} is-usagi')
    elif animal=='zebra':
        print(f'{animal} is-shimauma')

print('-----------------------')

number=int(input('Enter the number: '))

fac=1

for i in range(1,number+1):
        fac=fac*i
print("factorial of this ",number,"is",fac)

color=["red","white","orange","green"]
clothes=['skirt','pants','jacket','coat']

for x in color:
    for y in clothes:
        print(x,y)

print('--------------------------------')

for num in range(3,20,3):
    quotient=i/3
    print(f'{i} devided by 3 is {int(quotient)}')

print('-----------------------------')
number=int(input("Enter the number"))

for score in range(6,18,2):
    print(number,'+',score,'=',number+score)

for i in range(3,16,3):
    quotient=i/3
    print(f"{i} divided by 3 is {int(quotient)}.")

for i in range(5,50,5):
    quotient=i/10
    print(f'{i} divided by 5 is {int(quotient)}')

print('---------------------------------')

list_tohoku=[5349,5478,4644,4968,6259]

for val in list_tohoku:
    print(val)

avg_tohoku=0
for val in list_tohoku:
    avg_tohoku+= val

avg_tohoku/=len(list_tohoku)
print(avg_tohoku)

print('-------------------------------')
list_shikoku=[3148,2991,2966,2457]


for val in list_shikoku:
    print(val)

avg_shikoku=0
for val in list_shikoku:
    avg_shikoku+= val

avg_shikoku/=len(list_shikoku)
print(avg_shikoku)


