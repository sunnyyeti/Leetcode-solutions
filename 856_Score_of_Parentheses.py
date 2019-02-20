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
 class Solution:
    def scoreOfParentheses(self, S: 'str') -> 'int':
        stack = []
        for c in S:
            if c=="(":
                stack.append(c)
            else:
                if stack[-1]=="(":
                    stack[-1] = 1
                    if len(stack) >1 and stack[-2] != "(":
                        stack[-2] +=stack[-1]
                        stack.pop()
                else:
                    new_v = 2*stack.pop()
                    stack[-1] = new_v
                    if len(stack) >1 and stack[-2] !="(":
                        stack[-2] +=stack[-1]
                        stack.pop()
        return stack.pop()