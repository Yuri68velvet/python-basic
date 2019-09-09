# x={1,2,3,4}
# y={4,5,6,7}
# z=(x&y)
# print(z)

# x,y.add(8)
# print(x,y)

#family age average 
# dict={'yuri':21,'takato':17,'keiko':49,'Naoki':52}
# print(dict.keys())
# print(dict)
# print(dict.values())

family=[('naoki',52,'m'),('keiko',49,'f'),('yuri',21,'f'),('takato',17,'f')]
age=family[0][1]+family[1][1]+family[2][1]+family[3][1]
# print(age)
# print(age/4)

def average_age(family):
    sum_family_age=0
    for next_family in age:
        sum_family_age=sum_family_age+next_family[1]
        return sum_family_age/len(family)

print(average_age([('naoki',52,'m'),('keiko',49,'f'),('yuri',21,'f'),('takato',17,'f')]))

# family=['yuri','keiko','naoki','takato']
# for f in family:
#     print(f)

# integer=[1,2,3,4,5,6,7,8,9,10]
# ans=0;
# for i in integer:
#     if i%2==0:
#         print(i)
# print(ans)
