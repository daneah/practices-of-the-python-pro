class Tire:  # <1>
    def __repr__(self):
        return 'A rubber tire'


class Frame:
    def __repr__(self):
        return 'An aluminum frame'


class Bicycle:
    def __init__(self):  # <2>
        self.front_tire = Tire()
        self.back_tire = Tire()
        self.frame = Frame()

    def print_specs(self):  # <3>
        print(f'Frame: {self.frame}')
        print(f'Front tire: {self.front_tire}, back tire: {self.back_tire}')


if __name__ == '__main__':  # <4>
    bike = Bicycle()
    bike.print_specs()
