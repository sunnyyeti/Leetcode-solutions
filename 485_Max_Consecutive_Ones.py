
# Given a binary array, find the maximum number of consecutive 1s in this array.

# Example 1:
# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s.
#     The maximum number of consecutive 1s is 3.
# Note:

# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000
# Accepted
import itertools
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
         return max(map(lambda x: len(list(x[1])),
                        filter(lambda x:x[0]==1,itertools.groupby(nums))),
                    default=0)