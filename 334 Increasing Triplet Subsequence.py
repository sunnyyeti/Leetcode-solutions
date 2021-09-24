# Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 

# Example 1:

# Input: nums = [1,2,3,4,5]
# Output: true
# Explanation: Any triplet where i < j < k is valid.
# Example 2:

# Input: nums = [5,4,3,2,1]
# Output: false
# Explanation: No triplet exists.
# Example 3:

# Input: nums = [2,1,5,0,4,6]
# Output: true
# Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
 

# Constraints:

# 1 <= nums.length <= 5 * 105
# -231 <= nums[i] <= 231 - 1
 

# Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?
import bisect


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first, second = None, None
        for n in nums:
            if first is None:
                first = n
            elif second is None:
                if n <= first:
                    first = n
                else:
                    second = n
            else:
                if n > second:
                    return True
                elif first < n <= second:
                    second = n
                else:
                    first = n
        return False

    def lsi(self, nums: List[int]) -> bool:
        # find the longest increasing subsequence
        # check if the length is greater than or equal to 3
        lis = []
        ans = 1
        for n in nums:
            if not lis or n > lis[-1]:
                lis.append(n)
                ans = max(ans, len(lis))
                if ans >= 3:
                    return True
            else:
                insert_pos = bisect.bisect_left(lis, n)
                lis[insert_pos] = n
                ans = max(ans, insert_pos+1)
                if ans >= 3:
                    return True
        return False
