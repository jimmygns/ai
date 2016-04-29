# -*- coding: utf-8 -*-

__author__ = 'Dan'
__email__ = 'daz040@eng.ucsd.edu'

from assignment2 import Player,State,Player
import Queue as Q
class Node:
    
    def __init__(self,action, priority,value):
        self.priority = priority
        self.value = value
        self.action=action
    def getAction(self):
        return self.action
    def getValue(self):
        return self.value
    def __cmp__(self, other):
        return cmp(self.priority, other.priority)
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
        self.best_utility=-2
    def move(self, state):
        """
        You're free to implement the move(self, state) however you want. Be
        run time efficient and innovative.
        :param state: State, the current state of the board.
        :return: Action, the next move
        """
        best_action=None
        while len(state.actions())>0 and self.MaxDepth<2*State.M+2:
            temp=self.best_utility
            action=self.alpha_beta_search(state,0)
            if self.best_utility>temp:
                best_action=action
            self.MaxDepth=self.MaxDepth+1
        return best_action
        
    def alpha_beta_search(self,state,depth):
        self.best_utility=-2
        queue = Q.PriorityQueue()
        for new_action in state.actions():
            queue.put(Node(new_action,self.evaluate(state.result(new_action),state.player_row),self.evaluate(state.result(new_action),state.player_row)))
        while not queue.empty():
            first_action=queue.get().getAction()
            current_utility = self.MAX_value(state.result(first_action), -2, 2,depth)
            if(current_utility>self.best_utility):
                self.best_utility=current_utility
                best_action = new_action
        return best_action
        
    def MAX_value(self,state,alpha,beta,depth):
        if self.is_time_up() or depth>=self.MaxDepth:
            value=self.evaluate(state,state.player_row)
            return value
        if state.ser() in self.cache:
            return self.cache[state.ser()]
        if state.is_terminal():
            return state.utility(self)
        
        value=-2
        if len(state.actions())==0:
            value= max(value,self.MIN_value(state.result(None),alpha,beta,depth+1))
        if value >= beta:
            return value
        queue = Q.PriorityQueue()
        for new_action in state.actions():
            queue.put(Node(new_action,self.evaluate(state.result(new_action),state.player_row),self.evaluate(state.result(new_action),state.player_row)))
        while not queue.empty():
            first_action=queue.get().getAction()
            value= max(value,self.MIN_value(state.result(first_action),alpha,beta,depth+1))
            if value >= beta:
                return value
            alpha=max(alpha,value)
            self.cache[state.ser()]=value
        return value
    def MIN_value(self,state,alpha,beta,depth):
        if self.is_time_up() or depth>=self.MaxDepth:
            value=(-1)*self.evaluate(state,state.player_row)
            return value
        if state.ser() in self.cache:
            return self.cache[state.ser()]
        if state.is_terminal():
            return state.utility(self)
        value=2
        if len(state.actions())==0:
            value= min(value,self.MAX_value(state.result(None),alpha,beta,depth+1))
            if value <= alpha:
                return value
        queue = Q.PriorityQueue()
        for new_action in state.actions():
            queue.put(Node(new_action,self.evaluate(state.result(new_action),state.player_row),self.evaluate(state.result(new_action),state.player_row)))

        while not queue.empty():
            first_action=queue.get().getAction()
            value = min(value,self.MAX_value(state.result(first_action),alpha,beta,depth+1))
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

