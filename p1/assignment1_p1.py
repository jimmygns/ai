__author__='jix029@ucsd.edu,A99076165,jih089@ucsd.edu,A99037641,z6hu@ucsd.edu,A99056145'

from sets import Set
import sys
explored=Set() 


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

def getPath(startingPrime, finalPrime):
	if startingPrime==finalPrime:
		return startingPrime
	queue = [(startingPrime,startingPrime)]
	while queue:
		(v,p) = queue.pop(0)
		if v in explored:
			continue
		explored.add(v)
		for neighbor in getPossibleActions(v):
			if neighbor == finalPrime:
				return p + ' ' + finalPrime
			queue.append((neighbor,p + ' ' + neighbor))

	return 'UNSOLVABLE'


def main():
	for line in sys.stdin:
		primes=str(line).split()
		if len(primes)==1:
			print(primes[0])
		else:
			print(getPath(primes[0],primes[1]))
		explored.clear()

if __name__ == '__main__' :
        main()




