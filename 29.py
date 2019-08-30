# def myfun2(x):
#     x[0]=120
#After below line link of x with previous
#object gets broken.A new object is assigned
#to x.
    # x=[20,30,40]

#Driver Code(Note that lst is not modified)
#after function call.

# lst=[10,11,12,13,14,15]
# myfun2(1)
# print(1)

# def myfun2(x):
#     x[0]=120
    
#     lst=[10,11,12,13,14,15]
#     myfun2(1)
# print(1)

def myfun(x):
    x=10
    
    myfun(x);
    print(x)

