# Strings s1 and s2 are k-similar (for some non-negative integer k) if we can swap the positions of two letters in s1 exactly k times so that the resulting string equals s2.

# Given two anagrams s1 and s2, return the smallest k for which s1 and s2 are k-similar.

 

# Example 1:

# Input: s1 = "ab", s2 = "ba"
# Output: 1
# Example 2:

# Input: s1 = "abc", s2 = "bca"
# Output: 2
# Example 3:

# Input: s1 = "abac", s2 = "baca"
# Output: 2
# Example 4:

# Input: s1 = "aabc", s2 = "abca"
# Output: 2
 

# Constraints:

# 1 <= s1.length <= 20
# s2.length == s1.length
# s1 and s2 contain only lowercase letters from the set {'a', 'b', 'c', 'd', 'e', 'f'}.
# s2 is an anagram of s1.
from collections import deque
class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        visited = set()
        queue = deque([(s1,0)])
        visited.add(s1)
        while queue:
            cur_str, k = queue.popleft()
            if cur_str == s2:
                return k
            cur_str = list(cur_str)
            i = 0
            while cur_str[i] == s2[i]:
                i+=1
            j = i+1
            while j<len(cur_str):
                if cur_str[j] == s2[i]:
                    cur_str[i],cur_str[j] = cur_str[j],cur_str[i]
                    next_str = ''.join(cur_str)
                    if next_str not in visited:
                        visited.add(next_str)
                        queue.append((next_str,k+1))
                    cur_str[i],cur_str[j] = cur_str[j],cur_str[i]
                j+=1
            
                    
        