'''
Created on Feb 1, 2013

@author: Will
'''
import itertools

if __name__ == '__main__':
    end = (10 ** 6) - 1
    for idx, perm in enumerate(itertools.permutations(range(10))):
        if idx == end:
            s = ""
            for p in perm:
                s += str(p)
            print s 