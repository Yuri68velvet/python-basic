
# def families():
#     families=0
#     sum_family_age=0
#     list=families
#     print(list)

# def family_data(families):
#          for key,val in families.items():
#               print(f'{key} is {val} old.')
            

# families={}
# while True:
#     family_name=(input('Enter your family name:'))
#     family_age=(input('Enter your family age:'))
    
#     families[family_name]=family_age

#     another=(input('Do you want to add more member?:'))

#     if another=='y':
#         continue

#     else:
#         break

# print(families)

# # family_data(families)
# print('---------------------------------------------------')


# def average_age(dictionary):
#     family=list(dictionary.values())

#     print(family)
#     x=sum(family)/len(family)
#     print(x)

# print('----------------------------------------------------')
# family_data={}

# while True:
#     family_name=input('Enter your family name')
#     family_age=int(input('Enter your family age'))

#     family_data[family_name]=family_age

#     another=input('add another family data?')

#     if another=='y':
#         continue
#     else:
#         break

# average_age(family_data)

# print('----------------------------------------------')



# list=[1,2,3,4,5,6]

# for num in list:
#     if  num==2:
#         print(f'Hello {num}')
#         continue
#     else:
#         print(f'Bye{num}')


# size=int(input('Enter your height:'))

# if size>=175:
#     print('Your size is L')

# elif 165<=size<175:
#     print('Your size is M')
# elif 150<=size<165:
#     print('Your size is S')
# else:
#     print('Your size is kids size')

def highschool(dictionary):
    students=list(dictionary.values())

    for number in students:
         num=students.count(number)

         print(f'There are {num}{number} students')



school={}

while True:
    grade=input('How old are you?:')
    if 15<=grade<=16:
        print('You are 1st grade')
    elif 17<=grade<=18:
        print('You are 2nd grade')
    elif 18<=grade<=19:
        print('You are 3rd grade')
    
    course=input('Are you select science or arts?s/a:')
    if course=='s':
        print('Your classroom is 2nd floor')

    elif course=='a':
        print('Your classroom is 3rd floor')

