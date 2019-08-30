
# def multiply(a,b,c):
#     return a*b*c
# def ans(num):
#     print(multiply/num)

# a=int(input('Enter the numbera:'))
# b=int(input('Enter the numberb:'))
# c=int(input('Enter the numberc:'))

# ans(100)



# age=int(input('Enter your age:'))
# year=int(input('Enter the year:'))

# left=100-age
# ans=year+left

# print(ans)

born_year=int(input('Enter your born year:'))

answer=born_year+100

print(answer)

def pencase(dictionary):
    pencils=list(dictionary.values())

    for pen in pencils:
         num=pencils.count(pen)

         print(f'There are {num}{pen} pens')

pencil={}

while True:
    my_pencil=input('Enter the kind of your pencil:')
    pencil_color=input('Enter the pencil color:')

    pencil[my_pencil]=pencil_color

    another=input('Add the item?y/n:')

    if another=='y':
        continue
    else:
        break

pencase(pencil)