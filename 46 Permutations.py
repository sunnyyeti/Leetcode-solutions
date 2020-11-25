# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:

# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:

# Input: nums = [1]
# Output: [[1]]
 

# Constraints:

# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def help(nums,l):
            if l==len(nums):
                ans.append(nums[:])
            else:
                for i in range(l,len(nums)):
                    nums[l],nums[i]=nums[i],nums[l]
                    help(nums,l+1)
                    nums[l],nums[i]=nums[i],nums[l]
        help(nums,0)
        return ans
                    
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)==1 or len(nums)==0:
            return [nums]
        res = []
        for i in range(len(nums)):
            tmp = self.permute(nums[:i]+nums[i+1:])
            res.extend([ [nums[i]]+t for t in tmp ])
        return res
        