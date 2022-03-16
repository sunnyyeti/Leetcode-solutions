# Given a string s and an integer k, return true if s is a k-palindrome.

# A string is k-palindrome if it can be transformed into a palindrome by removing at most k characters from it.

 

# Example 1:

# Input: s = "abcdeca", k = 2
# Output: true
# Explanation: Remove 'b' and 'e' characters.
# Example 2:

# Input: s = "abbababa", k = 1
# Output: true
 

# Constraints:

# 1 <= s.length <= 1000
# s consists of only lowercase English letters.
# 1 <= k <= s.length
from functools import cache


class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        @cache
        def isPalindromeHelper(start, end, k):
            if start >= end:
                return True
            if k == 0:
                while start <= end:
                    if s[start] == s[end]:
                        start += 1
                        end -= 1
                    else:
                        return False
                return True
            if isPalindromeHelper(start+1, end, k-1):
                return True
            if isPalindromeHelper(start, end-1, k-1):
                return True
            if s[start] == s[end] and isPalindromeHelper(start+1, end-1, k):
                return True
            if k > 1:
                if isPalindromeHelper(start+1, end-1, k-2):
                    return True
            return False
        return isPalindromeHelper(0, len(s)-1, k)
