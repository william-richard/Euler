'''
Created on Oct 19, 2012

@author: wrichard
'''
        
def factorNoN(n):
    factors = factor(n)
    factors.remove(n)
    return factors
        
        
def factor(n):
    factors = set()
    for i in range(1,int(n/2) + 1):
        if n % i == 0:
            factors.add(i)
    factors.add(n)
    return factors

def numFactors(n):
    nFactors = 0
    sqrt = int(n**.5)
    for i in range(1, sqrt +1):
        if n % i == 0:
            nFactors += 2
    if sqrt**2 == n:
        nFactors -= 1
    return nFactors
    