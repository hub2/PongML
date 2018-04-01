class GameState:
    __slots__ = ["p1_y", "p2_y", "b_pos", "b_dir"]

    def __init__(self, p1_y, p2_y, b_pos, b_dir):
        self.p1_y = p1_y
        self.p2_y = p2_y
        self.b_pos = b_pos
        self.b_dir = b_dir



