'''
Created on Oct 21, 2012

@author: Will
'''

fibs = [0,1,1]

def fibonacci(n):
    while len(fibs) <= n:
        fibs.append(fibonacci(n-1) + fibonacci(n-2))
    return fibs[n]