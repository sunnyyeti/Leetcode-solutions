# A peak element is an element that is strictly greater than its neighbors.

# Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

# You may imagine that nums[-1] = nums[n] = -∞.

# You must write an algorithm that runs in O(log n) time.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.
# Example 2:

# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
 

# Constraints:

# 1 <= nums.length <= 1000
# -231 <= nums[i] <= 231 - 1
# nums[i] != nums[i + 1] for all valid i.
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def get(ind):
            if 0<=ind<len(nums):
                return nums[ind]
            return float('-inf')
        def slope(ind):
            if get(ind) > get(ind-1) and get(ind)>get(ind+1):
                return 0
            elif get(ind-1) < get(ind) < get(ind+1):
                return 1
            elif get(ind-1) > get(ind) > get(ind+1):
                return -1
            else:
                return 2
        left, right = 0, len(nums)-1
        while left<=right:
            mid = (left+right)//2
            mid_slope = slope(mid)
            if mid_slope==0:
                return mid
            elif mid_slope == 1:
                left = mid + 1
            elif mid_slope == -1:
                right = mid - 1
            else:
                right = mid -1
        