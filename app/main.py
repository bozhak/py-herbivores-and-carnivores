class AliveList(list):
    def __str__(self):
        return "[" + ", ".join(
            f"{{Name: {i.name}, Health: {i.health}, Hidden: {i.hidden}}}" for i in self
        if i.health > 0) + "]"

class Animal:
    alive = AliveList()

    def __init__(self, name, health: int = 100, hidden: bool = False):
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other):
        if not isinstance(other, Carnivore) and not other.hidden and other.health > 0:
            other.health -= 50


lion = Carnivore("Lion")
Parrot = Herbivore("Parrot")


lion.health = 0
#
# Parrot.hide()
# Parrot.hide()
#
# lion.bite(Parrot)
# lion.bite(Parrot)
print(Animal.alive)