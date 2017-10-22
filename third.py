import sys
import re
import math
from math import floor
def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)
#define MOD 1000000007
def fib(n):
    if n < 2:
        return n
    a = 0
    b = 1
    i = 1
    while i < n:
        ans = (a+b) % 1000000007
        a = b
        b = ans
        i+=1
    return ans

def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

lines = [line.strip() for line in sys.stdin.readlines()]
line1 = [int(i) for i in re.split("[^0-9]", lines[0])]
questions = [[int(i) for i in re.split("[^0-9]", j)] for j in lines[1:]]

#for i in range(0,line1[0]):
#    steps = questions[i][0]
#    sum = 0
#    if steps%2 != 0:
#        for i in range(0,floor((steps+1)//2)):
#            j = steps - i
#            sum += nCr(j,i)
#        print(int(sum))
#    else:
#        for i in range(0,steps//2+1):
#            j = steps - i
#            sum += nCr(j,i)
#        print(int(sum))

for i in range(0,line1[0]):
    steps = questions[i][0]
    print(fib(steps+1))
