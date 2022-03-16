# A positive integer is magical if it is divisible by either a or b.

# Given the three integers n, a, and b, return the nth magical number. Since the answer may be very large, return it modulo 109 + 7.

 

# Example 1:

# Input: n = 1, a = 2, b = 3
# Output: 2
# Example 2:

# Input: n = 4, a = 2, b = 3
# Output: 6
# Example 3:

# Input: n = 5, a = 2, b = 4
# Output: 10
# Example 4:

# Input: n = 3, a = 6, b = 4
# Output: 8
 

# Constraints:

# 1 <= n <= 109
# 2 <= a, b <= 4 * 104
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        def gcd(a,b):
            if a<b:
                a,b = b,a
            while b:
                a,b = b,a%b
            return a
        def lcm(a,b):
            return a*b//gcd(a,b)
        m = lcm(a,b)
        #print(m)
        left = min(a,b)
        right = max(a,b)*n
        while left <= right:
            mid = (left+right)//2
            cnt = mid//a+mid//b-mid//m
            if cnt < n:
                left = mid + 1
            else:
                right = mid-1
        return left%(10**9+7)
                
            