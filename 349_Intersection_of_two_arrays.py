# Given two arrays, write a function to compute their intersection.

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        ans = []
        i,j = 0,0
        while i<len(nums1) and j<len(nums2):
            n1 = nums1[i]
            n2 = nums2[j]
            if n1 < n2:
                i+=1
            elif n1 > n2:
                j += 1
            else:
                ans.append(n1)
                while i<len(nums1) and nums1[i] == n1:
                    i+=1
                while j<len(nums2) and nums2[j] == n2:
                    j+=1
        return ans
