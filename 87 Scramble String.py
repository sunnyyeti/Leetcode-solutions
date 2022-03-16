# We can scramble a string s to get a string t using the following algorithm:

# If the length of the string is 1, stop.
# If the length of the string is > 1, do the following:
# Split the string into two non-empty substrings at a random index, i.e., if the string is s, divide it to x and y where s = x + y.
# Randomly decide to swap the two substrings or to keep them in the same order. i.e., after this step, s may become s = x + y or s = y + x.
# Apply step 1 recursively on each of the two substrings x and y.
# Given two strings s1 and s2 of the same length, return true if s2 is a scrambled string of s1, otherwise, return false.

 

# Example 1:

# Input: s1 = "great", s2 = "rgeat"
# Output: true
# Explanation: One possible scenario applied on s1 is:
# "great" --> "gr/eat" // divide at random index.
# "gr/eat" --> "gr/eat" // random decision is not to swap the two substrings and keep them in order.
# "gr/eat" --> "g/r / e/at" // apply the same algorithm recursively on both substrings. divide at ranom index each of them.
# "g/r / e/at" --> "r/g / e/at" // random decision was to swap the first substring and to keep the second substring in the same order.
# "r/g / e/at" --> "r/g / e/ a/t" // again apply the algorithm recursively, divide "at" to "a/t".
# "r/g / e/ a/t" --> "r/g / e/ a/t" // random decision is to keep both substrings in the same order.
# The algorithm stops now and the result string is "rgeat" which is s2.
# As there is one possible scenario that led s1 to be scrambled to s2, we return true.
# Example 2:

# Input: s1 = "abcde", s2 = "caebd"
# Output: false
# Example 3:

# Input: s1 = "a", s2 = "a"
# Output: true
 

# Constraints:

# s1.length == s2.length
# 1 <= s1.length <= 30
# s1 and s2 consist of lower-case English letters.
from functools import cache

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @cache
        def is_same(i1,j1,i2,j2):
            if j1==i1:
                return s1[i1:j1+1]==s2[i2:j2+1]
            for k in range(i1,j1):
                same_no_swap = is_same(i1,k,i2,i2+k-i1) and is_same(k+1,j1,i2+k-i1+1,j2)
                if same_no_swap:
                    return True
                same_swap = is_same(i1,k, j2-(k-i1),j2) and is_same(k+1,j1,i2,i2+j1-k-1)
                if same_swap:
                    return True
            return False

        return is_same(0,len(s1)-1,0,len(s2)-1)