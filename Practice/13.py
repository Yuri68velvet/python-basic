
# x=int(input('Enter the number1:'))
# y=int(input('Enter the number2:'))
# z=int(input('Enter the number3:'))

# if x>y>z:
#     print(x,y,z)
# elif x>z>y:
#     print(x,z,y)
# elif y>x>z:
#     print(y,x,z)
# elif y>z>x:
#     print(y,z,x)
# elif z>x>y:
#     print(z,x,y)
# elif z>y>x:
#     print(z,y,x)

# n=int(input('Enter the number'))
# fac=1
# for n in range(1,n+1):
#     fac=fac*n
#     if n==25:
#         print(fac)

# x=int(input('Enter the number:'))

# n=str('■'*x)

# print(n)

# n=int(input('Enter the number:'))
# x=1

# for n in range(1,n+1):
#     x=x*n
#     i='■'*(n+1)
#     print(i)

# counter=0
# sum=0
# data=int(input('Enter the data:'))
# while data>=0:
#     counter+=1
#     sum+=data
#     data=int(input('Enter the data:'))
# avg=sum/counter

# print('data=',counter,'sum=',sum,'avg=',avg)


# lent=int(input('How much did you lend?'))
# add=float(input('Enter the add:'))
# pay=int(input('How much will you pay?'))
# total=0
# month=0
# while lent>pay:
#     month+=1
#     lent=lent*(1+add/12/100)-pay
#     print(str(month)+'(m):pay：￥',pay,'left:￥',int(lent),sep='')
#     total+=pay
# month+=1
# lent=lent*(1+add/12/100)
# print(str(month)+'month:paid￥',int(lent),\
#     'You have paid all ￥','total:￥',\
#     int(total),sep='')


# print('--------------------------------')

# print("Please pick one:rock sessors paper")

# while True:
#     game={'rock':0,'scissors':1,'paper':2}
#     user_1=str(input('your name:'))
#     user_2=str(input('Your name:'))
#     u1=game.get(user_1)
#     u2=game.get(user_2)
#     dif=u1-u2

#     if dif in []:
#         print('user_1 wins')


# x='rock'
# y='sissors'
# z='paper'

# if x==x or y==y or z==z:
#     print('drow')
#     continue
# elif x

# x=1
# for x in range(1,101):

#     if x%3==0 and x%5==0:
#         print('FizzBuzz')
#     elif x%5==0:
#         print('Buzz')
#     elif x%3==0:
#         print('Fizz')
#     else:
#         print(x)

# meal={'breakfast':'dosa','lunch':'meals','dinner':'momos'}

# for foods in meal:
#     print(foods)

# print('--------------------------------------')
# for foods in meal.values():
#     print(foods)




def rank(dictionary):
    for key,val in dictionary.items():
        print(f'you are:{key}Your score is:{val}')


player={}
while True:
    name=(input('Enter your name:'))
    score=int(input('Enter your score'))

    
    player[name]=score
    
    
    anything=input('Do you want to add more info?(y/n):')

    if anything=='y':
        continue
    else:
        break

rank(player)

    