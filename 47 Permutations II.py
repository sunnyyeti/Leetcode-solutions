# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

# Example 1:

# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
# Example 2:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

# Constraints:

# 1 <= nums.length <= 8
# -10 <= nums[i] <= 10
class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)==0:
            return []
        if len(nums)==1:
            return [nums]
        res = []
        occured = set()
        for i in range(len(nums)):
            if nums[i] not in occured:
                tmp = self.permuteUnique(nums[:i]+nums[i+1:])
                res.extend([ [nums[i]]+t for t in tmp ])
                occured.add(nums[i])
        return res
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def help(nums,l):
            cur_choices = set()
            if l==len(nums):
                ans.append(nums[:])
            else:
                for i in range(l,len(nums)):
                    if nums[i] not in cur_choices:
                        cur_choices.add(nums[i])
                        nums[l],nums[i]=nums[i],nums[l]
                        help(nums,l+1)
                        nums[l],nums[i]=nums[i],nums[l]
        help(nums,0)
        return ans
                    