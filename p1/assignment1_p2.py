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

def getPath(startingPrime, finalPrime,explored, depth):
    if startingPrime==finalPrime:
        return finalPrime
    if depth>5:
        return 'failure'
    for neighbor in getPossibleActions(startingPrime):
        if neighbor in explored:
           continue
        explored.add(neighbor)
        #print (neighbor+' '+str(depth))
        result=getPath(neighbor,finalPrime,explored,depth+1)
        if result=='failure':
            continue
        else:
            #print (result)
            return (startingPrime+' '+result)
    if depth==0:
      return 'UNSOLVEABLE'
    return 'failure'


def main():
    primes=str(sys.stdin.readline()).split()
    print(getPath(primes[0],primes[1],{primes[0]},0))

if __name__ == '__main__' :
    main()
