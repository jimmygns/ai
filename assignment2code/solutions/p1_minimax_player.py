# -*- coding: utf-8 -*-
__author__ = 'Dan'
__email__ = 'daz040@eng.ucsd.edu'

from assignment2 import Player, State, Action


        

class MinimaxPlayer(Player):
    def __init__(self):
        self.cache ={}

    def move(self, state):
        for new_action in state.actions():
            if self.minimax(state.result(new_action)) == 1:
                return new_action
        for new_action in state.actions():
            if self.minimax(state.result(new_action)) == 0:
                return new_action
        return state.actions()[0]


    def minimax(self,state):
        
        if state.is_terminal():
            return state.utility(self)
        if state.player == self:
            value=-2
            for new_action in state.actions():
                new_utility = self.minimax(state.result(new_action))
                if new_utility > value:
                    value=new_utility
            return value
        else:
            value=2
            for new_action in state.actions():
                new_utility = self.minimax(state.result(new_action))
                if new_utility < value:
                    value=new_utility
            return value


        """
        Calculates the best move from the given board using the minimax
        algorithm.
        :param state: State, the current state of the board.
        :return: Action, the next move
        """