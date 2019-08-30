def names(dictionary):
    for key,val in dictionary.items():
        print(f'At spiceup{key} is handled to {val}')


assignment={}

while True:
    program=input("Enter the name of programming Language")

    student=input('Enter the name of the student')

    assignment[program]=student

    another=input('Do you want to add one more item(y/n)')
    if another=='y':
        continue
    else:
        break

names(assignment)

def lohit(dictionary):
       for key, val in dictionary.items():
      
        print(f'I know this  a {key} programing and this is  {val}, a framework of {key}')

lohit_items= {}
while True:
   lohit_program= input('enter name of programming')
   lohit_frame=input('enter the name of frame work')
   lohit_items[lohit_program]=lohit_frame
   another=input('add another program? (y/n)')
   if another=='y':
       continue
   else:
       break

lohit(lohit_items)

    