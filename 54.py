class Myclass:
    variable="blah"
    
    def function(self):
        print("This is a message inside the class.")


myobjectx=Myclass()
myobjecty=Myclass()

myobjecty.variable="yackity"
#Then print out both values

print(myobjectx.variable)
print(myobjecty.variable)


