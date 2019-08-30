class yuri:
    program='python'
    def Function(self):
        print("This is a message iniside the class.")


first=yuri()

print(first.program)

second=yuri()

second.program='php'
print(second.program)


third=yuri()
third.program='django'
print(third.program)