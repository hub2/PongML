from enum import Enum
import pygame
from config import *
class Direction(Enum):
    UP = 1
    DOWN = 2
    NONE = 3

move_map = {
    pygame.K_w: Direction.UP,
    pygame.K_a: Direction.DOWN,
    pygame.K_p: Direction.UP,
    pygame.K_l: Direction.DOWN,
}
class Paddle:
    def __init__(self, rect=(0,0,10,10)):
        self.rect = rect

    def move(self, direction: Direction):
        tmp = list(self.rect)
        if direction == Direction.UP:
            tmp[1] += -paddle_speed
        elif direction == direction.DOWN:
            tmp[1] += paddle_speed
        else:
            pass
        self.rect = tuple(tmp)

    @property
    def y(self):
        return (self.rect[1]+self.rect[3])/2

