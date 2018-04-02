from GameState import GameState
from Paddle import Direction
from enum import Enum
import copy
from config import *
class Winner(Enum):
    P1 = 1,
    P2 = 2,
    NONE = 3

class Game:
    __slots__ = ["p1", "p2", "b", "size"]
    def __init__(self, p1, p2, b, size):
        self.p1 = p1
        self.p2 = p2
        self.b = b
        self.size = size

    def get_state(self):
        return GameState(self.p1.y, self.p2.y, self.b.pos, self.b.direction)

    def next_state(self, state, p1_move, p2_move):
        new_state = copy.copy(state)
        if p1_move == Direction.UP:
            new_state.p1_y += -paddle_speed
        elif p1_move == Direction.DOWN:
            new_state.p1_y += paddle_speed

        if p2_move == Direction.UP:
            new_state.p2_y += -paddle_speed
        elif p2_move == Direction.DOWN:
            new_state.p2_y += paddle_speed

        if abs(new_state.b_pos[1] - size[1]) <= ball_radius/2:
            new_state.b_dir = (new_state.b_dir[0], new_state.b_dir[1]*(-1))
        if abs(new_state.b_pos[1]) <= ball_radius/2:
            new_state.b_dir = (new_state.b_dir[0], new_state.b_dir[1]*(-1))

        if abs(p1_left_x + paddle_width - new_state.b_pos[0]) <= ball_radius/2 and \
                new_state.p1_y-(paddle_height//2) <= new_state.b_pos[1] <= new_state.p1_y + (paddle_height//2):
            new_state.b_dir = (new_state.b_dir[0]*(-1), new_state.b_dir[1])

        if abs(p2_left_x + paddle_width - new_state.b_pos[0]) <= ball_radius/2 and \
                new_state.p2_y-(paddle_height//2) <= new_state.b_pos[1] <= new_state.p2_y + (paddle_height//2):
            new_state.b_dir = (new_state.b_dir[0]*(-1), new_state.b_dir[1])

        new_state.b_pos = (new_state.b_pos[0] + new_state.b_dir[0], new_state.b_pos[1] + new_state.b_dir[1])

        return new_state

    def legal(self, state):
        if paddle_height/2 <= state.p2_y + paddle_speed <= size[1] - paddle_height/2 and \
                paddle_height/2 <= state.p2_y - paddle_speed <= size[1] - paddle_height/2:
            return [Direction.UP, Direction.DOWN, Direction.NONE]
        elif paddle_height/2 >= state.p2_y - paddle_speed:
            return [Direction.DOWN, Direction.NONE]
        elif state.p2_y + paddle_speed >= size[1] - paddle_height/2:
            return [Direction.UP, Direction.NONE]
        else:
            return []

    def winner(self, states):
        #for new_state in states:
        new_state = states[-1]
        if new_state.b_dir[0] < 0 or new_state.b_pos[0] <= 0:
            return Winner.P2
        elif new_state.b_pos[0] >= size[0]:
            return Winner.P1
        return Winner.NONE


    def move(self, p1_move, p2_move):
        self.p1.move(p1_move)
        self.p2.move(p2_move)

        if abs(self.b.pos[1] - self.size[1]) <= ball_radius/2:
            self.b.flip_direction_y()
        if abs(self.b.pos[1]) <= ball_radius/2:
            self.b.flip_direction_y()

        if abs(self.p1.rect[0] + self.p1.rect[2] - self.b.pos[0]) <= ball_radius/2 and \
                self.p1.rect[1] <= self.b.pos[1] <= (self.p1.rect[1]+self.p1.rect[3]):
            self.b.flip_direction_x()
        if abs(self.p2.rect[0] - self.b.pos[0]) <= ball_radius/2 and \
                self.p2.rect[1] <= self.b.pos[1] <= (self.p2.rect[1]+self.p2.rect[3]):
            self.b.flip_direction_x()

        self.b.move()

        if self.b.pos[0] <= 0:
            return Winner.P2
        elif self.b.pos[0] >= self.size[0]:
            return Winner.P1
        else:
            return Winner.NONE

