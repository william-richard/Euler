'''
Created on Oct 18, 2012

@author: Will
'''
from prime import prime_sieve

if __name__ == '__main__':
    n = 600851475143
    ps = prime_sieve(int(n ** .5) + 1)
    print "sieve done - got %d primes" % len(ps)
    ps.remove(1)
    ps.sort(reverse=True)
    for p in ps:
        if n % p == 0:
            print p
            break
