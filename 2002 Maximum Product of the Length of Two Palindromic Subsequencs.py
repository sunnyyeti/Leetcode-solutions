# Given a string s, find two disjoint palindromic subsequences of s such that the product of their lengths is maximized. The two subsequences are disjoint if they do not both pick a character at the same index.

# Return the maximum possible product of the lengths of the two palindromic subsequences.

# A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters. A string is palindromic if it reads the same forward and backward.

 

# Example 1:

# example-1
# Input: s = "leetcodecom"
# Output: 9
# Explanation: An optimal solution is to choose "ete" for the 1st subsequence and "cdc" for the 2nd subsequence.
# The product of their lengths is: 3 * 3 = 9.
# Example 2:

# Input: s = "bb"
# Output: 1
# Explanation: An optimal solution is to choose "b" (the first character) for the 1st subsequence and "b" (the second character) for the 2nd subsequence.
# The product of their lengths is: 1 * 1 = 1.
# Example 3:

# Input: s = "accbcaxxcxx"
# Output: 25
# Explanation: An optimal solution is to choose "accca" for the 1st subsequence and "xxcxx" for the 2nd subsequence.
# The product of their lengths is: 5 * 5 = 25.
 

# Constraints:

# 2 <= s.length <= 12
# s consists of lowercase English letters only.
from functools import cache
class Solution:
    def maxProduct(self, s: str) -> int:
        @cache
        def ispalindrome(mask):
            if mask== 0:
                return True,0
                
            left,right = None,None
            for j in range(length_s):
                if mask& (1<<j):
                    left = s[length_s-1-j]
                    break
            for k in range(length_s-1,-1,-1):
                if mask&(1<<k):
                    right = s[length_s-1-k]
                    break
            if j==k:
                return True, 1
            if left != right:
                return False, -1
            new_mask = mask&(mask-1)
            new_mask = new_mask & (~(1<<k))
            is_new_mask, new_mask_length = ispalindrome(new_mask)
            if is_new_mask:
                return True, new_mask_length+2
            return False, -1
        @cache
        def max_palindrome(mask):
            is_pal, length = ispalindrome(mask)
            if is_pal:
                return length
            max_length = 0
            new_mask = (mask-1)&mask
            while new_mask:
                is_pal,length = ispalindrome(new_mask)
                if is_pal:
                    max_length = max(max_length,length)
                new_mask = (new_mask-1)&mask
            return max_length  
        length_s = len(s)
        ans = float("-inf")
        for mask in range(1,1<<(length_s-1)):
            pair_mask = ~mask
            pair_mask &= (1<<length_s)-1
            l1,l2 = max_palindrome(pair_mask),max_palindrome(mask)
            if  l1*l2> ans:
                ans = l1*l2
        return ans
            