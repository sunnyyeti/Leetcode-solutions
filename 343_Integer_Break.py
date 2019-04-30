# Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

# Example 1:

# Input: 2
# Output: 1
# Explanation: 2 = 1 + 1, 1 × 1 = 1.
# Example 2:

# Input: 10
# Output: 36
# Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        max_ans = float("-inf")
        for k in range(2,n+1):
            new_p = self.break_p(n,k)
            if new_p<max_ans:
                return max_ans
            max_ans = new_p
        return max_ans
        
    def break_p(self,n,k):
        can = n//k
        remain = n-can*k
        ans = pow(can,k-remain)*pow((can+1),remain)
        return ans