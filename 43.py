def mynames(*names):
    print('type of the arguments',type(names))

    print("printing the passed arguments")


    for name in names:
        print(name)

mynames("lohit","john","smith","sfhou")
