# Given a string s, return the number of substrings of length k with no repeated characters.

 

# Example 1:

# Input: s = "havefunonleetcode", k = 5
# Output: 6
# Explanation: 
# There are 6 substrings they are : 'havef','avefu','vefun','efuno','etcod','tcode'.
# Example 2:

# Input: s = "home", k = 5
# Output: 0
# Explanation: 
# Notice k can be larger than the length of s. In this case is not possible to find any substring.
 

# Note:

# 1 <= s.length <= 104
# All characters of s are lowercase English letters.
# 1 <= k <= 104
from collections import Counter


class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        i, j = 0, k-1
        window = Counter(s[i:j+1])
        number_of_substrings = 0
        while True:
            if len(window) == k:
                number_of_substrings += 1
            chari = s[i]
            window[chari] -= 1
            if window[chari] == 0:
                del window[chari]
            i += 1
            j += 1
            if j >= len(s):
                break
            charj = s[j]
            window[charj] += 1
        return number_of_substrings
