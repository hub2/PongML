import sys, pygame, time

from MCTSPlayer import MCTSPlayer
from Paddle import Paddle
from Ball import Ball
from Driver import Driver
from Game import Game, Winner
from Paddle import Direction, move_map
from SimplePlayer import SimplePlayer
from config import *

pygame.init()

screen = pygame.display.set_mode(size)
b = Ball(pos=(width//2, height//2))
p1 = Paddle(rect=(p1_left_x, p1_top_y, paddle_width, paddle_height))
p2 = Paddle(rect=(p2_left_x, p2_top_y, paddle_width, paddle_height))
d = Driver(p1, p2, b, screen)
g = Game(p1, p2, b, size)

def draw():
    screen.fill(black)
    d.draw()

last_p1 = Direction.NONE
last_p2 = Direction.NONE
m_player = MCTSPlayer(1, 0.1, g)
s_player = SimplePlayer(g)
k = 0
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_w, pygame.K_a]:
                #last_p1 = move_map[event.key]
                pass
            elif event.key in [pygame.K_p, pygame.K_l]:
                #last_p2 = move_map[event.key]
                pass

    draw()
    if k%20 == 0:
        m_player.update(g.get_state())
        s_player.update(g.get_state())
        last_p2 = m_player.get_move()
        last_p1 = s_player.get_move()
        winner = g.move(last_p1, last_p2)
        if winner != Winner.NONE:
            sys.exit(0)
        last_p1 = Direction.NONE
        last_p2 = Direction.NONE


    k+=1
    pygame.display.flip()
