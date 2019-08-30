#Variable length arguments:
#We can have both normal and keyword variable number of arguments.\n
# please see this for details.

#python pronglam to illustrate
# *args for variable number of arguments

def address(*argv):
    for arg in argv:
        print(arg)

address('lohit','hubli',89898993,"389HJsdjf")

address('lohit','fhfhosdhlfkv','bdjv',89989993,"hvufhvk",'hjkvsdb')






