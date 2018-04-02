from GameState import GameState
from Paddle import Direction


class SimplePlayer:
    def __init__(self, game):
        self.last_state = game.get_state()
    def update(self, state : GameState):
        self.last_state = state
    def get_move(self):
        if self.last_state.b_pos[1] > self.last_state.p1_y:
            return Direction.DOWN
        elif self.last_state.b_pos[1] < self.last_state.p1_y:
            return Direction.UP
        else:
            return Direction.NONE
