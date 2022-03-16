# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

# A palindrome string is a string that reads the same backward as forward.


# Example 1:

# Input: s = "aab"
# Output: [["a", "a", "b"], ["aa", "b"]]
# Example 2:

# Input: s = "a"
# Output: [["a"]]


# Constraints:

# 1 <= s.length <= 16
# s contains only lowercase English letters.

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        all_palindromes = set()
        for i in range(len(s)):
            for j in range(i+1):
                if i == j or (j+1 == i and s[j] == s[i]):
                    all_palindromes.add((j, i))
                elif s[j] == s[i] and (j+1, i-1) in all_palindromes:
                    all_palindromes.add((j, i))
        tmp = []
        ans = []

        def split_from(start):
            if start == len(s):
                ans.append(tmp[:])
            for end in range(start, len(s)):
                if (start, end) in all_palindromes:
                    tmp.append(s[start:end+1])
                    split_from(end+1)
                    tmp.pop()
        split_from(0)
        return ans
