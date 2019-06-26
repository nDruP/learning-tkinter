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
    d = {4: Dice(4), 6: Dice(6), 8: Dice(8),
         10: Dice(10), 12: Dice(12), 20: Dice(20)}
    for x in d.keys():
        print(d[x].roll())
        print(d[x].roll(2))
        print(d[x].history)
