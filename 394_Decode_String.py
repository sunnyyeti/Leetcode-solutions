# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

# Examples:

# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c!=']':
                stack.append(c)
            else:
                tmp = ''
                while stack[-1]!='[':
                    tmp = stack.pop()+tmp
                stack.pop()
                k = 0
                m = 1
                while stack and stack[-1].isdigit():
                    k += int(stack.pop())*m
                    m*=10
                stack.append(tmp*k)
        return ''.join(stack)

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c!="]":
                stack.append(c)
            else:
                substring = ""
                while stack[-1] != '[':
                    substring += stack.pop()
                stack.pop()
                repeat = ""
                while stack and stack[-1].isdigit():
                    repeat += stack.pop()
                stack.extend(substring[::-1]*int(repeat[::-1]))
        return "".join(stack)
                