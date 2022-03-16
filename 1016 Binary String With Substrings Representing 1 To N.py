# Given a binary string s (a string consisting only of '0' and '1's) and a positive integer n, return true if and only if for every integer x from 1 to n, the binary representation of x is a substring of s.

 

# Example 1:

# Input: s = "0110", n = 3
# Output: true
# Example 2:

# Input: s = "0110", n = 4
# Output: false
 

# Note:

# 1 <= s.length <= 1000
# 1 <= n <= 109
class Solution:
    def queryString(self, s: str, n: int) -> bool:
        return all(bin(i)[2:] in s for i in range(1, n+1))
