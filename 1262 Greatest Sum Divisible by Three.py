# Given an array nums of integers, we need to find the maximum possible sum of elements of the array such that it is divisible by three.

 

# Example 1:

# Input: nums = [3,6,5,1,8]
# Output: 18
# Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).
# Example 2:

# Input: nums = [4]
# Output: 0
# Explanation: Since 4 is not divisible by 3, do not pick any number.
# Example 3:

# Input: nums = [1,2,3,4,4]
# Output: 12
# Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).
 

# Constraints:

# 1 <= nums.length <= 4 * 10^4
# 1 <= nums[i] <= 10^4
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [[0,0,0] for _ in nums]
        if nums[-1]%3==0:
            dp[-1] = [nums[-1],float("-inf"),float("-inf")]
        elif nums[-1]%3==1:
            dp[-1] = [0,nums[-1],float("-inf")]
        else:
            dp[-1] = [0,float("-inf"),nums[-1]]
        for i in range(len(nums)-2,-1,-1):
            cur = nums[i]%3
            for r in range(3):
                n = (r+cur)%3
                dp[i][n] = max(dp[i+1][r]+nums[i],dp[i+1][n])
                
        #print(dp)
        return dp[0][0]