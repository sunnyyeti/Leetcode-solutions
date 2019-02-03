# Given an array of integers A, a move consists of choosing any A[i], and incrementing it by 1.

# Return the least number of moves to make every value in A unique.

 

# Example 1:

# Input: [1,2,2]
# Output: 1
# Explanation:  After 1 move, the array could be [1, 2, 3].
# Example 2:

# Input: [3,2,1,2,1,7]
# Output: 6
# Explanation:  After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
# It can be shown with 5 or less moves that it is impossible for the array to have all unique values.
 

# Note:

# 0 <= A.length <= 40000
# 0 <= A[i] < 40000
from collections import defaultdict
class Solution:
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return 0
        cnt = defaultdict(lambda:0)
        for a in A:
            cnt[a]+=1
        incre = 0
        i = min(A)
        max_v = max(A)
        while i<max_v:
            if cnt[i]>1:
                cnt[i+1] += cnt[i]-1
                incre += cnt[i]-1
            i+=1
        if cnt[i]>1:
            incre+= (cnt[i]-1)*cnt[i]//2
        return incre
        
        
        