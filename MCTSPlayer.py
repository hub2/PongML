from copy import deepcopy
from Paddle import Direction
from Game import Winner
import random
class MCTSPlayer:
    def __init__(self, player_number):
        self.player_number = player_number
        self.possible_moves = [Direction.UP, Direction.DOWN]
        self.max_moves = 200
    def get_move(self, game):
        number_of_sims = 300
        move_quality = []
        for possible_move in self.possible_moves:
            potential_game = deepcopy(game)

            won_sims = self.do_simulations(potential_game, number_of_sims)
            move_quality.append((possible_move, won_sims))


        sorted_by_best_score = sorted(move_quality, key=lambda x: x[1], reverse=True)
        print(sorted_by_best_score)
        if sorted_by_best_score[0][1] == sorted_by_best_score[1][1]:
            return Direction.NONE
        move = sorted_by_best_score[0][0]
        return move


    def do_simulations(self, game, number_of_sims):
        counter = 0
        for i in range(number_of_sims):
            who_won = self.do_simulation(deepcopy(game))
            if who_won == Winner.P2:
                counter += 1
        return counter

    def do_simulation(self, game):

        p1_move, p2_move = self.possible_moves[random.randint(0, 1)], self.possible_moves[random.randint(0, 1)]
        w = game.move(p1_move, p2_move)
        for i in range(self.max_moves):
            p1_move, p2_move = self.possible_moves[random.randint(0, 1)], self.possible_moves[random.randint(0, 1)]
            w = game.move(p1_move, p2_move)
            if w != Winner.NONE:
                break
            if game.b.direction[0] < 0:
                return Winner.P2
        else:
            return Winner.P2

        return w





