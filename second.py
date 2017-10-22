import sys
import re
import math

#def nCr(n,r):
#    f = math.factorial
#    return f(n) / f(r) / f(n-r)
def getchoose(n,r):
    if r >= n-r:
        second = r
    else:
        second = n-r
    count = 1
    product = 1
    for i in range(n,second,-1):
        if count <= c:
            product *= i/count
            count += 1
        else:
            product *= i
    return product


lines = [line.strip() for line in sys.stdin.readlines()]
line1 = [int(i) for i in re.split("[^0-9]", lines[0])]
questions = [[int(i) for i in re.split("[^0-9]", j)] for j in lines[1:]]
#divisors = [int(line) for line in lines[1:]]
#print(line1)
#print(questions)

#for i in range(0,len(questions)):
#    currentline = questions[i]
#    a = currentline[0]
#    b = currentline[1]
#    c = currentline[2]
#    shift = int(nCr(b,c))
#    product = float(a)
#    for i in range(0,shift-1): #-1 because product already starts at a^1
#        product *= a
#        product %= pow(10,9)+7
#    print(int(product))
for i in range(0,len(questions)):
    currentline = questions[i]
    a = currentline[0]
    b = currentline[1]
    c = currentline[2]
    if a == 1:
        print(1)
        continue
    myshift = int(getchoose(b,c))
    if a == 2:
        product = 1
        for i in range(0,myshift//100):
            #print(i)
            product <<= 100
            if product > pow(10,9)+7:
                product %= pow(10,9)+7
        product <<= myshift%100
        if product > pow(10,9)+7:
            product %= pow(10,9)+7
        print(product)
        continue
    
    product = float(1)
    
    for i in range(0,myshift//3):
        #print(i)
        product *= pow(a,3)
        if product > pow(10,9)+7:
            product %= pow(10,9)+7
    for i in range(0,myshift%3):
        #print(i)
        product *= a
        if product > pow(10,9)+7:
            product %= pow(10,9)+7
    print(int(product))

