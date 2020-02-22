# Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

# Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

# Example:

# Input:
# [[0,0],[1,0],[2,0]]

# Output:
# 2

# Explanation:
# The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
import math
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        if len(points)<3:
            return 0
        hash_table = {}
        for i in range(len(points)-1):
            for j in range(i+1,len(points)):
                pi = points[i]
                pj = points[j]
                dis = (pi[0]-pj[0])**2+(pi[1]-pj[1])**2
                sub = hash_table.setdefault(i,{})
                sub[dis] = sub.get(dis,0)+1
                sub = hash_table.setdefault(j,{})
                sub[dis] = sub.get(dis,0)+1
        cnt = 0
        for i in range(len(points)):
            sub = hash_table[i]
            for key in sub.keys():
                cnt+=sub[key]*(sub[key]-1)
        return cnt
            