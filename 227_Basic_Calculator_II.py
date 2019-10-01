# Implement a basic calculator to evaluate a simple expression string.

# The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

# Example 1:

# Input: "3+2*2"
# Output: 7
# Example 2:

# Input: " 3/2 "
# Output: 1
# Example 3:

# Input: " 3+5 / 2 "
# Output: 5
# Note:

# You may assume that the given expression is always valid.
# Do not use the eval built-in library function.
# Accepted
# 128,775
# Submissions
# 372,646
class Solution:
    def calculate(self, s: str) -> int:
        operands = []
        operators = []
        s = s.replace(" ", "")
        ops = {'+', '-', '*', '/'}
        for i, c in enumerate(s):
            if c not in ops:
                if i == 0 or s[i - 1] in ops:
                    operands.append(int(c))
                else:
                    operands[-1] = operands[-1] * 10 + int(c)
            else:
                if not operators or self.isgreater(c, operators[-1]):
                    operators.append(c)
                else:
                    while operators and not self.isgreater(c,operators[-1]):
                        op = operators.pop()
                        ond2 = operands.pop()
                        ond1 = operands.pop()
                        operands.append(self.cal(op, ond1, ond2))
                    operators.append(c)
        while operators:
            op = operators.pop()
            ond2 = operands.pop()
            ond1 = operands.pop()
            operands.append(self.cal(op, ond1, ond2))
        return operands.pop()

    def isgreater(self, c1, c2):
        return c1 in {'*', '/'} and c2 in {'+', '-'}

    def cal(self, op, o1, o2):
        if op == '+':
            return o1 + o2
        if op == '-':
            return o1 - o2
        if op == '*':
            return o1 * o2
        if op == "/":
            return int(o1 / o2)