__author__='jix029@ucsd.edu,A99076165,jih089@ucsd.edu,A99037641,z6hu@ucsd.edu,A99056145'

from sets import Set
import sys
import time
explored=Set() 
startTime = time.time()


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
    s=list(currentPrime)
    for index in range(len(s)):
        c=s[index]
        for i in range(10):
            s[index]=str(i)
            newString=''.join(s)
            if newString not in explored:
                if(newString[0]!='0' and isPrime(newString)):
                    result.append(newString)
        s[index]=c
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
        elif len(primes)==2 and isPrime(primes[0]) and isPrime(primes[1]):
            print(getPath(primes[0],primes[1]))
        else:
            print("invalid input!")
        print ('The script took {0} second !'.format(time.time() - startTime))

if __name__ == '__main__' :
        main()




