class human():


    def __init__(self,hand,leg):

        self.x=hand
        self.y=leg

    def part(self):

        #x='right hand'
       # y='left hand'
        print('part of the body',self.x)
        print('part of the body',self.y)

        #print('this is own properties part',x)
        #print('this is own properties part',y)


        #xyz=100
        #zxc=10
       # print(xyz+zxc)

ok=human('right','left')
ok.part()