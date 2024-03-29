# -*- coding: utf-8 -*-

__author__= 'Jinye Xu, Jiaying Hu, Zhongting Hu'
__email__ ='jix029@ucsd.edu,A99076165,jih089@ucsd.edu,A99037641,z6hu@ucsd.edu,A99056145'

from assignment2 import Player,State,Player,Action
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
class CustomPlayer(Player):
    """The custom player implementation.
    """

    def __init__(self):
        """Called when the Player object is initialized. You can use this to
        store any persistent data you want to store for the  game.

        For technical people: make sure the objects are picklable. Otherwise
        it won't work under time limit.
        """
        self.cache={}
        self.MaxDepth=15
        self.best_utility=-2
        self.depth_limit=0
        self.terminal=True
    def move(self, state):
        """
        You're free to implement the move(self, state) however you want. Be
        run time efficient and innovative.
        :param state: State, the current state of the board.
        :return: Action, the next move
        """
        
        self.depth_limit=1
        self.best_utility=-2
        action=None
        while not self.is_time_up():
            self.terminal=True
            self.cache={}
            action=self.alpha_beta_search(state,0)
            if self.terminal==True:
                break
            self.depth_limit=self.depth_limit+1
        
        return action
    
    
    def alpha_beta_search(self,state,depth):
        self.best_utility=-2
        best_action=None
        queue = Q.PriorityQueue()
        for new_action in state.actions():
            queue.put(Node(new_action,self.evaluate(state.result(new_action),state.player_row),self.evaluate(state.result(new_action),state.player_row)))
        while not queue.empty():
            if not self.is_time_up():
                first_action=queue.get().getAction()
                current_utility = self.MIN_value(state.result(first_action), -2, 2,depth+1)
               
                if(current_utility>self.best_utility):
                    self.best_utility=current_utility
                    best_action = first_action
            
            else:
               first_action=queue.get().getAction()
               current_utility=self.evaluate(state.result(first_action),state.player_row)
               if(current_utility>self.best_utility):
                    self.best_utility=current_utility
                    best_action = first_action
        return best_action
        
        
    def MAX_value(self,state,alpha,beta,depth):
        if depth>=self.depth_limit or self.is_time_up():
            value=self.evaluate(state,state.player_row)
            if not state.is_terminal():
                self.terminal=False
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
            if state.ser() in self.cache:
                self.cache[state.ser()]=max(self.cache[state.ser()],value)
            else:
                self.cache[state.ser()]=value
        return value
            
            
    def MIN_value(self,state,alpha,beta,depth):
        if depth>=self.depth_limit or self.is_time_up():
            if not state.is_terminal():
                self.terminal=False

            value=self.evaluate(state,state.player_row)
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
            if state.ser() in self.cache:
                self.cache[state.ser()]=min(self.cache[state.ser()],value)
            else:
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
                    
                    
    def heuristic(self,state,my_row):
        max_blank=0
        max_num=0;
        for i in range(State.M):
            if my_row==0:
                if state.board[State.M+1+i]==0:
                    if state.board[i]>max_num:
                        max_num=state.board[i]
                        max_blank=i
            else:
                if state.board[i]==0:
                    if state.board[State.M+i+1]>max_num:
                        max_num=state.board[State.M+i+1]
                        max_blank=State.M+i+1
        return Action(my_row,max_blank)
                        
                        
    def hasZero(self,state,my_row):
        for i in range(State.M):
            if my_row==0:
                if state.board[State.M+1+i]==0 and state.board[i]>0:
                    
                    return True
            else:
                if state.board[i]==0 and state.board[State.M+1+i]>0:
                    return True
        return False
