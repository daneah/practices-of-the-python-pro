from abc import ABC, abstractmethod


class Predator(ABC):  # <1>
    @abstractmethod  # <2>
    def eat(self, prey):  # <3>
        pass # <4>


class Bear(Predator):  # <5>
    def eat(self, prey):  # <6>
        print(f'Mauling {prey}!')


class Owl(Predator):
    def eat(self, prey):
        print(f'Swooping in on {prey}!')


class Chameleon(Predator):
    def eat(self, prey):
        print(f'Shooting tongue at {prey}!')


if __name__ == '__main__':
    bear = Bear()
    bear.eat('deer')
    owl = Owl()
    owl.eat('mouse')
    chameleon = Chameleon()
    chameleon.eat('fly')
