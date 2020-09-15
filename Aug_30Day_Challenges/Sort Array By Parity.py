# Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

# You may return any answer array that satisfies this condition.

 

# Example 1:

# Input: [3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
 

# Note:

# 1 <= A.length <= 5000
# 0 <= A[i] <= 5000
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        odd_index = len(A)-1
        cur_index = 0
        while cur_index <= odd_index:
            cur_ele = A[cur_index]
            if cur_ele & 1:
                A[cur_index],A[odd_index] = A[odd_index], A[cur_index]
                odd_index -= 1
            else:
                cur_index += 1
        return A