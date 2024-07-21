class Robot:
    def __init__(self, n, c, w):
        self.name = n
        self.color = c
        self.weight = w

    def introduce_self(self):
        print("My name is " + self.name)


r1 = Robot("Troy", "Black", 75)
r2 = Robot("Mega", "Red", 90)

r1.introduce_self()
r2.introduce_self()


class Person:
    def __init__(self, n, p, i):
        self.name = n
        self.personality = p
        self.is_sitting = i

    def sit_down(self):
        self.is_sitting = True

    def stand_up(self):
        self.is_sitting = False


p1 = Person("Alice", "aggressive", False)
p2 = Person("Becky", "talkative", True)

p1.robot_owned = r1
p2.robot_owned = r2
p1.introduce_self()
p2.introduce_self()

