# Given an array of strings strs, return the length of the longest uncommon subsequence between them. If the longest uncommon subsequence does not exist, return -1.

# An uncommon subsequence between an array of strings is a string that is a subsequence of one string but not the others.

# A subsequence of a string s is a string that can be obtained after deleting any number of characters from s.

# For example, "abc" is a subsequence of "aebdc" because you can delete the underlined characters in "aebdc" to get "abc". Other subsequences of "aebdc" include "aebdc", "aeb", and "" (empty string).
 

# Example 1:

# Input: strs = ["aba","cdc","eae"]
# Output: 3
# Example 2:

# Input: strs = ["aaa","aaa","aa"]
# Output: -1
 

# Constraints:

# 1 <= strs.length <= 50
# 1 <= strs[i].length <= 10
# strs[i] consists of lowercase English letters.
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        graph = {}
        for i in range(len(strs)):
            for j in range(i+1, len(strs)):
                str1 = strs[i]
                str2 = strs[j]
                if len(str1) < len(str2):
                    if self.is_subsequence(str1, str2):
                        graph.setdefault(i, []).append(j)
                elif len(str1) > len(str2):
                    if self.is_subsequence(str2, str1):
                        graph.setdefault(j, []).append(i)
                else:
                    if str1 == str2:
                        graph.setdefault(i, []).append(j)
                        graph.setdefault(j, []).append(i)
        #print(graph)
        candidates = [i for i in range(len(strs)) if i not in graph]
        #print(candidates)
        return max(len(strs[c]) for c in candidates) if candidates else -1

    def is_subsequence(self, str1, str2):
        target_ind = 0
        target_char = str1[target_ind]
        for i, cur_char in enumerate(str2):
            if cur_char == target_char:
                target_ind += 1
                if target_ind == len(str1):
                    return True
                target_char = str1[target_ind]
        return False
