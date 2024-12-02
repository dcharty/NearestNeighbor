
# Please create a simple example use of the pynn library for your end user. Assume that the end
# user knows a lot about their subject matter but has only a basic understanding of Python.

# Meaningful examples may include reading a file, finding a few nearby points and writing them
# out to the console.
import sys
import os
from ast import literal_eval
sys.path.append('../../NEARESTNEIGHBOR')
from pynn import KDTree
def readFileQueryPoints():
    """readFileQueryPoints is a function used to show that you can input just
    an array full of tuples into the KDTree class to create the class/tree and how to 
    get nearest neighbor"""
    tempArr =[]
    with open("Example.txt") as f:
        for line in f:
            x = literal_eval(line)
            tempArr.append(x)
    tempTree = KDTree(tempArr)
    print(tempTree.nearestNeighbor((233, 1421)))
    print(tempTree.nearestNeighbor((-2000, 0)))
    print(tempTree.nearestNeighbor((40, 3)))

def readFileQueryInsert():
    """readFileQueryPoints is a function used to show that you can insert tuples one by one
    into the KDTree class to create the tree and how to 
    get nearest neighbor"""
    tempTree = KDTree()
    with open("Example.txt") as f:
        for line in f:
            x = literal_eval(line)
            tempTree.insert(x)
    print(tempTree.nearestNeighbor((233, 1421)))
    print(tempTree.nearestNeighbor((-2000, 0)))
    print(tempTree.nearestNeighbor((40, 3)))        
readFileQueryInsert()
print('\n')
readFileQueryPoints()