'''
Created on Oct 19, 2012

@author: Will
'''
from prime import prime_sieve

if __name__ == '__main__':
    p = prime_sieve(2000000)
    print "Done with sieve"
    print sum(p)