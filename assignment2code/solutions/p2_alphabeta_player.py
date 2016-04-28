# -*- coding: utf-8 -*-
__author__ = 'Dan'
__email__ = 'daz040@eng.ucsd.edu'

from assignment2 import Player, State, Action


class AlphaBetaPlayer(Player):
    
    def __init__(self):
    
        self.cache={}
    

    """def move(self, state):
        if len(state.actions()) == 0:
            return None
        for new_action in state.actions():  
            if self.alphabeta(state.result(new_action),-2,2) == 1:
                print 1
                return new_action
        for new_action in state.actions():
            if self.alphabeta(state.result(new_action),-2,2) == 0:
                print 0
                return new_action
        print -1
        return state.actions()[0]


    def alphabeta(self,state,alpha,beta):
        if state.ser() in self.cache:
            return self.cache[state.ser()]
        if state.is_terminal():
            return state.utility(self)
        if state.player == self:
            value=-2
            if len(state.actions())==0:
                value = max(value,self.alphabeta(state.result(None),alpha,beta))
                alpha = max(value,alpha)               
            for new_action in state.actions():
                new_state=state.result(new_action)
                value = max(value,self.alphabeta(new_state,alpha,beta))
                tTable[state.ser()]=value
                if beta <= value:
                    return value
                alpha=max(alpha,value)
            return value
        else:
            value=2
            if len(state.actions())==0:
                value = min(beta,self.alphabeta(state.result(None),alpha,beta))
                beta = min(value,beta)               
            for new_action in state.actions():
                new_state=state.result(new_action)
                value = min(value,self.alphabeta(new_state,alpha,beta))
                tTable[state.ser()]=value
                if value <= alpha:
                    return value
                beta = min(value,beta)
            return value
    """
    def move(self, state):
        """Calculates the best move from the given board using the minimax
         algorithm with alpha-beta pruning and transposition table.
         :param state: State, the current state of the board.
        :return: Action, the next move
         """
    
        def alpha_beta_search(state):
             best_utility=-2
             for new_action in state.actions():
                current_utility = MIN_value(state.result(new_action), -2, 2)
                if(current_utility>best_utility):
                    best_utility=current_utility
                    best_action = new_action
                                
             return best_action
    
        def MAX_value(state,alpha,beta):
            if state.ser() in self.cache:
                return self.cache[state.ser()]
            if state.is_terminal():
                 return state.utility(self)

            value=-2
            if len(state.actions())==0:
                 value= max(value,MIN_value(state.result(None),alpha,beta))
                 if value >= beta:
                     return value
            for new_action in state.actions():
                 value= max(value,MIN_value(state.result(new_action),alpha,beta))
                 if value >= beta:
                     return value
                 alpha=max(alpha,value)
            self.cache[state.ser()]=value
        
            return value
        def MIN_value(state,alpha,beta):
            if state.ser() in self.cache:
                return self.cache[state.ser()]
            if state.is_terminal():
                return state.utility(self)

            value=2
            if len(state.actions())==0:
                value= min(value,MIN_value(state.result(None),alpha,beta))
                if value <= alpha:
                    return value
            for new_action in state.actions():
                value = min(value,MAX_value(state.result(new_action),alpha,beta))
                if value <= alpha:
                    return value
                beta=min(beta,value);
            self.cache[state.ser()]=value
            return value
        return alpha_beta_search(state)

