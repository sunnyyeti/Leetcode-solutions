# Given a balanced parentheses string S, compute the score of the string based on the following rule:

# () has score 1
# AB has score A + B, where A and B are balanced parentheses strings.
# (A) has score 2 * A, where A is a balanced parentheses string.
 

# Example 1:

# Input: "()"
# Output: 1
# Example 2:

# Input: "(())"
# Output: 2
# Example 3:

# Input: "()()"
# Output: 2
# Example 4:

# Input: "(()(()))"
# Output: 6
 

# Note:

# S is a balanced parentheses string, containing only ( and ).
# 2 <= S.length <= 50
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = []
        vals = []
        for i,c in enumerate(S):
            if c=='(':
                stack.append((i,c))
            else:
                ind,_ = stack.pop()
                if i-ind==1:
                    vals.append((ind,1))
                else:
                    tmps = 0
                    while vals and vals[-1][0]>ind:
                        tmps += vals.pop()[1]
                    vals.append((ind,tmps*2))
        return sum(v[1]  for v in vals)