__author__='jix029@ucsd.edu,A99076165,jih089@ucsd.edu,A99037641,z6hu@ucsd.edu,A99056145'

from sets import Set
import sys



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
			if(newString!=currentPrime and isPrime(newString) and newString[0]!='0'):
				result.append(newString)
	return result

def getPath(startingPrime, finalPrime):
	if startingPrime==finalPrime:
		return startingPrime
	queueF = [(startingPrime,startingPrime)]
	dicF = {startingPrime:startingPrime}
	exploredF = Set()
	queueB = [(finalPrime,finalPrime)]
	dicB = {finalPrime:finalPrime}
	exploredB = Set()
	
	

	while queueF and queueB:
		
		(v,p) = queueF.pop(0)
		
		if v in exploredF:
			continue
		exploredF.add(v)
		
		for neighbor in getPossibleActions(v):
			if neighbor in dicB.keys():
				return p + ' ' + neighbor + '\n' + dicB[neighbor]
			queueF.append((neighbor,p + ' ' + neighbor))
			if neighbor not in dicF.keys():
				dicF[neighbor]=p + ' ' + neighbor
		
		(vb,pb) = queueB.pop(0)
		if vb in exploredB:
			continue
		exploredB.add(vb)
		for neighbor in getPossibleActions(vb):
			if neighbor in dicF.keys():
				return  dicF[neighbor] +'\n'+pb+ ' '+neighbor 
			queueB.append((neighbor,pb + ' ' + neighbor))
			if neighbor not in dicB.keys():
				dicB[neighbor]=pb + ' ' + neighbor
	return 'UNSOLVABLE'


def main():
        primes=str(sys.stdin.readline()).split()
        if len(primes)==1:
        	print(primes[0])
        else:
        	print(getPath(primes[0],primes[1]))

if __name__ == '__main__' :
        main()

