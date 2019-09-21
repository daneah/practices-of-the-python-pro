class BigCat:
    def eats(self):
        return ['rodents']


class Lion(BigCat):  # <1>
    def eats(self):
        return ['wildebeest']
        # return super().eats() + ['wildebeest']  # cooperative version


class Tiger(BigCat):  # <2>
    def eats(self):
        return ['water buffalo']
        # return super().eats() + ['water buffalo']  # cooperative version


class Liger(Lion, Tiger):  # <3>
    def eats(self):
        return super().eats() + ['rabbit', 'cow', 'pig', 'chicken']


if __name__ == '__main__':
    lion = Lion()
    print('The lion eats', lion.eats())
    tiger = Tiger()
    print('The tiger eats', tiger.eats())
    liger = Liger()
    print('The liger eats', liger.eats())
