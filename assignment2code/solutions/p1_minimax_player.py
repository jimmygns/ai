# -*- coding: utf-8 -*-
__author__ = 'Dan'
__email__ = 'daz040@eng.ucsd.edu'

from assignment2 import Player, State, Action

class Node(State,Player):
    def __init__(self):
        self.state=State
        if Player==state.Player:
            self.untility=-2
        else:
            self.untility=2
        

class MinimaxPlayer(Player):
    def __init__(self):
        self.cache ={}

    def move(self, state):
        for new_action in state.action:
            if minimax(state.result(new_action)) == 1:
                return new_action
        for new_action in state.action:
            if minimax(state.result(new_action)) == 0:
                return new_action
        return state.action[0]


    def minimax(self, state):
        board = state.board
        if state._is_terminal:
            return state.untility
        if state.Player == Player:
            value=-2
            for new_action in state.action:
                new_utility = minimax(state.result(new_action))
                if new_utility > value:
                    value=new_utility
            return value
        else:
            value=2
            for new_action in state.action:
                new_utility = minimax(state.result(new_action))
                if new_utility < value:
                    value=new_utility
            return value




        """
        Calculates the best move from the given board using the minimax
        algorithm.
        :param state: State, the current state of the board.
        :return: Action, the next move
        """
        raise NotImplementedError("Need to implement this method")