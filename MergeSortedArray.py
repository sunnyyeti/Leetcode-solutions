# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

# The number of elements initialized in nums1 and nums2 are m and n respectively. You may assume that nums1 has a size equal to m + n such that it has enough space to hold additional elements from nums2.

 

# Example 1:

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Example 2:

# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
 

# Constraints:

# nums1.length == m + n
# nums2.length == n
# 0 <= m, n <= 200
# 1 <= m + n <= 200
# -109 <= nums1[i], nums2[i] <= 109
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        id1 = m-1
        id2 = n-1
        k = len(nums1)-1
        while id1>=0 and id2>=0:
            if nums1[id1]>nums2[id2]:
                nums1[k] = nums1[id1]
                id1-=1
            else:
                nums1[k] = nums2[id2]
                id2-=1
            k-=1
        while id1>=0:
            nums1[k] = nums1[id1]
            id1-=1
            k-=1
        while id2>=0:
            nums1[k] = nums2[id2]
            id2-=1
            k-=1
            