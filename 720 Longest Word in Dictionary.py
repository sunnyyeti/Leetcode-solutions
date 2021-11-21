# Given an array of strings words representing an English Dictionary, return the longest word in words that can be built one character at a time by other words in words.

# If there is more than one possible answer, return the longest word with the smallest lexicographical order. If there is no answer, return the empty string.

 

# Example 1:

# Input: words = ["w","wo","wor","worl","world"]
# Output: "world"
# Explanation: The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
# Example 2:

# Input: words = ["a","banana","app","appl","ap","apply","apple"]
# Output: "apple"
# Explanation: Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
 

# Constraints:

# 1 <= words.length <= 1000
# 1 <= words[i].length <= 30
# words[i] consists of lowercase English letters.
class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = {}
        words.sort(key=len)
        ans = None
        for word in words:
            node = trie
            can_built = True
            for i,char in enumerate(word):
                node = node.setdefault(char,{})
                if i<len(word)-1 and '#' not in node:
                    can_built = False
            node['#'] = True
            if can_built:
                if ans is None or len(word) > len(ans):
                    ans = word
                elif len(word)==len(ans) and word<ans:
                    ans = word
        return '' if ans is None else ans
                    
                                