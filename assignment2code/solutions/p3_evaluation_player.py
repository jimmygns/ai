# -*- coding: utf-8 -*-
__author__ = 'Dan'
__email__ = 'daz040@eng.ucsd.edu'

from assignment2 import Player, State, Action


class EvaluationPlayer(Player):
    def move(self, state):
        """Calculates the best move after 1-step look-ahead with a simple
        evaluation function.
        :param state: State, the current state of the board.
        :return: Action, the next move
        """

        # *You do not need to modify this method.*
        best_value = -1.0

        actions = state.actions()
        if not actions:
            actions = [None]

        best_move = actions[0]
        for action in actions:
            result_state = state.result(action)
            value = self.evaluate(result_state, state.player_row)
            if value > best_value:
                best_value = value
                best_move = action

        # Return the move with the highest evaluation value
        return best_move

    def evaluate(self, state, my_row):
        """
        Evaluates the state for the player with the given row
        """
        myStones = 0.0
        opponentStones = 0.0
        for i in range(len(state.board)):
            if my_row == 0:
                if i <= State.M:
                    myStones += state.board[i]
                else:
                    opponentStones += state.board[i]
            else:
                if i <= State.M:
                    opponentStones += state.board[i]
                else:
                    myStones += state.board[i]
        return (myStones - opponentStones)/(2*State.M*State.N)
