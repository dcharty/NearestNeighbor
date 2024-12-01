import math

def fakedistance(point1,point2):
        #FakeDistance returns the euclidean distance between two points just without the square root
        # This is because the squareroot is not needed when comparing two distances and because
        #square root takes a lot of extra cycles. Just small optimization. 
        return (point1[0]-point2[0])**2+(point1[0]-point2[0])**2

def closest(point,node1,node2):
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
    #dimensions variable. can be changed but is static right now for this.
    k=2
    def __init__(self):
        self.head = none
    #recursive function for insert
    def insertRecursion(self,parent,point,depth):
        if not parent:
            return node(point)
        axis = depth%k
        #basic binary-tree style check to see where point will go
        if point[axis] < parent.point[axis]:
            parent.left = insert(parent.left,point,depth+1)
        else:
            parent.right = insert(parent.right,point,depth+1)
        return parent
    #insert start function
    def insert(self,point):
        return insertRecursion(self.head,point,0)
    #recursive Function for nearest neighbor search
    def nearestNeighborRecursion(self,parent,point,depth):
        if parent ==None:
            return
        axis = depth%k
        if point[axis] < parent.point[axis]:
            firstBranch = parent.left
            laterBranch = parent.right
        else:
            firstBranch = parent.right
            laterBranch = parent.left
        temp = nearestNeighborRecursion(firstBranch,point,depth+1)
        best = closest(point,temp,parent)
        
        radiusSquared = fakedistance(point,best.point)
        dist = point[axis]-parent.point[axis]
        if(radiusSquared >= dist*dist):
            temp = nearestNeighborRecursion(laterBranch,point,depth+1)
            best =  closest(point,temp,parent)
        return best
    #nearestNeighbor Start function
    def nearestNeighbor(self,point):
        if(self.head==None):
            return None
        return nearestNeighborRecursion(self.head,point,0)

class NearestNeighborIndex:
    """
    TODO give me a decent comment

    NearestNeighborIndex is intended to index a set of provided points to provide fast nearest
    neighbor lookup. For now, it is simply a stub that performs an inefficient traversal of all
    points every time.
    """

    def __init__(self, points):
        """
        takes an array of 2d tuples as input points to be indexed.
        """
        self.points = points

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

        min_dist = None
        min_point = None

        for point in self.points:
            deltax = point[0] - query_point[0]
            deltay = point[1] - query_point[1]
            dist = math.sqrt(deltax * deltax + deltay * deltay)
            if min_dist is None or dist < min_dist:
                min_dist = dist
                min_point = point

        return min_point

    def find_nearest(self, query_point):
        """
        TODO comment me.
        """

        # TODO implement me so this class runs much faster.
        return self.find_nearest_fast(query_point)
