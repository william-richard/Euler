'''
Created on Jan 29, 2013

@author: Will
'''
import collections

class Node:
    def __init__(self, _val):
        self.val = _val
        self.children = []
        self.parents = []
    def __repr__(self):
        return str(self.val)
        
def readTriangle(triFileLoc):
    prevRow = None
    tri = open(triFileLoc, 'r')
    for line in tri:
        thisRow = []
        for idx, val in enumerate(line.split()):
            valNode = Node(int(val))
            thisRow.append(valNode)
            if prevRow is not None:
                if idx - 1 >= 0:
                    prevRow[idx-1].children.append(valNode)
                    valNode.parents.append(prevRow[idx-1])
                if idx < len(prevRow):
                    prevRow[idx].children.append(valNode)
                    valNode.parents.append(prevRow[idx])
            else:
                rootNode = valNode
        prevRow = list(thisRow)
    tri.close()
    return rootNode

def bruteRec(node, sumSoFar):
    if len(node.children) == 0:
        return [node.val + sumSoFar]
    mySum = sumSoFar + node.val
    ret = []
    for c in node.children:
        ret.extend(bruteRec(c, mySum))
    return ret

def brute(root):
    sums = bruteRec(root, 0)
    return max(sums)

def smart(root):
    #find the bottom row of the tree
    bottomRow = set()
    nodesToTraverse = {root}
    while len(nodesToTraverse) > 0:
        curNode = nodesToTraverse.pop()
        if len(curNode.children) == 0:
            bottomRow.add(curNode)
        nodesToTraverse.update(set(curNode.children))
    #update each nodes best value with it's sum plus the best from its children
    nodesToTraverse = collections.deque(bottomRow)
    while len(nodesToTraverse) > 0:
        curNode = nodesToTraverse.popleft()
        curNode.best = max([c.best for c in curNode.children] + [0]) + curNode.val
        for p in curNode.parents:
            if not p in nodesToTraverse:
                nodesToTraverse.append(p)
    return root.best

if __name__ == '__main__':
    #read in the triangle
    #root = readTriangle('./18-1.txt')
    #root = readTriangle('./18-2.txt')
    root = readTriangle('./triangle.txt')
    
    #now, try to find the best way through it
    #result = brute(root)
    #print result
    result = smart(root)
    print result
    
    
    
    
    