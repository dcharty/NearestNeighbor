"""nn_search_test"""

import random
import time
import unittest
import sys
import math
sys.path.append('../NEARESTNEIGHBOR')
from pynn import NearestNeighborIndex
from pynn import KDTree


class NearestNeighborIndexTest(unittest.TestCase):
    def test_basic(self):
        """
        test_basic tests a handful of nearest neighbor queries to make sure they return the right
        result.
        """

        test_points = [
            (1, 2),
            (1, 0),
            (10, 5),
            (-1000, 20),
            (3.14159, 42),
            (42, 3.14159),
        ]

        uut = NearestNeighborIndex(test_points)

        self.assertEqual((1, 0), uut.find_nearest((0, 0)))
        self.assertEqual((-1000, 20), uut.find_nearest((-2000, 0)))
        self.assertEqual((42, 3.14159), uut.find_nearest((40, 3)))

    def test_benchmark(self):
        """
        test_benchmark tests a bunch of values using the slow and fast version of the index
        to determine the effective speedup.
        """

        def rand_point():
            return (random.uniform(-1000, 1000), random.uniform(-1000, 1000))

        index_points = [rand_point() for _ in range(10000)]
        query_points = [rand_point() for _ in range(1000)]

        expected = []
        actual = []

        # Run the baseline slow tests to get the expected values.
        start = time.time()
        for query_point in query_points:
            expected.append(NearestNeighborIndex.find_nearest_slow(query_point, index_points))
        slow_time = time.time() - start

        # don't include the indexing time when benchmarking
        uut = NearestNeighborIndex(index_points)

        # Run the indexed tests
        start = time.time()
        for query_point in query_points:
            actual.append(uut.find_nearest(query_point))
        new_time = time.time() - start

        print(f"slow time: {slow_time:0.2f}sec")
        print(f"new time: {new_time:0.2f}sec")
        print(f"speedup: {(slow_time / new_time):0.2f}x")
        
    # TODO: Add more test cases to ensure your index works in different scenarios
    #added test case to see if fast version of nearest neighbor is equal or better
    #than the slow way of doing it.
        for actualPoints in index_points:
            self.assertEqual(actualPoints, uut.find_nearest(actualPoints))
        for query_point in query_points:
            nodeFast= uut.find_nearest(query_point)
            nodeSlow = NearestNeighborIndex.find_nearest_slow(query_point, index_points)
            distanceFast = math.sqrt((query_point[0]-nodeFast[0])**2+(query_point[1]-nodeFast[1])**2)
            distanceSlow = math.sqrt((query_point[0]-nodeSlow[0])**2+(query_point[1]-nodeSlow[1])**2)
            tempMsg = [query_point,nodeFast,nodeSlow,distanceFast,distanceSlow]
            self.assertTrue(distanceFast<=distanceSlow,msg=tempMsg)
    def test_Null(self):
            """
            test_null tests if the tree returns None when empty
            """
            uut = KDTree()
            self.assertTrue(uut.nearestNeighbor((1, 2))==None)