from sets import Set
import sys
import Queue as Q

explored=Set() 

class Node:
	def __init__(self,number,priority,path):
		self.number=number
		self.priority=priority
		self.path=path

	def getNumber(self):
		return self.number

	def getPath(self):
		return self.path

	def __cmp__(self,other):
		return cmp(self.priority,other.priority)

def isPrime(num):
	number=int(num)
	for i in range(2,number):
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
	queue = Q.PriorityQueue()
	queue.put(Node(startingPrime,getDistance(startingPrime,finalPrime),startingPrime))
	while not queue.empty():
		currentNode = queue.get()
		if currentNode.getNumber() in explored:
			continue
		explored.add(currentNode.getNumber())
		for neighbor in getPossibleActions(currentNode.getNumber()):
			if neighbor == finalPrime:
				return currentNode.getPath() + ' ' + finalPrime
			queue.put(Node(neighbor,currentNode.priority+getDistance(neighbor,finalPrime),currentNode.getPath() + ' ' + neighbor))

	return 'UNSOLVABLE'


def main():
        primes=str(sys.stdin.readline()).split()
        print(getPath(primes[0],primes[1]))

if __name__ == '__main__' :
        main()