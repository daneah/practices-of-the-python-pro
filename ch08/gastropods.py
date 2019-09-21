class Slug:
    def __init__(self, name):
        self.name = name

    def crawl(self):
        print('slime trail!')


class Snail(Slug):  # <1>
    def __init__(self, name, shell_size):  # <2>
        super().__init__(name)
        self.name = name
        self.shell_size = shell_size


def race(gastropod_one, gastropod_two):
    gastropod_one.crawl()
    gastropod_two.crawl()


race(Slug('Geoffrey'), Slug('Ramona'))  # <3>
race(Snail('Geoffrey'), Snail('Ramona'))  # <4>
