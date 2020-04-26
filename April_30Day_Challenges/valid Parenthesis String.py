# Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
# An empty string is also valid.
# Example 1:
# Input: "()"
# Output: True
# Example 2:
# Input: "(*)"
# Output: True
# Example 3:
# Input: "(*))"
# Output: True
# Note:
# The string size will be in the range [1, 100].

class Solution:
    def checkValidString(self, s: str) -> bool:
        def isvalid(cur_re,ind):
            if cur_re < 0:
                return False
            if ind==len(s):
                return cur_re==0
            if (cur_re,ind) in cache:
                return cache[(cur_re,ind)]
            cur_char = s[ind]
            if cur_char =="(":
                tmp = isvalid(cur_re+1,ind+1)
                cache[(cur_re,ind)] = tmp
                return tmp
            if cur_char==")":
                tmp =  isvalid(cur_re-1,ind+1)
                cache[(cur_re,ind)] = tmp
                return tmp
            if isvalid(cur_re,ind+1) or isvalid(cur_re+1,ind+1) or isvalid(cur_re-1,ind+1):
                cache[(cur_re,ind)] = True
                return True
            cache[(cur_re,ind)] = False
            return False
        cache = {}
        return isvalid(0,0)