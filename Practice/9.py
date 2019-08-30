# num=1

# number=int(input('Enter the number'))

# while num<=1:
#     print(number,'X',num,'=',number*num)
    
#     num=num+1


# i=1

# number=int(input('Enter your number:'))

# while i<=10:
#     print(number,i,number*i)

#     i=i+1

# import random
# random.randint(0,9)

# rand_num=0
# while rand_num !=4:
#     rand_num=random.randint(0,9)
#     print(rand_num)

# while True:
#     rand_num=random.randint(0,9)
#     print(rand_num)
#     if rand_num !=4:
#         continue
#     else:
#         break

while True:
    height=(input('Enter your height:'))
    if len(height)==0:
        break
    print(f'your height is{height}')
    weight=(input('Enter your weight:'))
    print(f'your weight is{weight}')
    bmi=int(weight)/float(height)**2
    print(f'your BMI is{bmi:.1f}')

    if bmi<float(18.5):
        print('you are skinny')
    elif 18.5<bmi<=25.0:
        print('you are normal')
    elif 25.0<bmi<=30.0:
        print('you are fat')
    else:
        print('you are obesity')


    