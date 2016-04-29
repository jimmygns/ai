# -*- coding: utf-8 -*-

__author__ = 'Dan'
__email__ = 'daz040@eng.ucsd.edu'

from assignment2 import Player,State,Player


class PleasePleaseChangeThisToSomethingSomethingPlayer(Player):
    """The custom player implementation.
    """

    def __init__(self):
        """Called when the Player object is initialized. You can use this to
        store any persistent data you want to store for the  game.

        For technical people: make sure the objects are picklable. Otherwise
        it won't work under time limit.
        """
        self.cache={}
        self.MaxDepth=0
    
    def move(self, state):
        """
        You're free to implement the move(self, state) however you want. Be
        run time efficient and innovative.
        :param state: State, the current state of the board.
        :return: Action, the next move
        """
        for i in range(10):
        self.MaxDepth = 80
        action=self.alpha_beta_search(state,0)
        return action
        
    def alpha_beta_search(self,state,depth):
        best_utility=-2
        for new_action in state.actions():
            current_utility = self.MIN_value(state.result(new_action), -2, 2,depth)
            if(current_utility>best_utility):
                best_utility=current_utility
                best_action = new_action
        return best_action
        
    def MAX_value(self,state,alpha,beta,depth):
        if state.ser() in self.cache:
            return self.cache[state.ser()]
        if state.is_terminal():
            return state.utility(self)
        if self.is_time_up():
            value=self.evaluate(state,state.player_row)
            return value
        value=-2
        if len(state.actions())==0:
            value= max(value,self.MIN_value(state.result(None),alpha,beta,depth+1))
        if value >= beta:
            return value
        for new_action in state.actions():
            value= max(value,self.MIN_value(state.result(new_action),alpha,beta,depth+1))
            if value >= beta:
                return value
            alpha=max(alpha,value)
            self.cache[state.ser()]=value
        return value
    def MIN_value(self,state,alpha,beta,depth):
        if state.ser() in self.cache:
            return self.cache[state.ser()]
        if state.is_terminal():
            return state.utility(self)
        if depth>self.MaxDepth:
            value=self.evaluate(state,state.player_row)
            return value
        value=2
        if len(state.actions())==0:
            value= min(value,self.MAX_value(state.result(None),alpha,beta,depth+1))
            if value <= alpha:
                return value
        for new_action in state.actions():
            value = min(value,self.MAX_value(state.result(new_action),alpha,beta,depth+1))
            if value <= alpha:
                return value
            beta=min(beta,value);
            self.cache[state.ser()]=value
        return value
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

