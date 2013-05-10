'''
Created on Oct 19, 2012

@author: wrichard
'''

def chainLength(n):
    if n <= 1:
        return 1
    if n % 2 == 0:
        return chainLength(n / 2) + 1
    else:
        return chainLength(3*n+1) + 1

if __name__ == '__main__':
    maxChain = 0
    maxN = 0
    for n in range(1, 10**6):
        cl = chainLength(n)
        if cl > maxChain:
            maxN = n
            maxChain = cl
            
    print maxN