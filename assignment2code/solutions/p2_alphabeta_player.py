# -*- coding: utf-8 -*-
__author__ = 'Dan'
__email__ = 'daz040@eng.ucsd.edu'

from assignment2 import Player, State, Action

class AlphaBetaPlayer(Player):
    def __init__(self):
        self.cache={}
    
    def move(self, state):
        """Calculates the best move from the given board using the minimax
        algorithm with alpha-beta pruning and transposition table.
        :param state: State, the current state of the board.
        :return: Action, the next move
        """
    
        def alpha_beta_search(state):
            value=-2
            for new_action in state.actions():
                current_utility = MIN_value(state.result(new_action), -100, 100)
                if(current_utility>value):
                    best_utility=current_utility
                    best_action = new_action
                                
            return best_action
    
        def MAX_value(state,alpha,beta):
            if state in self.cache:
                return self.cache[state]
            if state.is_terminal():
                return state.utility(self)

            value=-2
            for new_action in state.actions():
                value= max(value,MIN_value(state.result(new_action),alpha,beta))
                if value >= beta:
                    return value
                alpha=max(alpha,value)
        
            self.cache[state]=alpha
            return value
        def MIN_value(state,alpha,beta):
            if state in self.cache:
                return self.cache[state]
            if state.is_terminal():
                return state.utility(self)

            value=2
            for new_action in state.actions():
                value = min(value,MAX_value(state.result(new_action),alpha,beta))
                
                if value <= alpha:
                    return value
                beta=min(beta,value);
            self.cache[state]=beta
            return value
        return alpha_beta_search(state)
