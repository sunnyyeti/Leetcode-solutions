# Given an array of strings, group anagrams together.

# Example:

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note:

# All inputs will be in lowercase.
# The order of your output does not matter.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def key(word):
            return "".join(sorted(word))
        ans = {}
        for word in strs:
            ans.setdefault(key(word),[]).append(word)
        return list(ans.values())