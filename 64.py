#I can use the classes
#Modules

#folder_name.file_name import class_name

from folder_name.classes import planet

naboo=planet('naboooo',123,2577)

print(f'name : {naboo.name}')

print(naboo.spin('a very high speed'))
print()

new=planet('lohit','new',23)

print(new.orbit())