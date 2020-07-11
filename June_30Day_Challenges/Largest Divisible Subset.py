# Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

# Si % Sj = 0 or Sj % Si = 0.

# If there are multiple solutions, return any subset is fine.

# Example 1:

# Input: [1,2,3]
# Output: [1,2] (of course, [1,3] will also be ok)
# Example 2:

# Input: [1,2,4,8]
# Output: [1,2,4,8]
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        nums.sort()
        dp = [tuple() for _ in nums]
        dp[-1] = (len(nums)-1,1)
        gind = len(nums)-1
        gmax = 1
        for i in range(len(nums)-2,-1,-1):
            p,mp = i,0
            for j in range(i+1,len(nums)):
                if nums[j]%nums[i]==0:
                    if dp[j][1]>mp:
                        mp = dp[j][1]
                        p = j
            dp[i] = (p,1+mp)
            if dp[i][1]>gmax:
                gmax = dp[i][1]
                gind = i
                
        ans = [nums[gind]]
        while dp[gind][0]!=gind:
            gind = dp[gind][0]
            ans.append(nums[gind])
        return ans