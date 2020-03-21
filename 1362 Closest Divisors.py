# Given an integer num, find the closest two integers in absolute difference whose product equals num + 1 or num + 2.

# Return the two integers in any order.

 

# Example 1:

# Input: num = 8
# Output: [3,3]
# Explanation: For num + 1 = 9, the closest divisors are 3 & 3, for num + 2 = 10, the closest divisors are 2 & 5, hence 3 & 3 is chosen.
# Example 2:

# Input: num = 123
# Output: [5,25]
# Example 3:

# Input: num = 999
# Output: [40,25]
 

# Constraints:

# 1 <= num <= 10^9
import math
class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        def diff(n):
            a = int(math.sqrt(n))
            while n%a!=0:
                a-=1
            return abs(a-n//a),a,n//a
        dif1,a1,b1 = diff(num+1)
        dif2,a2,b2 = diff(num+2)
        if dif1<dif2:
            return [a1,b1]
        else:
            return [a2,b2]
        