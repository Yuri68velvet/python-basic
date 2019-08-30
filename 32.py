def area(radius):
    return 3.14*radius*radius

def volume(area,length):
    print(area*length)

radius=int(input('Enter the radius'))
length=int(input('Enter the length'))

volume(area(radius),length)