class Tire:
    def __repr__(self):
        return 'A rubber tire'


class Frame:
    def __repr__(self):
        return 'An aluminum frame'


class CarbonFiberFrame:
    def __repr__(self):
        return 'A carbon fiber frame'


class Bicycle:
    def __init__(self, front_tire, back_tire, frame):  # <1>
        self.front_tire = front_tire
        self.back_tire = back_tire
        self.frame = frame

    def print_specs(self):
        print(f'Frame: {self.frame}')
        print(f'Front tire: {self.front_tire}, back tire: {self.back_tire}')


if __name__ == '__main__':
    bike = Bicycle(Tire(), Tire(), Frame())  # <2>
    bike.print_specs()

    bike = Bicycle(Tire(), Tire(), CarbonFiberFrame())  # <1>
    bike.print_specs()  # <2>
