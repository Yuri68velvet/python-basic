class planet:

    country='Japan'


    def __init__(self,city,place):

        self.city=city
        print('====================')

    def waste(self):
        return f'{self.city}--------------------'

    @classmethod
    def commons(yuri):
        return f'{yuri.country}'

    @staticmethod
    def spin(speed='20000m/s speed'):
        return f'Japan is not effected by {speed}'

pass_value=planet('Tokyo','Osaka')

print(planet.commons())

print(planet.spin())