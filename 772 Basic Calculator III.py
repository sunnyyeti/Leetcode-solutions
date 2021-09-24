# Implement a basic calculator to evaluate a simple expression string.

# The expression string contains only non-negative integers, '+', '-', '*', '/' operators, and open '(' and closing parentheses ')'. The integer division should truncate toward zero.

# You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

# Example 1:

# Input: s = "1+1"
# Output: 2
# Example 2:

# Input: s = "6-4/2"
# Output: 4
# Example 3:

# Input: s = "2*(5+5*2)/3+(6/2+8)"
# Output: 21
# Example 4:

# Input: s = "(2+6*3+5-(3*14/7+2)*5)+3"
# Output: -12
# Example 5:

# Input: s = "0"
# Output: 0
 

# Constraints:

# 1 <= s <= 104
# s consists of digits, '+', '-', '*', '/', '(', and ')'.
# s is a valid expression.
class Solution:
    def calculate(self, s: str) -> int:
        calc_funcs = {
            "+": lambda x,y:x+y,
            '-':lambda x,y:x-y,
            '*':lambda x,y:x*y,
            '/':lambda x,y:abs(x)//abs(y) * (1 if x*y>=0 else -1) 
        }
        operands = []
        operators = []
        for i,c in enumerate(s):
            if c.isdigit():
                if i-1>=0 and s[i-1].isdigit():
                    last_num = operands.pop()
                    new_number = last_num*10+int(c)
                    operands.append(new_number)
                else:
                    operands.append(int(c))
            elif c=='(':
                operators.append(c)
            elif c==')':
                while operators[-1]!='(':
                    op = operators.pop()
                    oprand1 = operands.pop()
                    oprand2 = operands.pop()
                    calc_res = calc_funcs[op](oprand2,oprand1)
                    operands.append(calc_res)
                operators.pop()
            else:
                while operators and (operators[-1] in ['*','/'] or c in ['+','-']) and operators[-1]!='(':
                    op = operators.pop()
                    oprand1 = operands.pop()
                    oprand2 = operands.pop()
                    calc_res = calc_funcs[op](oprand2,oprand1)
                    operands.append(calc_res)
                operators.append(c)
        #print(operators)
        #print(operands)
        while operators:
                op = operators.pop()
                oprand1 = operands.pop()
                oprand2 = operands.pop()
                calc_res = calc_funcs[op](oprand2,oprand1)
                operands.append(calc_res)   
        return operands.pop()