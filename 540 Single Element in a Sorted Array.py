# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

 

# Example 1:

# Input: [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:

# Input: [3,3,7,7,10,11,11]
# Output: 10
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        i,j = 0,len(nums)-1
        while i<j:
            mid = (i+j)//2
            if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
                return nums[mid]
            elif nums[mid]==nums[mid-1]:
                if (mid-1)%2==0:
                    i = mid+1
                else:
                    j = mid-2
            else:
                if mid%2==0:
                    i = mid+2
                else:
                    j = mid-1
        return nums[i]