# Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

# You need to return the number of important reverse pairs in the given array.

# Example1:

# Input: [1,3,2,3,1]
# Output: 2
# Example2:

# Input: [2,4,3,5,1]
# Output: 3
# Note:
# The length of the given array will not exceed 50,000.
# All the numbers in the input array are in the range of 32-bit integer.
from sortedcontainers import SortedList
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.ans = 0
        self.merge_sort(nums,0,len(nums)-1)
        return self.ans
    def merge_sort(self,nums,start,end):
        if start>=end:
            return
        mid = (start+end)//2
        self.merge_sort(nums,start,mid)
        self.merge_sort(nums,mid+1,end)
        left = nums[start:mid+1]
        right = nums[mid+1:end+1]
        #rint("left:",left)
        #rint("right:",right)
        i,j = 0,0
        while i<len(left) and j<len(right):
            if left[i]>2*right[j]:
                self.ans += len(right)-j
                i+=1
            else:
                j+=1
        i,j,k = 0,0,0
        while i<len(left) and j<len(right):
            if left[i]>=right[j]:
                nums[start+k] = left[i]
                i+=1
            else:
                nums[start+k] = right[j]
                j+=1
            k+=1
        while i<len(left):
            nums[start+k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            nums[start+k]=right[j]
            j+=1
            k+=1
        #rint("nums:",nums)