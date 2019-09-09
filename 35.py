def person(dictionary):
    belts=list(dictionary.values())

    for belt in belts:
        num=belts.count(belt)

        print(f'there are {num}{belt} belts')

lohit_items={}

while True:
    lohit_program=input('Enter the name of belt')
    lohit_frame=input('Enter belt name with color')

    lohit_items[lohit_program]=lohit_frame

    another=input('Add one more y/n:')

    if another=='y':
        continue
    else:
        break

person(lohit_items)

