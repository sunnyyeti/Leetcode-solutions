# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

# You are given a target value to search. If found in the array return true, otherwise return false.

# Example 1:

# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
# Example 2:

# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false
# Follow up:

# This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
# Would this affect the run-time complexity? How and why?
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        start, end = 0, len(nums)-1
        while start<=end:
            mid =  (start+end)//2
            if target == nums[mid]:
                return True
            if nums[mid] < nums[end]: #mid is in smaller half
                if target > nums[end]:
                    end = mid - 1
                elif nums[mid]<target<=nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
            elif nums[mid] > nums[end]: #mid is in larger half
                if target < nums[start]:
                    start = mid + 1
                elif nums[start]<=target<nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid]!=nums[start]: #[1,3,1,1,1] [1,1,1,0,1] [1,1,3,1] [1,1,1,3,1]
                    end = mid - 1
                else:
                    latter_same = True
                    for j in range(mid+1,end):
                        if nums[j] != nums[end]:
                            latter_same = False
                            break
                    if latter_same:
                        end = mid-1
                    else:
                        start = mid+1
        return False