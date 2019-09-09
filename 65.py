#list comprehensions

#normal way to get output

numbers=[2,3,4,5,5,7,7]

double=[]
for number in numbers:
    double.append(number*2)

print(double)

double.append(number*2 for number in numbers)
print('This is comp way',double)