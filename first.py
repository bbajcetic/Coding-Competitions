import sys
import re
from math import floor

def is_prime(x):
    if x > 1:
        n = x // 2
        for i in range(2, n + 1):
            if x % i == 0:
                return False
        return True
    else:
        return False

def get_Cdivisors(num):
    thelist = []
    if num%2 != 0:
        for i in range(3, floor(num/2)+1,2):
            if num%i == 0:
                thelist.append(i)
    else:
        for i in range(2, floor(num/2)+1):
            if num%i == 0:
                thelist.append(i)
    thelist.append(num)
    return len(thelist)
    
def get_Bdivisors(num):
    thelist = []
    if num%2 != 0:
        for i in range(3, floor(num/2)+1,2):
            if num%i == 0 and i%divisors[current] != 0:
                thelist.append(i)
    else:
        for i in range(2, floor(num/2)+1):
            if num%i == 0 and i%divisors[current] != 0:
                thelist.append(i)
    if (num%divisors[current] != 0):
        thelist.append(num)
    return len(thelist)


lines = [line.strip() for line in sys.stdin.readlines()]
line1 = [int(i) for i in re.split("[^0-9]", lines[0])]
divisors = [int(line) for line in lines[1:]]
initepsilon = set()
initprimes = set()
for i in range(line1[1],line1[2]+1):
    initepsilon.add(i)
    
if line1[1] <= 2 and line1[2] >= 2:
    initprimes.add(2)
off = 0
if line1[1]%2 == 0:
    off = 1
for i in range(line1[1]+off,line1[2]+1,2):
    if (is_prime(i)):
        initprimes.add(i)

        
for current in range(0,line1[0]):
    sum = 0
    epsilon = initepsilon
    primes = initprimes
    sum += len(epsilon)

    epsilon = epsilon.difference(primes)
    primes = primes.difference(set([divisors[current]]))
    sum += len(primes)
    listA = list(epsilon)
    listB = []
    listC = []
    for i in range(0,len(listA)):
        if  listA[i]%line1[2] == 0:
            listB.append(listA[i])
        else:
            listC.append(listA[i])
    for i in range(0,len(listB)):
        sum += get_Bdivisors(listB[i])
    for i in range(0,len(listC)):
        sum += get_Cdivisors(listC[i])
    print(sum)

