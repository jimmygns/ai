__author__='jix029@ucsd.edu,A99076165,jih089@ucsd.edu,A99037641,z6hu@ucsd.edu,A99056145'

from sets import Set
import sys
import Queue as Q
import time
explored=Set() 
startTime = time.time()

class Node:
	def __init__(self,number,priority,level,path):
		self.number=number
		self.priority=priority
		self.level=level
		self.path=path

	def getNumber(self):
		return self.number

	def getPath(self):
		return self.path

	def __cmp__(self,other):
		return cmp(self.priority,other.priority)

def isPrime(num):
    number=int(num)
    if number>2 and number%2==0:
        return False
    for i in range(3,number,2):
        if number%i == 0:
            return False
    return True


def getPossibleActions(currentPrime):
	result=[]
	current=currentPrime
	for index in range(len(current)):
		current=currentPrime
		for i in range(10):
			s=list(current)
			s[index]=str(i)
			newString=''.join(s)
			if(newString!=currentPrime and isPrime(newString) and newString[0]!='0' and newString not in explored):
				result.append(newString)
	return result

def getDistance(current,final):
	if(len(current)!=len(final)):
		return 0
	result=0
	for index in range(len(current)):
		if(current[index]!=final[index]):
			result=result+1
	return result



def getPath(startingPrime, finalPrime):
	if startingPrime==finalPrime:
		return startingPrime
	queue = Q.PriorityQueue()
	queue.put(Node(startingPrime,getDistance(startingPrime,finalPrime),1,startingPrime))
	while not queue.empty():
		currentNode = queue.get()
		if currentNode.getNumber() in explored:
			continue
		explored.add(currentNode.getNumber())
		for neighbor in getPossibleActions(currentNode.getNumber()):
			if neighbor == finalPrime:
				return currentNode.getPath() + ' ' + finalPrime
			queue.put(Node(neighbor,currentNode.level+getDistance(neighbor,finalPrime),currentNode.level+1,currentNode.getPath() + ' ' + neighbor))

	return 'UNSOLVABLE'


def main():
    for line in sys.stdin:
        primes=str(line).split()
        if len(primes)==1:
            print(primes[0])
        elif len(primes)==2 and isPrime(primes[0]) and isPrime(primes[1]):
            print(getPath(primes[0],primes[1]))
        else:
            print("invalid input!")
        print ('The script took {0} second !'.format(time.time() - startTime))


if __name__ == '__main__' :
        main()