# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

# Find all the elements that appear twice in this array.

# Could you do it without extra space and in O(n) runtime?

# Example:
# Input:
# [4,3,2,7,8,2,3,1]

# Output:
# [2,3]
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for i,n in enumerate(nums):
            cur = n
            if n not in {0,-1}:
                nums[i] = -1 # the element has been considered
                while cur not in {0,-1} and nums[cur-1]!=0:
                    n = nums[cur-1]
                    nums[cur-1] = 0
                    cur = n
                if cur>0:
                    ans.append(cur)
        return ans