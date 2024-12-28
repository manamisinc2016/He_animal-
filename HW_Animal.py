import random

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        new_z = self._cords[2] + dz * self.speed
        if new_z < 0:
            print("It's too deep, I can't dive :(")
        else:
            self._cords[0] += dx * self.speed
            self._cords[1] += dy * self.speed
            self._cords[2] = new_z

    def get_cords(self):
        print(f"X: {self._cords[0]} Y: {self._cords[1]} Z: {self._cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, I'm peaceful :)")
        else:
            print("Be careful, I'm attacking you 0_0")

    def speak(self):
        print(self.sound)

class Bird(Animal):
    beak = True

    def lay_eggs(self):
        eggs = random.randint(1, 4)
        print(f"Here are(is) {eggs} egg(s) for you")

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        dz = abs(dz)  # Ensure dz is positive
        new_z = self._cords[2] - dz * (self.speed / 2)
        if new_z < 0:
            print("It's too deep, I can't dive :(")
        else:
            self._cords[2] = new_z

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    sound = "Click-click-click"

# Example usage
db = Duckbill(10)

print(db.live)  # True
print(db.beak)  # True

db.speak()  # Click-click-click
db.attack()  # Be careful, I'm attacking you 0_0

db.move(1, 2, 3)
db.get_cords()  # X: 10 Y: 20 Z: 30

db.dive_in(6)
db.get_cords()  # X: 10 Y: 20 Z: 0

db.lay_eggs()  # Here are(is) X eggs for you (X - случайное число от 1 до 4)
