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
class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        self.s = s
        self.cache = {}
        return self.search(0, 0)

    def search(self, index, remain):
        if index == len(self.s):
            return remain == 0
        if (index, remain) in self.cache:
            return self.cache[(index, remain)]
        c = self.s[index]
        if c == "(":
            remain += 1
            ans = self.search(index + 1, remain)
            self.cache[(index, remain-1)] = ans
            return ans
        if c == ")":
            remain -= 1
            if remain<0:
                self.cache[(index, remain+1)] = False
                return False
            ans = self.search(index + 1, remain)
            self.cache[(index, remain+1)] = ans
            return ans
        if c == "*":
            remain += 1
            if self.search(index + 1, remain):
                self.cache[(index, remain-1)] = True
                return True
            remain -= 2
            if remain>=0 and self.search(index + 1, remain):
                self.cache[(index, remain+1)] = True
                return True
            remain += 1
            if self.search(index + 1, remain):
                self.cache[(index, remain)] = True
                return True
            self.cache[(index, remain)] = False
            return False