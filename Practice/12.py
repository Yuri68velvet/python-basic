
n=int(input('Enter the number:'))
i=1

for i in range(10):
    x=i*n
    i=i+1
    print(x)
print('-----------------------------------------')
N=4

while N<=4:
    if N==4:
        x='*'*N
        break
print(x)

print('----------------------------------------')
x=int(input('Enter your remain:'))
i=x
while x<3000:
    print(input('Do you want to charge?(y/n):'))
    i=x+10000
    if x=='yes':
        continue    
    else:
        break

print(i)

print('----------------------------------------')

def total_score(dictionary):
    for key,val in dictionary.items():
        print(f'Your {key} score is {val}') 

exam={}

while True:
    subject=(input('Enter your subject:'))
    score=(input('Enter your score:'))

    exam[subject]=score

    another=(input('Do you want to add?:(y/n)'))
    
    if another=='yes':
        continue
    else:
        break

print('---------------------------------------')
family=[('yuri',21),('naoki',52),('keiko',49),('takato',18)]

def average_age(family):
    sum_familyage=0

    for familyage in family:
        sum_familyage=sum_familyage+familyage[1]
    
    return sum_familyage/len(family)
    
print(average_age([('yuri',21),('naoki',52),('keiko',49),('takato',18)]))


def family_data(dictionary):
    for key,val in dictionary.items():
        print(f'You are {key} and your age is {val}')

total_score(exam)

family={}

while True:
    name=(input('Enter your family name:'))
    age=(input('Enter your familys age:'))

    family[name]=age

    anything=(input('Do you have anything else about your family?'))

    if anything=='yes':
        print('Please add your family member')
        continue
    else:
        break

family_data(family)


x=int(input('Enter the number:'))
a=x/(3.6)
print(a)


money=int(input('Enter your money:'))
print(f'You have {money} yen')

a=money//10000
money=money%10000
print(a)

b=money//5000
money=money%5000
print(b)

c=money//1000
money=money%1000
print(c)

d=money//500
money=money%500
print(d)

e=money//100
money=money%100
print(e)

f=money//50
money=money%50
print(f)

g=money//10
money=money%10
print(g)

h=money//5
money=money%5
print(h)

i=money//1
money=money%1
print(i)