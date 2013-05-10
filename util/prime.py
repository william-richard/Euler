'''
Created on Oct 18, 2012

@author: Will
'''

primes = set([2,3,5,7])


def firstNprimes(n):
    i = n
    while len(primes) < n:
        prime_sieve(i)
        i = i * 2
    return sorted(list(primes))[:n]

def primesLessThan(n):
    return prime_sieve(n)

def prime_factors(n):
    return trial_division(n)

def prime_sieve(m):
    global primes
    if max(primes) > m:
        return list(primes)
    newRange = range(max(primes),m+1,2)
    for i in range(2, m):
        removeThese = []
        for p in newRange:
            if p > i and p % i == 0:
                removeThese.append(p)
        for r in removeThese:
            newRange.remove(r)
    primes = primes.union(newRange)
    return [x for x in list(primes) if x <=m]

def trial_division(n):
    if n == 1:
        return [1]
    localPrimes = primesLessThan(int(n/2) + 1)
    prime_factors = []
    for p in localPrimes:
        while n % p == 0:
            prime_factors.append(p)
            n = n / p
    if n > 1: prime_factors.append(n)
    return prime_factors
