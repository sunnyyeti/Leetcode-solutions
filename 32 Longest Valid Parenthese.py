# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

 

# Example 1:

# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".
# Example 2:

# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".
# Example 3:

# Input: s = ""
# Output: 0
 

# Constraints:

# 0 <= s.length <= 3 * 104
# s[i] is '(', or ')'.
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        pairs = [-1]*len(s)
        for i,c in enumerate(s):
            if c==')' and i>=1:
                prev_c = s[i-1]
                if prev_c=='(':
                    j = i-2
                    if j>=0 and pairs[j]!=-1:
                        pairs[i] = pairs[j]
                    else:
                        pairs[i] = i-1
                else:
                    if pairs[i-1]!=-1:
                        prev_pair_start = pairs[i-1]
                        if prev_pair_start-1>=0 and s[prev_pair_start-1]=='(':
                            pairs[i] = prev_pair_start-1
                        prev = pairs[i]-1
                        if prev>=0 and pairs[prev]!=-1:
                            pairs[i]=pairs[prev]
        #print(pairs)                
        return max((i-prev+1 for i,prev in enumerate(pairs) if prev!=-1), default=0)
                