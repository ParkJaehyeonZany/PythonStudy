import random

class Dice:

    def __init__(self):
        self.face = 0
    def roll(self):
        self.face = random.randint(1, 6)
        return self.face

def main():
    print('주사위 값 :', Dice().roll())

if __name__ == '__main__':
    main()