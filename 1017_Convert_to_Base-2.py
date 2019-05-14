# Given a number N, return a string consisting of "0"s and "1"s that represents its value in base -2 (negative two).

# The returned string must have no leading zeroes, unless the string is "0".

 

# Example 1:

# Input: 2
# Output: "110"
# Explantion: (-2) ^ 2 + (-2) ^ 1 = 2
# Example 2:

# Input: 3
# Output: "111"
# Explantion: (-2) ^ 2 + (-2) ^ 1 + (-2) ^ 0 = 3
# Example 3:

# Input: 4
# Output: "100"
# Explantion: (-2) ^ 2 = 4
 

# Note:

# 0 <= N <= 10^9
class Solution(object):
    def baseNeg2(self, N):
        """
        :type N: int
        :rtype: str
        """
        if N==0:
            return "0"
        ans = []
        while N not in [0,1]:
            if (N-1)%(-2)==0:
                ans.append(1)
                N = (N-1)//(-2)
            else:
                ans.append(0)
                N = N//-2
        ans.append(N)
        return "".join(map(str,ans[::-1])).lstrip("0")