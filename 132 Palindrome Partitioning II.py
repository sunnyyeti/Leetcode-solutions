# Given a string s, partition s such that every substring of the partition is a palindrome.

# Return the minimum cuts needed for a palindrome partitioning of s.

 

# Example 1:

# Input: s = "aab"
# Output: 1
# Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
# Example 2:

# Input: s = "a"
# Output: 0
# Example 3:

# Input: s = "ab"
# Output: 1
 

# Constraints:

# 1 <= s.length <= 2000
# s consists of lower-case English letters only.
from functools import cache
class Solution:
    def minCut(self, s: str) -> int:
        def expand(left:int,right:int,all_palindromes:set):
            while 0<=left and right<len(s) and s[left]==s[right]:
                all_palindromes.add((left,right))
                left-=1
                right+=1
        all_palindromes = set()
        for i in range(len(s)):
            expand(i,i,all_palindromes)
            if i+1 < len(s):
                expand(i,i+1,all_palindromes)
        @cache
        def min_splits(i,j):
            if (i,j) in all_palindromes:
                return 0
            cur_min_splits = float("inf")
            for k in range(j,i,-1):
                if (k,j) in all_palindromes:
                    cur_min_splits = min(min_splits(i,k-1)+1,cur_min_splits)
            return cur_min_splits
        return min_splits(0,len(s)-1)