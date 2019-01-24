# We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

# (Here, the distance between two points on a plane is the Euclidean distance.)

# You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

 

# Example 1:

# Input: points = [[1,3],[-2,2]], K = 1
# Output: [[-2,2]]
# Explanation: 
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
# Example 2:

# Input: points = [[3,3],[5,-1],[-2,4]], K = 2
# Output: [[3,3],[-2,4]]
# (The answer [[-2,4],[3,3]] would also be accepted.)
 

# Note:

# 1 <= K <= points.length <= 10000
# -10000 < points[i][0] < 10000
# -10000 < points[i][1] < 10000
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        return self.quick_select(points, K)

    def sort_method(self, points, K):
        distances = list(map(lambda x: x[0] ** 2 + x[1] ** 2, points))
        index = sorted(range(len(points)), key=lambda x: distances[x])
        return [points[index[i]] for i in range(K)]

    def max_heap_method(self, points, K):
        import heapq
        points_distance = list(map(lambda x: (-x[0] ** 2 - x[1] ** 2, x), points))
        first_k_points = points_distance[:K]
        heapq.heapify(first_k_points)
        for i in range(K, len(points)):
            if points_distance[i][0] > first_k_points[0][0]:
                heapq.heapreplace(first_k_points, points_distance[i])
        return [x[1] for x in first_k_points]

    def min_heap_method(self, points, K):
        import heapq
        points = list(map(lambda x: (x[0] ** 2 + x[1] ** 2, x), points))
        heapq.heapify(points)
        res = []
        for i in range(K):
            res.append(heapq.heappop(points)[1])
        return res

    def quick_select(self, points, K):
        def helper(points, K, start, end):
            i = j = start
            pivot = points[end]
            while j < end:
                if points[j][0] <= pivot[0]:
                    points[i], points[j] = points[j], points[i]
                    i += 1
                    j += 1
                else:
                    j += 1
            points[i], points[end] = points[end], points[i]
            if i - start + 1 == K:
                return points[start:start + K]
            if i - start + 1 > K:
                return helper(points, K, start, i - 1)
            if i - start + 1 < K:
                return points[start:i + 1] + helper(points, K - i + start - 1, i + 1, end)

        points = list(map(lambda x: (x[0] ** 2 + x[1] ** 2, x), points))
        res = helper(points, K, 0, len(points) - 1)
        return [x[1] for x in res]