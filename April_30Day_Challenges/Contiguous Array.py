# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

# Example 1:
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
# Example 2:
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
# Note: The length of the given binary array will not exceed 50,000.
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # end1 - start1 = end0 - start0
        # end1 - end0 = start1 - start 0 
        record = {0:0}
        sum0 = 0
        sum1 = 0
        max_length  = 0
        for i,n in enumerate(nums,start=1):
            sum1 += n==1
            sum0 += n==0
            dif = sum1-sum0
            if dif in record:
                max_length = max(max_length,i-record[dif])
            else:
                record[dif] = i
        return max_length
            