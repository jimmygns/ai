__author__='jix029@ucsd.edu,A99076165,jih089@ucsd.edu,A99037641,z6hu@ucsd.edu,A99056145'

from sets import Set
import sys
import time
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
            if(newString!=currentPrime and isPrime(newString) and newString[0]!='0'):
                result.append(newString)
        s[index]=c
    return result

def getPath(startingPrime, finalPrime):
    if startingPrime==finalPrime:
        return startingPrime
    queueF = [(startingPrime,startingPrime)]
    dicF = {}
    exploredF = Set()
    queueB = [(finalPrime,finalPrime)]
    dicB = {}
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
    for line in sys.stdin:
        primes=str(line).split()
        if len(primes)==1:
            print(primes[0]+'\n'+primes[0])
        elif len(primes)==2 and isPrime(primes[0]) and isPrime(primes[1]):
            print(getPath(primes[0],primes[1]))
        else:
            print("invalid input!")
        print ('The script took {0} second !'.format(time.time() - startTime))


if __name__ == '__main__' :
        main()

