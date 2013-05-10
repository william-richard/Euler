'''
Created on Feb 1, 2013

@author: Will
'''

if __name__ == '__main__':
    i = 1
    step = 2
    tot = 1
    maxSide = 1001
    maxI = maxSide ** 2
    while i < maxI:
        for j in range(4):
            i += step
            tot += i
        step += 2
        
    print tot
        
        