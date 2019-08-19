#Tuples

list=(1,2,3,4)

print(list)

#non mutable or not changeable
# list[2]='dodkk'
# print(list)

empty_tuple=()
print(empty_tuple)
#One way of creation
#Creating non-empty tuples

tuple='python','Yuri'
print(tuple)

#Another for doing the same

tuple=('python','Yuri')
print(tuple)

print('---------------------------')

yuri=(1,2,3,4,5)
add=('python','gtggg')
print(yuri+add)

print('---------------------------')
tuple1=(0,1,2,3)
tuple2=('python','geek')
tuple3=(tuple1,tuple2)
print(tuple3)

#Finding Length of a tuple
tup=('python','php')
print(len(tup))

my_tuple=('p','e','r','m','i','t')

print(my_tuple[0])
print(my_tuple[5])

print('----------------------------')


n_tuple=("mouse lohit",[8,4,6],(1,2,3,'Yuri'))
print(n_tuple)


#nested index
print(n_tuple[0][6:12])

print('--------------------------')

print(n_tuple[0][6])
print('---------------------------------')

print(n_tuple[1][1])
print('--------------------------------------')

print(n_tuple[2][3])

my_tuple=('p','r','o','g','r','a','m','i','z')
print(my_tuple[:-8])
print('---------------------------------------')

print(my_tuple[2:-6])

del n_tuple
#print(n_tuple)

multiple=(1,2,3)
print(multiple*3)




