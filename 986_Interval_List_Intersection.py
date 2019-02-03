# Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

# Return the intersection of these two interval lists.

# (Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

 

# Example 1:



# Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
# Reminder: The inputs and the desired output are lists of Interval objects, and not arrays or lists.
 

# Note:

# 0 <= A.length < 1000
# 0 <= B.length < 1000
# 0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def intervalIntersection(self, A: 'List[Interval]', B: 'List[Interval]') -> 'List[Interval]':
        if not A or not B:
            return []
        result = []
        i=j=0
        target = A[0]
        comp = 1
        while i<len(A) and j<len(B):
            if comp:
                if B[j].start>target.end:
                    target = B[j]
                    comp = 0
                    i+=1
                elif B[j].end<target.start:
                    j+=1
                else:
                    result.append(Interval(max(target.start,B[j].start),min(target.end,B[j].end)))
                    if B[j].end>target.end:
                        target = B[j]
                        comp = 0
                        i+=1
                    else:
                        j+=1
            else:
                if A[i].start>target.end:
                    target = A[i]
                    comp = 1
                    j+=1
                elif A[i].end<target.start:
                    i+=1
                else:
                    result.append(Interval(max(target.start,A[i].start),min(target.end,A[i].end)))
                    if A[i].end>target.end:
                        target = A[i]
                        comp = 1
                        j+=1
                    else:
                        i+=1
        return result
        