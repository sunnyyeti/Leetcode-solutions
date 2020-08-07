# Given a set of distinct integers, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.

# Example:

# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
import itertools
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        max_v = 2**n
        ans = []
        for i in range(max_v):
            bin_i = bin(i)[2:]
            bin_i = '0'*(len(nums)-len(bin_i))+bin_i
            row = [n for n,b in zip(nums,bin_i) if b=='1']
            ans.append(row)
        return ans
             