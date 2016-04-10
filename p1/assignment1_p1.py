from sets import Set

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
		current=str(currentPrime)
		for i in range(10):
			current[index]=i
			if(current!=currentPrime&&isPrime(current)&&current[0]!='0'&&current not in explored):
				result.append(current)

def getPath(startingPrime, finalPrime):
	queue = [(startingPrime), [startingPrime]]
	while queue:
		(v,p) = queue.pop(0)
		if v in explored:
			continue
		explored.add(v)
		for neighbor in getPossibleActions(v):
			if neighbor == finalPrime:
				return p + ' -> ' + finalPrime
			queue.append(neighbor,p + ' ' + neighbor)

	return 'UNSOLVABLE'


def main():
	primes=str(sys.stdin.readline()).split()
	print(getPath(primes[0],primes[1]))





