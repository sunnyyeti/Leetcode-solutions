# We have two integer sequences nums1 and nums2 of the same non-zero length.

# We are allowed to swap elements nums1[i] and nums2[i]. Note that both elements are in the same index position in their respective sequences.

# At the end of some number of swaps, nums1 and nums2 are both strictly increasing. (An array A is strictly increasing if and only if A[0] < A[1] < A[2] < ... < A[A.length - 1].)

# Given nums1 and nums2, return the minimum number of swaps to make both sequences strictly increasing. It is guaranteed that the given input always makes it possible.

# Example:
# Input: nums1 = [1,3,5,4], nums2 = [1,2,3,7]
# Output: 1
# Explanation: 
# Swap nums1[3] and nums2[3].  Then the sequences are:
# nums1 = [1, 3, 5, 7] and nums2 = [1, 2, 3, 4]
# which are both strictly increasing.
# Note:

# nums1, nums2 are arrays with the same length, and that length will be in the range [1, 1000].
# nums1[i], nums2[i] are integer values in the range [0, 2000].
from functools import cache


class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        # @cache
        # def help(ind,swap):
        #     if ind == 0:
        #         return int(swap)
        #     c1 = nums1[ind]
        #     c2 = nums2[ind]
        #     p1 = nums1[ind-1]
        #     p2 = nums2[ind-1]
        #     if not swap:
        #         min_ = float('inf')
        #         if c1>p1 and c2>p2:
        #             min_ = min(min_,help(ind-1,False))
        #         if c1>p2 and c2>p1:
        #             min_ = min(min_,help(ind-1,True))
        #         return min_
        #     else:
        #         min_ = float('inf')
        #         if c1>p2 and c2>p1:
        #             min_ = min(min_,help(ind-1,False))+1
        #         if c1>p1 and c2>p2:
        #             min_ = min(min_,help(ind-1,True))+1
        #         return min_
        # return min(help(len(nums1)-1,True),help(len(nums1)-1,False))
        dp = [[0, 0] for _ in nums1]
        # swap not-swap
        dp[0] = [1, 0]
        for ind in range(1, len(nums1)):
            c1 = nums1[ind]
            c2 = nums2[ind]
            p1 = nums1[ind-1]
            p2 = nums2[ind-1]
            # not swap
            min_ = float('inf')
            if c1 > p1 and c2 > p2:
                min_ = min(min_, dp[ind-1][1])
            if c1 > p2 and c2 > p1:
                min_ = min(min_, dp[ind-1][0])
            dp[ind][1] = min_
            #swap
            min_ = float('inf')
            if c1 > p2 and c2 > p1:
                min_ = min(min_, dp[ind-1][1]+1)
            if c1 > p1 and c2 > p2:
                min_ = min(min_, dp[ind-1][0]+1)
            dp[ind][0] = min_
            #print(dp)
        return min(dp[-1])
