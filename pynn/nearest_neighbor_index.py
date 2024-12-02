import math
import unittest

def fakedistance(point1,point2):
        """
        FakeDistance returns the euclidean distance between two points just without the square root
        This is because the squareroot is not needed when comparing two distances and because
        square root takes a lot of extra cycles. Just small optimization. 
        """
        return (point1[0]-point2[0])**2+(point1[1]-point2[1])**2

def closest(point,node1,node2):
    if(node1==None):
        return node2
    if(node2==None):
        return node1
    #Closet Finds which node is closer to a singular point.
    if(fakedistance(point,node1.point)>fakedistance(point,node2.point)):
        return node2
    else:
        return node1
#simple node class
class node:
    def __init__(self,point):
        self.point=point
        self.leftChild = None
        self.rightChild = None
#KD tree implmentation
class KDTree:
    """
    KD tree is used because its easy to implement and it is very versatile, especially
    with low dimensions.
    """
    #dimensions variable.
    k=2
    def __init__(self,points=None):
        """
        initialize function for KDTree class. Can be initialized empty or with an array of points
        """
        self.head = None
        #just a check to see if points input is valid. if not it will just return with an empty tree.
        if(points==None or type(points)!=list or len(points)==0 or type(points[0])!=tuple):
            return
        for i in points:
            self.head=self.insert(i)
    def __printRec(self,parent):
        """
        recursive function for printing out tree points
        """
        if parent==None:
            return
        self.__printRec(parent.leftChild)
        print(parent.point)
        self.__printRec(parent.rightChild)
    def printTree(self):
        """
        basic binary tree print function going from 
        smallest/most negative point to biggest/most positive point in a 2d graph
        """
        self.__printRec(self.head)
    def __insertRecursion(self,parent,point,depth):
        """
        recursive function to insert a point in the correct location in the tree
        """
        if not parent:
            return node(point)
        axis = depth%self.k
        #basic binary-tree style check to see where point will go
        if point[axis] < parent.point[axis]:
            parent.leftChild = self.__insertRecursion(parent.leftChild,point,depth+1)
        else:
            parent.rightChild = self.__insertRecursion(parent.rightChild,point,depth+1)
        return parent
    
    def insert(self,point):
        """
        Start function to insert a point into the Tree
        """
        return self.__insertRecursion(self.head,point,0)
    #recursive Function for nearest neighbor search
    def __nearestNeighborRecursion(self,parent,point,depth):
        """
        Nearest Neighbor Algorithm used to detect the closest point to the target
        in a tree of points. used algorithm from this video: https://youtu.be/Glp7THUpGow
        I went through different implementations, but I had trouble finding one
        with a way to bypass checking the other side of the parent which would save time.
        This one popped up
        """
        if parent==None:
            return
        axis = depth%self.k
        if point[axis] < parent.point[axis]:
            firstBranch = parent.leftChild
            laterBranch = parent.rightChild
        else:
            firstBranch = parent.rightChild
            laterBranch = parent.leftChild
        temp = self.__nearestNeighborRecursion(firstBranch,point,depth+1)
        best = closest(point,temp,parent)
        radiusSquared = fakedistance(point,best.point)
        dist = point[axis]-parent.point[axis]
        #checks to see if its even worth checking the other side of the tree.
        if(radiusSquared >= dist*dist):
            temp = self.__nearestNeighborRecursion(laterBranch,point,depth+1)
            best =  closest(point,temp,best)
        return best
    def nearestNeighbor(self,point):
        """
        nearestNeighbor Start function. If tree is empty, it just returns None
        """
        if(self.head==None):
            return None
        return self.__nearestNeighborRecursion(self.head,point,0).point

class NearestNeighborIndex:
    """
    NearestNeighborIndex is intended to index a set of provided points to provide fast nearest
    neighbor lookup. 
    """

    def __init__(self, points):
        """
        takes an array of 2d tuples as input points to be indexed. 
        It creates a KDtree with said points as input.
        It also stores the points, as is to be used for find_nearest_slow. 
        """
        #print(points)
        self.points = points
        self.tree = KDTree(points)
        #self.tree.printTree()
    @staticmethod
    def find_nearest_slow(query_point, haystack):
        """
        find_nearest_slow returns the point that is closest to query_point. If there are no indexed
        points, None is returned.
        """

        min_dist = None
        min_point = None

        for point in haystack:
            deltax = point[0] - query_point[0]
            deltay = point[1] - query_point[1]
            dist = math.sqrt(deltax * deltax + deltay * deltay)
            if min_dist is None or dist < min_dist:
                min_dist = dist
                min_point = point

        return min_point

    def find_nearest_fast(self, query_point):
        """
        TODO: Re-implement me with your faster solution.

        find_nearest_fast returns the point that is closest to query_point. If there are no indexed
        points, None is returned.
        """
        
        return self.tree.nearestNeighbor(query_point)

    def find_nearest(self, query_point):
        """
        find_nearest returns the point that is closest to query_point. If there are no indexed
        points, None is returned.
        """
        # TODO implement me so this class runs much faster.
        return self.tree.nearestNeighbor(query_point)