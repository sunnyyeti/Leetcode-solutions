# Given an array A of integers, a ramp is a tuple (i, j) for which i < j and A[i] <= A[j].  The width of such a ramp is j - i.

# Find the maximum width of a ramp in A.  If one doesn't exist, return 0.

 

# Example 1:

# Input: [6,0,8,2,1,5]
# Output: 4
# Explanation: 
# The maximum width ramp is achieved at (i, j) = (1, 5): A[1] = 0 and A[5] = 5.
# Example 2:

# Input: [9,8,1,0,1,9,4,0,4,1]
# Output: 7
# Explanation: 
# The maximum width ramp is achieved at (i, j) = (2, 9): A[2] = 1 and A[9] = 1.
 

# Note:

# 2 <= A.length <= 50000
# 0 <= A[i] <= 50000

class Solution:
    def maxWidthRamp(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        return self.two_for_loops(A)

    def two_for_loops(self,A):
        """
        Time limit exceeded
        :param A:
        :return:
        """
        end_max = [A[-1]]*len(A)
        for j in range(len(A)-2,-1,-1):
            end_max[j] = max(A[j],end_max[j+1])
        max_length = 0
        for i,a in enumerate(A):
            if i+max_length+1<len(A) and a<=end_max[i+max_length+1]:
                for j in range(len(A)-1,i+max_length,-1):
                    if A[j]>=a:
                        max_length = max(max_length,j-i)
                        break
        return max_length

    def dp(self,start,end):
        """
        time limit exceeded
        :param start:
        :param end:
        :return:
        """
        if (start,end) in self.cache:
            return self.cache[(start,end)]
        if self.A[start]<=self.A[end]:
            self.cache[(start,end)]=end-start
            return end-start
        else:
            return max(self.dp(start+1,end),self.dp(start,end-1))