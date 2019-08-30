def spiceup(dictionary):
    for key,val in dictionary.items():
        print(f'You are{key}and you take {val}course')
    #
spiceup_members={}
while True:
    name=(input('Enter members name:'))
    course=(input('Enter the course:'))

     #assignment[key]=[value]
    spiceup_members[name]=course
    extra=(input('Do you wanna add anything else?(y/n):'))
    if extra=='y':
        continue
    else:
        break

spiceup(spiceup_members)


print('==========================================')



def family_data(dictionary):
    for key,val in dictionary.items():
        print(f'You are {key} and your age is {val}')

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

