

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Example 2:

# Input: nums = []
# Output: []
# Example 3:

# Input: nums = [0]
# Output: []
 

# Constraints:

# 0 <= nums.length <= 3000
# -105 <= nums[i] <= 105
from itertools import product
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        store = {}
        for i,n in enumerate(nums):
            store.setdefault(n,[]).append(i)
        ans = set()
        #keys = list(store.keys())
        for i in store.keys():
            i_list = store[i]
            for j in store.keys():
                j_list = store[j]
                k = -i-j
                k_list = store.get(k,[])
                for ii,jj,kk in product(i_list,j_list,k_list):
                    if ii!=jj and ii!=kk and jj!=kk:
                        ans.add(tuple(sorted([i,j,k])))
                        break
                
        return [list(a)  for a in ans]
                