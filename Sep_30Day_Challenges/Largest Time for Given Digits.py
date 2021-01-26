# Given an array of 4 digits, return the largest 24 hour time that can be made.

# The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.

# Return the answer as a string of length 5.  If no valid time can be made, return an empty string.

 

# Example 1:

# Input: [1,2,3,4]
# Output: "23:41"
# Example 2:

# Input: [5,5,5,5]
# Output: ""
 

# Note:

# A.length == 4
# 0 <= A[i] <= 9
from itertools import permutations
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        all_times = permutations(A)
        all_times = filter(lambda l: l[0]*10+l[1]<=23 and l[2]*10+l[3]<=59,all_times)
        all_times = map(lambda l:str(l[0])+str(l[1])+":"+str(l[2])+str(l[3]),all_times)
        return max(all_times,default='')