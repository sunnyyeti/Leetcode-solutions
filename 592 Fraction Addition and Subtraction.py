# Given a string representing an expression of fraction addition and subtraction, you need to return the calculation result in string format. The final result should be irreducible fraction. If your final result is an integer, say 2, you need to change it to the format of fraction that has denominator 1. So in this case, 2 should be converted to 2/1.

# Example 1:
# Input:"-1/2+1/2"
# Output: "0/1"
# Example 2:
# Input:"-1/2+1/2+1/3"
# Output: "1/3"
# Example 3:
# Input:"1/3-1/2"
# Output: "-1/6"
# Example 4:
# Input:"5/3+1/3"
# Output: "2/1"
# Note:
# The input string only contains '0' to '9', '/', '+' and '-'. So does the output.
# Each fraction (input and output) has format ±numerator/denominator. If the first input fraction or the output is positive, then '+' will be omitted.
# The input only contains valid irreducible fractions, where the numerator and denominator of each fraction will always be in the range [1,10]. If the denominator is 1, it means this fraction is actually an integer in a fraction format defined above.
# The number of given fractions will be in the range [1,10].
# The numerator and denominator of the final result are guaranteed to be valid and in the range of 32-bit int.

def gcd(a,b):
    if a<b:
        a,b = b,a
    while b!=0:
        a,b = b,a%b
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

class frac:
    def __init__(self,n,d):
        self.n = n
        self.d = d
    
    def __add__(self,o):
        denominator = lcm(self.d,o.d)
        numerator = self.n*denominator//self.d+o.n*denominator//o.d
        return frac(numerator,denominator)
    
    def __sub__(self,o):
        return self + frac(-o.n,o.d)
    
    def reduce(self):
        g = gcd(abs(self.n),self.d)
        return frac(self.n//g,self.d//g)
    
    def __str__(self):
        return f"{self.n}/{self.d}"

class Solution:
    def fractionAddition(self, expression: str) -> str:
        if expression[0] == '-':
            expression = '0/1'+expression
        operators = []
        operands = []
        for i,c in enumerate(expression):
            if c.isdigit():
                if i-1>=0 and expression[i-1].isdigit():
                    operands[-1] = operands[-1]*10+int(c)
                else:
                    operands.append(int(c))
            elif c=='/':
                operators.append(c)
            else:
                while operators:
                    cop = operators.pop()
                    s,f = operands.pop(),operands.pop()
                    if cop=='/':
                        operands.append(frac(f,s))
                    elif cop=='+':
                        operands.append(f+s)
                    else:
                        operands.append(f-s)
                operators.append(c)
        
        while operators:
            cop = operators.pop()
            s,f = operands.pop(),operands.pop()
            if cop=='/':
                operands.append(frac(f,s))
            elif cop=='+':
                operands.append(f+s)
            else:
                operands.append(f-s)
        return str(operands[0].reduce())
                