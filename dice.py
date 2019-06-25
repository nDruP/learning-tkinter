from random import randint


class Dice:
    def __init__(self, faces):
        self.faces = faces
        self.history = []

    def roll(self, num_rolls=1):
        for _ in range(num_rolls):
            roll_result = randint(1, self.faces)
            self.history.append(roll_result)
        return self.history[-1*num_rolls:]

if __name__ == '__main__':
    d4 = Dice(4)
    d20 = Dice(20)
    print(d4.roll(12))
    print(d20.roll(12))
    print(d4.roll())
    print(d20.roll())
    print(d4.history)
    print(d20.history)
