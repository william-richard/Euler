'''
Created on Oct 21, 2012

@author: Will
'''
from fibonacci import fibonacci

if __name__ == '__main__':
    digitTarget = 1000
    i = 1
    while len(str(fibonacci(i))) < digitTarget:
        i += 1
    print i, fibonacci(i)