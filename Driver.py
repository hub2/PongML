import pygame
from config import *
class Driver:
    def __init__(self, p1, p2, b, screen):
        self.p1 = p1
        self.p2 = p2
        self.b = b
        self.screen = screen

    def draw(self):
        pygame.draw.circle(self.screen, (255,255,255), [int(x) for x in self.b.pos], ball_radius)
        pygame.draw.rect(self.screen, (255,255,255), self.p1.rect)
        pygame.draw.rect(self.screen, (255,255,255), self.p2.rect)
