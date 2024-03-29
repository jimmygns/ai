#!/usr/bin/env python
""" generated source for module BayesianNetwork """
from Assignment4 import *
import Queue
import random
# 
#  * A bayesian network
#  * @author Panqu
#  
class BayesianNetwork(object):
    """ generated source for class BayesianNetwork """
    # 
    #     * Mapping of random variables to nodes in the network
    #     
    varMap = None

    # 
    #     * Edges in this network
    #     
    edges = None

    # 
    #     * Nodes in the network with no parents
    #     
    rootNodes = None

    # 
    #     * Default constructor initializes empty network
    #     
    def __init__(self):
        """ generated source for method __init__ """
        self.varMap = {}
        self.edges = []
        self.rootNodes = []

    # 
    #     * Add a random variable to this network
    #     * @param variable Variable to add
    #     
    def addVariable(self, variable):
        """ generated source for method addVariable """
        node = Node(variable)
        self.varMap[variable]=node
        self.rootNodes.append(node)

    # 
    #     * Add a new edge between two random variables already in this network
    #     * @param cause Parent/source node
    #     * @param effect Child/destination node
    #     
    def addEdge(self, cause, effect):
        """ generated source for method addEdge """
        source = self.varMap.get(cause)
        dest = self.varMap.get(effect)
        self.edges.append(Edge(source, dest))
        source.addChild(dest)
        dest.addParent(source)
        if dest in self.rootNodes:
            self.rootNodes.remove(dest)

    # 
    #     * Sets the CPT variable in the bayesian network (probability of
    #     * this variable given its parents)
    #     * @param variable Variable whose CPT we are setting
    #     * @param probabilities List of probabilities P(V=true|P1,P2...), that must be ordered as follows.
    #       Write out the cpt by hand, with each column representing one of the parents (in alphabetical order).
    #       Then assign these parent variables true/false based on the following order: ...tt, ...tf, ...ft, ...ff.
    #       The assignments in the right most column, P(V=true|P1,P2,...), will be the values you should pass in as probabilities here.
    #     
    def setProbabilities(self, variable, probabilities):
        """ generated source for method setProbabilities """
        probList = []
        for probability in probabilities:
            probList.append(probability)
        self.varMap.get(variable).setProbabilities(probList)

    # 
    #     * Returns an estimate of P(queryVal=true|givenVars) using rejection sampling
    #     * @param queryVar Query variable in probability query
    #     * @param givenVars A list of assignments to variables that represent our given evidence variables
    #     * @param numSamples Number of rejection samples to perform
    #     
    def performRejectionSampling(self, queryVar, givenVars, numSamples):
        """ generated source for method performRejectionSampling """
        #  TODO
        samplesNum=0
        expectedNum=0
        list=[]
        q = Queue.Queue()
        for i in self.rootNodes:
            q.put(i)
        while not q.empty():
            node=q.get()
            if not node in list:
                list.append(node)
            children=node.getChildren()
            for child in children:
                q.put(child)
        for i in range(numSamples):
            x=self.priorsampling(list)

            flag=True
            for key in givenVars.keys():
                if givenVars[key]!=x.assignments[key]:
                    flag=False
            if flag==True:
                samplesNum=samplesNum+1
                if x.assignments[queryVar]==True:
                    expectedNum=expectedNum+1
    
        num=(float)(expectedNum/float(samplesNum))

   
        return num
    def priorsampling(self,list):
        q = Queue.Queue()
        
        for i in self.rootNodes:
            q.put(i)
        sample=Sample()
        for node in list:
            r=random.uniform(0,1)
            
            p=node.getProbability(sample.assignments,True)
            if r>p:
                sample.setAssignment(node.getVariable(),False)
            else:
                sample.setAssignment(node.getVariable(),True)
        return sample 



    
    

    
    # 
    #     * Returns an estimate of P(queryVal=true|givenVars) using weighted sampling
    #     * @param queryVar Query variable in probability query
    #     * @param givenVars A list of assignments to variables that represent our given evidence variables
    #     * @param numSamples Number of weighted samples to perform
    #     
    def performWeightedSampling(self, queryVar, givenVars, numSamples):
        """ generated source for method performWeightedSampling """
        #  TODO
        resultWeight={}
        resultWeight["True"]=0
        resultWeight["False"]=0
        list=[]
        q = Queue.Queue()
        for i in self.rootNodes:
            q.put(i)
        while not q.empty():
            node=q.get()
            if not node in list:
                list.append(node)
            children=node.getChildren()
            for child in children:
                q.put(child)

        for i in range(numSamples):
            x=self.priorsampling_weighted(givenVars,list)
            if x.assignments[queryVar.getName()]==True:
                resultWeight["True"]=resultWeight["True"]+x.getWeight()
            else:
                resultWeight["False"]=resultWeight["False"]+x.getWeight()
        return (float)(resultWeight["True"])/(float)(resultWeight["True"]+resultWeight["False"])

    def priorsampling_weighted(self, givenVars,list):
        q = Queue.Queue()
        sample=Sample()
        for node in list:
            var=node.getVariable()
            if var in givenVars:
                p=node.getProbability(sample.assignments,givenVars[var])
                sample.setAssignment(var,givenVars[var])
                sample.setWeight(sample.getWeight()*p)
            else:
                r=random.uniform(0,1)            
                p=node.getProbability(sample.assignments,True)
                
                if r>p:
                    sample.setAssignment(node.getVariable().getName(),False)
                else:
                    sample.setAssignment(node.getVariable().getName(),True)

        return sample

    # 
    #     * Returns an estimate of P(queryVal=true|givenVars) using Gibbs sampling
    #     * @param queryVar Query variable in probability query
    #     * @param givenVars A list of assignments to variables that represent our given evidence variables
    #     * @param numTrials Number of Gibbs trials to perform, where a single trial consists of assignments to ALL
    #       non-evidence variables (ie. not a single state change, but a state change of all non-evidence variables)
    #     
    def performGibbsSampling(self, queryVar, givenVars, numTrials):
        """ generated source for method performGibbsSampling """
        #  TODO
       
        non_evidence=[]
        Normal={}
        Normal["True"]=0
        Normal["False"]=0
        sample=Sample()
        for key in self.varMap.keys(): 
            if key in givenVars:
                sample.setAssignment(key,givenVars[key])
            else:
                non_evidence.append(key)
                a=bool(random.getrandbits(1))
                sample.setAssignment(key,a)
                
        for i in range(numTrials): 
            for ne in non_evidence:
                self.resample(sample, ne)
                if sample.assignments[queryVar]==True:
                    Normal["True"]=Normal["True"]+1
                else:
                    Normal["False"]=Normal["False"]+1
        num=(float)(Normal["True"])/(float)(Normal["True"]+Normal["False"])
        return num



    def resample(self,sample,var):
        node=self.varMap[var]
        
        p1=node.getProbability(sample.assignments,True)
        p2=node.getProbability(sample.assignments,False)
        p=1.0
        px=1.0
        if sample.assignments[var]==True:
            p=p1
            px=p2
        else:
            p=p2
            px=p1
        for child in node.getChildren():
            p3=child.getProbability(sample.assignments,sample.assignments[child.getVariable()])
            p=p*p3
            
        sample.setAssignment(node.getVariable(),not sample.assignments[var])   
        for child in node.getChildren():
            p4=child.getProbability(sample.assignments,sample.assignments[child.getVariable()])
            px=px*p4
        sample.setAssignment(node.getVariable(),not sample.assignments[var])
        if sample.assignments[var]==True:
            if p==0:
                p=0
            else:
                p=(float)(p/(p+px))
        else:
            if px==0:
                p=0
            else:
                p=(float)(px/(p+px))
        r=random.uniform(0,1)
        if r>p:
            sample.setAssignment(var,False)
        else:
            sample.setAssignment(var,True)













