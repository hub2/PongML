from copy import deepcopy
from math import log, sqrt

from Paddle import Direction
from Game import Winner
import random, datetime
import operator
class MCTSPlayer:
    def __init__(self, player_number, calculation_time, game, **kwargs):
        self.game = game
        self.player_number = player_number
        self.calculation_time = datetime.timedelta(seconds=calculation_time)
        self.max_moves = 150
        self.states = []
        self.wins = {}
        self.plays = {}
        self.C = kwargs.get('C', 1.4)
        self.max_depth = 0

    def update(self, state):
        self.states.append(state)

    def get_move(self):
        self.max_depth = 0
        state = self.states[-1]

        games = 0
        begin = datetime.datetime.utcnow()
        while datetime.datetime.utcnow() - begin < self.calculation_time:
            self.run_simulation()
            games += 1
            #print(len(self.plays))
            #print(len(self.wins))

        moves_states = [(p, self.game.next_state(state, Direction.NONE, p)) for p in self.game.legal(state)]

        print (games, datetime.datetime.utcnow() - begin)

        percent_wins, move = max(
            ((self.wins.get(S, 0) / self.plays.get(S, 1), p) for p, S in moves_states), key=operator.itemgetter(0))
        for x in sorted(
            ((100 * self.wins.get(S, 0) /
              self.plays.get(S, 1),
              self.wins.get(S, 0),
              self.plays.get(S, 0), p)
             for p, S in moves_states),
            reverse=True, key=lambda x: x[0]
        ):
            print ("{3}: {0:.2f}% ({1} / {2})".format(*x))

        print ("Maximum depth searched:", self.max_depth)
        if percent_wins < 0.0001 or all([x==100 for x in [(self.wins.get(S, 0)/self.plays.get(S, 1)) * 100 for p, S in moves_states]]):
            return Direction.NONE
        return move

    def run_simulation(self):
        plays, wins = self.plays, self.wins
        visited_states = set()
        states_copy = self.states[:]
        state = states_copy[-1]

        expand = True
        for t in range(1, self.max_moves + 1):
            moves_states = [(p, self.game.next_state(state, Direction.NONE, p)) for p in self.game.legal(state)]
            if all(plays.get(S) for p, S in moves_states):
                # If we have stats on all of the legal moves here, use them.
                log_total = log(
                    sum(plays[S] for p, S in moves_states))
                value, move, state = max(
                    (((wins[S] / plays[S]) +
                     self.C * sqrt(log_total / plays[S]), p, S)
                    for p, S in moves_states), key=operator.itemgetter(0)
                )
            else:
                # Otherwise, just make an arbitrary decision.
                move, state = moves_states[random.randint(0, len(moves_states)-1)]

            states_copy.append(state)

            if expand and state not in self.plays:
                expand = False
                self.plays[state] = 0
                self.wins[state] = 0
                if t > self.max_depth:
                    self.max_depth = t

            visited_states.add(state)
            winner = self.game.winner(states_copy)
            if winner != Winner.NONE:
                break
        for state in visited_states:
            if state not in self.plays:
                continue
            self.plays[state] += 1
            if winner == Winner.P2:
                self.wins[state] += 1





"""
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
 """
