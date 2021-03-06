# Given an array A of positive integers, A[i] represents the value of the i-th sightseeing spot, and two sightseeing spots i and j have distance j - i between them.

# The score of a pair (i < j) of sightseeing spots is (A[i] + A[j] + i - j) : the sum of the values of the sightseeing spots, minus the distance between them.

# Return the maximum score of a pair of sightseeing spots.

 

# Example 1:

# Input: [8,1,5,2,6]
# Output: 11
# Explanation: i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11
 

# Note:

# 2 <= A.length <= 50000
# 1 <= A[i] <= 1000
# Accepted
# 5.9K
# Submissions
# 12.4K
class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        ans = float("-inf")
        ref_ind = 0
        ref_val = A[ref_ind]
        for cur_ind in range(1,len(A)):
            cur_val = A[cur_ind]
            candidate = cur_val+ref_val+ref_ind-cur_ind
            if candidate>ans:
                ans = candidate
            if cur_val+cur_ind>=ref_val+ref_ind:
                ref_val = cur_val
                ref_ind = cur_ind
        return ans
            
        