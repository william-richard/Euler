'''
Created on Oct 18, 2012

@author: Will
'''

if __name__ == '__main__':
    nn = range(1,101)
    print sum(nn) ** 2  - sum([x ** 2 for x in nn]) 