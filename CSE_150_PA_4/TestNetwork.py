#!/usr/bin/env python

from BayesianNetwork import *
# 
#   * Creates and tests the alarm network as given in the book.
#   
class TestNetwork(object):
    """ generated source for class TestNetwork """
    @classmethod
    def main(cls, args):
        """ generated source for method main """
        alarmnet = BayesianNetwork()
        #  Add variables to network
        burglary = RandomVariable("Burglary")
        earthquake = RandomVariable("Earthquake")
        alarm = RandomVariable("Alarm")
        john = RandomVariable("John")
        mary = RandomVariable("Mary")
        alarmnet.addVariable(burglary)
        alarmnet.addVariable(earthquake)
        alarmnet.addVariable(alarm)
        alarmnet.addVariable(john)
        alarmnet.addVariable(mary)
        #  Add edges to network
        alarmnet.addEdge(burglary, alarm)
        alarmnet.addEdge(earthquake, alarm)
        alarmnet.addEdge(alarm, john)
        alarmnet.addEdge(alarm, mary)
        #  Initialize probability tables
        burglaryProbs = [0.001]
        earthquakeProbs = [0.002]
        alarmProbs = [0.95, 0.94, 0.29, 0.001]
        johnProbs = [0.9, 0.05]
        maryProbs = [0.7, 0.01]
        alarmnet.setProbabilities(burglary, burglaryProbs)
        alarmnet.setProbabilities(earthquake, earthquakeProbs)
        alarmnet.setProbabilities(alarm, alarmProbs)
        alarmnet.setProbabilities(john, johnProbs)
        alarmnet.setProbabilities(mary, maryProbs)

        guiltynet = BayesianNetwork()
        #  Add variables to network
        brokeLaw = RandomVariable("BrokeLaw")
        indicted = RandomVariable("Indicted")
        motivatedProsecuter = RandomVariable("MotivatedProsecuter")
        guilty = RandomVariable("Guilty")
        jailed = RandomVariable("Jailed")

        guiltynet.addVariable(brokeLaw) 
        guiltynet.addVariable(indicted)
        guiltynet.addVariable(motivatedProsecuter)
        guiltynet.addVariable(guilty)
        guiltynet.addVariable(jailed)

        #  Add edges to network
        guiltynet.addEdge(brokeLaw, indicted)
        guiltynet.addEdge(motivatedProsecuter, indicted)
        guiltynet.addEdge(brokeLaw, guilty)
        guiltynet.addEdge(indicted, guilty)
        guiltynet.addEdge(motivatedProsecuter, guilty)
        guiltynet.addEdge(guilty, jailed)

        #  Initialize probability tables
        brokeLawProbs = [0.9]
        motivatedProsecuterProbs = [0.1]
        indictedProbs = [0.9, 0.5, 0.5, 0.1]
        guiltyProbs = [0.9, 0.8, 0.0, 0.0, 0.2, 0.1, 0.0, 0.0]
        jailedProbs = [0.9, 0.0]

        guiltynet.setProbabilities(brokeLaw, brokeLawProbs)
        guiltynet.setProbabilities(motivatedProsecuter, motivatedProsecuterProbs)
        guiltynet.setProbabilities(indicted, indictedProbs)
        guiltynet.setProbabilities(guilty, guiltyProbs)
        guiltynet.setProbabilities(jailed, jailedProbs)


        #  Perform sampling tests
        #  ----------------------
        #  P(J=1|B=0,E=1) = TODO in writeup
        print("Test 1")
        given1 = {}
        given1[burglary]= False
        given1[earthquake]=True
        print('alarm')
        #print("rejection sampling: " +str(alarmnet.performRejectionSampling(john, given1, 999999)))
        #print("weighted sampling: " + str(alarmnet.performWeightedSampling(john, given1, 99999)))
        print("gibbs sampling: " + str(alarmnet.performGibbsSampling(john, given1, 99999)))
        given3={}
        given3[brokeLaw]=True
        given3[motivatedProsecuter]=False
        #print('guilty')
        #print("rejection sampling: " +str(guiltynet.performRejectionSampling(jailed, given3, 999999)))
        #print("weighted sampling: " + str(guiltynet.performWeightedSampling(jailed, given3, 99999)))
        #print("gibbs sampling: " + str(guiltynet.performGibbsSampling(jailed, given3, 99999)))
        #  P(B=1|J=1) = TODO in writeup
        print("Test 2")
        given2 = {}
        given4={}
        given2[john]=True
        given4[jailed]=True
        #print("rejection sampling: " + str(alarmnet.performRejectionSampling(burglary, given2, 999999)))
        #print("weighted sampling: " + str(alarmnet.performWeightedSampling(burglary, given2, 99999)))
        print("gibbs sampling: " + str(alarmnet.performGibbsSampling(burglary, given2, 99999)))
        #print('guilty')
        #print("rejection sampling: " +str(guiltynet.performRejectionSampling(motivatedProsecuter, given4, 999999)))
        #print("weighted sampling: " + str(guiltynet.performWeightedSampling(motivatedProsecuter, given4, 99999)))
        #print("gibbs sampling: " + str(guiltynet.performGibbsSampling(motivatedProsecuter, given4, 99999)))

if __name__ == '__main__':
    import sys
    TestNetwork.main(sys.argv)

