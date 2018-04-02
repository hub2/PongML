from config import *
class Ball:
    __slots__ = ["size", "pos", "direction"]
    def __init__(self, pos=(0,0)):
        self.pos = pos
        self.direction = (4,1.5)

    def move(self):
        self.pos = (self.pos[0] + self.direction[0], self.pos[1] + self.direction[1])

    def flip_direction_x(self):
        self.direction = (self.direction[0]*(-1), self.direction[1])

    def flip_direction_y(self):
        self.direction = (self.direction[0], self.direction[1]*(-1))


