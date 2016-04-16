__author__='jix029@ucsd.edu,A99076165,jih089@ucsd.edu,A99037641,z6hu@ucsd.edu,A99056145'

from sets import Set
import sys
import time
import math

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

def getPath(startingPrime, finalPrime,explored, depth,limit):
    if startingPrime==finalPrime:
        return finalPrime
    if depth>limit:
        return 'failure'
    for neighbor in getPossibleActions(startingPrime):
        if neighbor in explored:
           continue
        explored.add(neighbor)
        #print (neighbor+' '+str(depth))
        result=getPath(neighbor,finalPrime,explored,depth+1,limit)
        explored.remove(neighbor)
        if result=='failure':
            continue
        else:
            #print (result)
            return (startingPrime+' '+result)
    if depth==0:
      return 'UNSOLVEABLE'
    return 'failure'

def repeatDFS(startingPrime,finalPrime):
    for i in range(8):
        result=getPath(startingPrime,finalPrime,{startingPrime},0,i)
        if result=='UNSOLVEABLE':
            continue
        else:
            return result
    return 'UNSOLVEABLE'
def main():
    for line in sys.stdin:
        primes=str(line).split()
        if len(primes) ==1:
            print(primes[0])
        else:
            print (repeatDFS(primes[0],primes[1]))
        

if __name__ == '__main__' :
    main()
