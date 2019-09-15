# Write a program to find the n-th ugly number.

# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

# Example:

# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
# Note:  

# 1 is typically treated as an ugly number.
# n does not exceed 1690.
from collections import deque
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        d = deque([1])
        uglys = {1}
        cnt = 1
        max_c=float("-inf")
        while d:
            cur = d.popleft()
            for m in [2,3,5]:
                if cur*m not in uglys:
                    if cnt<n or cur*m<max_c:
                        uglys.add(cur*m)
                        d.append(cur*m)
                        cnt+=1
                        max_c = max(max_c,cur*m)
        return sorted(uglys)[n-1]
                        
            