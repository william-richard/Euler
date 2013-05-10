'''
Created on Oct 19, 2012

@author: wrichard
'''

triangles = [0,1]

def triangleNumber(n):
    while len(triangles) <= n:
        triangles.append(triangles[-1] + len(triangles))
    return triangles[n]
    