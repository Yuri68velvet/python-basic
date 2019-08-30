def myfun(x):
    
    #After below line link of x with previous
    #object gets broken.A new object is assigned
    #to x.
    x=20

#Driver Code(Note that x is not modified)
#after function call.

x=10
myfun(x);
print(x)