# Given an array A of positive integers (not necessarily distinct), return the lexicographically largest permutation that is smaller than A, that can be made with one swap (A swap exchanges the positions of two numbers A[i] and A[j]).  If it cannot be done, then return the same array.

 

# Example 1:

# Input: [3,2,1]
# Output: [3,1,2]
# Explanation: Swapping 2 and 1.
# Example 2:

# Input: [1,1,5]
# Output: [1,1,5]
# Explanation: This is already the smallest permutation.
# Example 3:

# Input: [1,9,4,6,7]
# Output: [1,7,4,6,9]
# Explanation: Swapping 9 and 7.
# Example 4:

# Input: [3,1,1,3]
# Output: [1,3,1,3]
# Explanation: Swapping 1 and 3.
 

# Note:

# 1 <= A.length <= 10000
# 1 <= A[i] <= 10000
class Solution(object):
    def prevPermOpt1(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        stack =[]
        for i in range(len(A)-1,-1,-1):
            if not stack or A[i]<=stack[-1][1]:
                stack.append((i,A[i]))
            else:
                j = len(stack)-1
                tmp_max = stack[j][1]
                tmp_max_j = stack[j][0]
                while j>=0 and stack[j][1]<A[i]:
                    if stack[j][1]>tmp_max:
                        tmp_max = stack[j][1]
                        tmp_max_j=stack[j][0]
                    j-=1
                A[i],A[tmp_max_j]=A[tmp_max_j],A[i]
                return A
        return A