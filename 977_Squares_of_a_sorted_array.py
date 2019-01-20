# Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

 

# Example 1:

# Input: [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Example 2:

# Input: [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
 

# Note:

# 1 <= A.length <= 10000
# -10000 <= A[i] <= 10000
# A is sorted in non-decreasing order.
class Solution:
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res = [0]*len(A)
        i = 0
        j = len(A)-1
        k = j
        while A[i]<=0 and A[j]>0:
            if abs(A[j])>abs(A[i]):
                res[k] = A[j]**2
                j-=1
            else:
                res[k] = A[i]**2
                i+=1
            k-=1
        if A[i]>0:
            while j>=i:
                res[k]=A[j]**2
                j-=1
                k-=1
        if A[j]<=0:
            while i<=j:
                res[k]=A[i]**2
                i+=1
                k-=1
        return res