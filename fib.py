#The Fibonacci Sequence

#Method 1: Using a second order recurrence system

from typing import Dict

memo: Dict[int, int] = {0: 0, 1: 1} #base cases

def fib(n):
    if n not in memo:
        memo[n] = fib(n-1) + fib(n-2) #recursive case
    return memo[n]

out = fib(50)

print("The fiftieth value of the Fibonacci sequence: "+str(memo[50]))
print("The first fifty values of the Fibonacci sequence: "+str(list(memo.values())))

#Method 2: Using Binet's formula

phi = 0.5*(1+(5**0.5)) #the golden ratio
psi = 0.5*(1-(5**0.5))
memoB = []

def binet(m):
    for i in range(m+1): #we add one since range starts from 0 by default
        memoB.append(int((1/(5**0.5))*((phi**i)-(psi**i)))) #binet's formula
        
outB = binet(50)

print("The fiftieth value of the Fibonacci sequence: "+str(memoB[50]))
print("The first fifty values of the Fibonacci sequence: "+str(memoB))



