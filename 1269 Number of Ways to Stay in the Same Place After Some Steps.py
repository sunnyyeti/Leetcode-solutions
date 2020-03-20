# You have a pointer at index 0 in an array of size arrLen. At each step, you can move 1 position to the left, 1 position to the right in the array or stay in the same place  (The pointer should not be placed outside the array at any time).

# Given two integers steps and arrLen, return the number of ways such that your pointer still at index 0 after exactly steps steps.

# Since the answer may be too large, return it modulo 10^9 + 7.

 

# Example 1:

# Input: steps = 3, arrLen = 2
# Output: 4
# Explanation: There are 4 differents ways to stay at index 0 after 3 steps.
# Right, Left, Stay
# Stay, Right, Left
# Right, Stay, Left
# Stay, Stay, Stay
# Example 2:

# Input: steps = 2, arrLen = 4
# Output: 2
# Explanation: There are 2 differents ways to stay at index 0 after 2 steps
# Right, Left
# Stay, Stay
# Example 3:

# Input: steps = 4, arrLen = 2
# Output: 8
 

# Constraints:

# 1 <= steps <= 500
# 1 <= arrLen <= 10^6
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        R = 1000000007
        prow = [0]*arrLen
        prow[0]=prow[1] = 1
        for s in range(1,steps):
            crow = [0]*arrLen
            for ind in range(arrLen):
                if ind>0 and s==steps-1:
                    break
                crow[ind]+=prow[ind]%R
                if ind>0:
                    crow[ind]+=prow[ind-1]%R
                if ind<arrLen-1:
                    crow[ind]+=prow[ind+1]%R
                if crow[ind]==0:
                    break
            prow = crow
        return crow[0]%R