# You are given a string s representing a list of words. Each letter in the word has one or more options.

# If there is one option, the letter is represented as is.
# If there is more than one option, then curly braces delimit the options. For example, "{a,b,c}" represents options ["a", "b", "c"].
# For example, if s = "a{b,c}", the first character is always 'a', but the second character can be 'b' or 'c'. The original list is ["ab", "ac"].

# Return all words that can be formed in this manner, sorted in lexicographical order.

 

# Example 1:

# Input: s = "{a,b}c{d,e}f"
# Output: ["acdf","acef","bcdf","bcef"]
# Example 2:

# Input: s = "abcd"
# Output: ["abcd"]
 

# Constraints:

# 1 <= s.length <= 50
# s consists of curly brackets '{}', commas ',', and lowercase English letters.
# s is guaranteed to be a valid input.
# There are no nested curly brackets.
# All characters inside a pair of consecutive opening and ending curly brackets are different.
class Solution:
    def expand(self, s: str) -> List[str]:
        candidates = []
        stack = []
        for c in s:
            if not stack:
                if c == '{':
                    stack.append(c)
                else:
                    candidates.append([c])
            else:
                if c != '}':
                    stack.append(c)
                else:
                    cache = []
                    while stack[-1] != '{':
                        top = stack.pop()
                        if top.isalpha():
                            cache.append(top)
                    stack.pop()
                    candidates.append(cache)
        for group in candidates:
            group.sort()
        ans = []
        tmp = []
        #print(candidates)

        def bt(ind):
            if ind == len(candidates):
                ans.append(''.join(tmp))
                return
            group = candidates[ind]
            for char in group:
                tmp.append(char)
                bt(ind+1)
                tmp.pop()
        bt(0)
        return ans
