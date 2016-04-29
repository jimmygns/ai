# -*- coding: utf-8 -*-
__author__= 'Jinye Xu, Jiaying Hu, Zhongting Hu'
__email__ ='jix029@ucsd.edu,A99076165,jih089@ucsd.edu,A99037641,z6hu@ucsd.edu,A99056145'
from assignment2 import Player, State, Action


        

class MinimaxPlayer(Player):
    def __init__(self):
        self.cache ={}

    def move(self, state):
        if len(state.actions()) == 0:
                return None
        best_action=None
        value=-2
        for new_action in state.actions():
            new_value=self.mini_value(state.result(new_action))
            if  new_value>value:
                value=new_value
                best_action=new_action
        return best_action


    def max_value(self,state):
        if state.is_terminal():
            return state.utility(self)
        value=-2
        if len(state.actions())==0:
                 value= max(value,self.mini_value(state.result(None)))
        for new_action in state.actions():
            value = max(value,self.mini_value(state.result(new_action)))
        return value

    def mini_value(self,state):
        if state.is_terminal():
            return state.utility(self)
        value=2
        if len(state.actions())==0:
                 value= min(value,self.max_value(state.result(None)))
        for new_action in state.actions():
            value = min(value,self.max_value(state.result(new_action)))
        return value 



    # def minimax(self,state):
    #     #if state.ser() in self.cache:
    #         #return self.cache[state.ser()]
    #     if state.is_terminal():
    #         return state.utility(self)
    #     if state.player == self:
    #         value=-2
    #         for new_action in state.actions():
    #             new_utility = self.minimax(state.result(new_action))
    #             if new_utility > value:
    #                 value=new_utility
    #         #self.cache[state.ser()]=value
    #         return value
    #     else:
    #         value=2
    #         for new_action in state.actions():
    #             new_utility = self.minimax(state.result(new_action))
    #             if new_utility < value:
    #                 value=new_utility
    #         #self.cache[state.ser()]=value
    #         return value


        """
        Calculates the best move from the given board using the minimax
        algorithm.
        :param state: State, the current state of the board.
        :return: Action, the next move
        """