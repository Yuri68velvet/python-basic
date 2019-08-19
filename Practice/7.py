#practice list
list=['naoki','keiko','yuri','takato']

print(list)
print(list[0:1])
print(list[2])
print(list*2)

#practice tuple
tuple1=('yuri',21,'f')
tuple2=('keiko',49,'f')
tuple3=(tuple1+tuple2)

print(tuple3)

print(len(tuple3))

#practice dictionaly

country_code={'America':1,'Itary':39,'China':86,'India':91}
print(country_code)
print(country_code.keys())
print(country_code.values())

print(81 in country_code)
print('America' in country_code)

country_code[81]='Japan'
print(country_code)

country_code[1]='USA'
print(country_code)


#practice if

height=float(input('Enter your height: '))
print(height)
weight=float(input('Enter your weight: '))
print(weight)

bmi=int(weight)/float(height)**2
print('Your BMI is{:.1f}'.format(bmi))


if bmi<18.5:
    print('You are skinny')
elif 18.5<=bmi<25.0:
    print('You are normal')
elif 25.0<=bmi<30.0:
    print('You are fat')
else:
    print('You are obesity')
