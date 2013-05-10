'''
Created on Oct 18, 2012

@author: Will
'''
from prime import firstNprimes

if __name__ == '__main__':
    print sorted(firstNprimes(10001), reverse=True)[0]
