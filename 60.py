class planet:


    shape='squre'

    def __init__(self,water,moon):
        self.water=water
        self.moon=moon
    
    def orbit(self):
        return f'{self.water}and satelite is {self.moon}'


    @classmethod
    def commons(cls):
        return f'all the planets are {cls.shape}'

naboo=planet('yes','moon is not present')

print(planet.shape)

print(planet.commons())


