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
        """ samplesNum=0
        expectedNum=0
        for i in range(numSamples):
            x=self.priorsampling()

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
    def priorsampling(self):
        q = Queue.Queue()
        
        for i in self.rootNodes:
            q.put(i)
        sample=Sample()
        while not q.empty():
            node=q.get()
            r=random.uniform(0,1)
            
            p=node.getProbability(sample.assignments,True)
            if r>p:
                sample.setAssignment(node.getVariable(),False)
            else:
                sample.setAssignment(node.getVariable(),True)
            children=node.getChildren()
            for child in children:
                q.put(child)
        return sample """



    
    

    
    # 
    #     * Returns an estimate of P(queryVal=true|givenVars) using weighted sampling
    #     * @param queryVar Query variable in probability query
    #     * @param givenVars A list of assignments to variables that represent our given evidence variables
    #     * @param numSamples Number of weighted samples to perform
    #     
    def performWeightedSampling(self, queryVar, givenVars, numSamples):
        """ generated source for method performWeightedSampling """
        #  TODO
        #sampleWeight=0
        resultWeight={}
        resultWeight["True"]=0
        resultWeight["False"]=0
        for i in range(numSamples):
            x=self.priorsampling_weighted(givenVars)
            if x.assignments[queryVar.getName()]==True:
                resultWeight["True"]=resultWeight["True"]+x.getWeight()
            else:
                resultWeight["False"]=resultWeight["False"]+x.getWeight()
          #  sampleWeight=sampleWeight+x.getWeight()
    
        #num=(float)(resultWeight/float(sampleWeight))

        print resultWeight["True"]
        print (resultWeight["True"]+resultWeight["False"])
        return (float)(resultWeight["True"])/(float)(resultWeight["True"]+resultWeight["False"])

    def priorsampling_weighted(self, givenVars):
        q = Queue.Queue()
        
        for i in self.rootNodes:
            q.put(i)
        sample=Sample()
        while not q.empty():
            node=q.get()
            var=node.getVariable()
            if var in givenVars.keys():
                p=node.getProbability(sample.assignments,givenVars[var])
                sample.setAssignment(var.getName(),givenVars[var])
                sample.setWeight(sample.getWeight()*p)
            else:
                r=random.uniform(0,1)            
                p=node.getProbability(sample.assignments,True)
                
                if r>p:
                    sample.setAssignment(node.getVariable().getName(),False)
                else:
                    sample.setAssignment(node.getVariable().getName(),True)
            children=node.getChildren()
            for child in children:
                q.put(child)

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
        """resultSample=0
        var=[]
        for key in self.varMap.keys():
            sample=Sample()
            if key in givenVars.keys():
                sample.setAssignment(key,givenVars[key])
            else:
                var.append(sample)
                sample.setAssignment(key,bool(random.getrandbits(1)))

        for i in range(numTrials): 
            node=var.pop(0)
            num=
            self.resample(sample, queryVar)
            if sample.assignments[queryVar]==True:
                resultSample=resultSample+1

        
        num=(float)(resultSample/float(numTrials))
        return num



    def resample(self,sample,queryVar):
        node=self.varMap[queryVar]
        del sample.assignments[queryVar]
        p1=node.getProbability(sample.assignments,True)
        p2=node.getProbability(sample.assignments,False)+p1
        p=p1/p2
        r=random.uniform(0,1)
        if r>p:
            sample.setAssignment(queryVar,False)
        else:
            sample.setAssignment(queryVar,True)"""













