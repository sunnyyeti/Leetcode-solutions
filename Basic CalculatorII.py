# Given a string s which represents an expression, evaluate this expression and return its value. 

# The integer division should truncate toward zero.

 

# Example 1:

# Input: s = "3+2*2"
# Output: 7
# Example 2:

# Input: s = " 3/2 "
# Output: 1
# Example 3:

# Input: s = " 3+5 / 2 "
# Output: 5
 

# Constraints:

# 1 <= s.length <= 3 * 105
# s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
# s represents a valid expression.
# All the integers in the expression are non-negative integers in the range [0, 231 - 1].
# The answer is guaranteed to fit in a 32-bit integer.
class Solution:
    def calculate(self, s: str) -> int:
        def cal(op1,op2,sym):
            if sym=="+":
                return op1+op2
            if sym=="-":
                return op1-op2
            if sym=="*":
                return op1*op2
            if sym=="/":
                return op1//op2
        operators = {'+', '-', '*', '/'}
        oprands_stack = []
        operators_stack = []
        d = 0
        for i,c in enumerate(s):
            if c == " ":
                continue
            if c in ['+','-']:
                oprands_stack.append(d)
                d=0
                while operators_stack:
                    cur_op = operators_stack.pop()
                    opr2 = oprands_stack.pop()
                    opr1 = oprands_stack.pop()
                    oprands_stack.append(cal(opr1,opr2,cur_op))
                operators_stack.append(c)
            elif c in ["*","/"]:
                oprands_stack.append(d)
                d=0
                while operators_stack and operators_stack[-1] in ["*","/"]:
                    cur_op = operators_stack.pop()
                    opr2 = oprands_stack.pop()
                    opr1 = oprands_stack.pop()
                    oprands_stack.append(cal(opr1,opr2,cur_op))
                operators_stack.append(c)
            else:
                d = d*10 + int(c)

        oprands_stack.append(d)
        while operators_stack:
            cur_op = operators_stack.pop()
            opr2 = oprands_stack.pop()
            opr1 = oprands_stack.pop()
            oprands_stack.append(cal(opr1,opr2,cur_op))
        return oprands_stack.pop()
        