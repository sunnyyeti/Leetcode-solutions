# Given two strings S and T, each of which represents a non-negative rational number, return True if and only if they represent the same number. The strings may use parentheses to denote the repeating part of the rational number.

# In general a rational number can be represented using up to three parts: an integer part, a non-repeating part, and a repeating part. The number will be represented in one of the following three ways:

# <IntegerPart> (e.g. 0, 12, 123)
# <IntegerPart><.><NonRepeatingPart>  (e.g. 0.5, 1., 2.12, 2.0001)
# <IntegerPart><.><NonRepeatingPart><(><RepeatingPart><)> (e.g. 0.1(6), 0.9(9), 0.00(1212))
# The repeating portion of a decimal expansion is conventionally denoted within a pair of round brackets.  For example:

# 1 / 6 = 0.16666666... = 0.1(6) = 0.1666(6) = 0.166(66)

# Both 0.1(6) or 0.1666(6) or 0.166(66) are correct representations of 1 / 6.

 

# Example 1:

# Input: S = "0.(52)", T = "0.5(25)"
# Output: true
# Explanation:
# Because "0.(52)" represents 0.52525252..., and "0.5(25)" represents 0.52525252525..... , the strings represent the same number.
# Example 2:

# Input: S = "0.1666(6)", T = "0.166(66)"
# Output: true
# Example 3:

# Input: S = "0.9(9)", T = "1."
# Output: true
# Explanation: 
# "0.9(9)" represents 0.999999999... repeated forever, which equals 1.  [See this link for an explanation.]
# "1." represents the number 1, which is formed correctly: (IntegerPart) = "1" and (NonRepeatingPart) = "".
 

# Note:

# Each part consists only of digits.
# The <IntegerPart> will not begin with 2 or more zeros.  (There is no other restriction on the digits of each part.)
# 1 <= <IntegerPart>.length <= 4
# 0 <= <NonRepeatingPart>.length <= 4
# 1 <= <RepeatingPart>.length <= 4
import re
class Rational:

    def __init__(self,numerator,denominator):
        self.denominator = denominator
        self.numerator = numerator
        if numerator==0:
            self.denominator=1

    def __add__(self, other):
        #assert isinstance(other,int)
        new_denominator = self.denominator
        new_numerator = other*self.denominator+self.numerator
        return Rational(new_numerator,new_denominator)

    def __truediv__(self, other):
        #assert isinstance(other,int)
        return Rational(self.numerator,self.denominator*other)

    def reduce(self):
        def gcd(a,b):
            if a<b:
                a,b = b,a
            mod = a%b
            while mod!=0:
                a,b = b,mod
                mod = a%b
            return b
        if self.numerator==0:
            self.denominator=1
        else:
            gcd_ = gcd(self.numerator,self.denominator)
            self.numerator//=gcd_
            self.denominator//=gcd_

    def __eq__(self, other):
        return self.denominator==other.denominator and self.numerator==other.numerator

class Solution:
    def isRationalEqual(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        S_splits = S.split(".")
        T_splits = T.split(".")
        s_integer = self.integer_part(S_splits[0])
        t_integer = self.integer_part(T_splits[0])
        s_fraction = S_splits[-1] if len(S_splits) > 1 else ""
        t_fraction = T_splits[-1] if len(T_splits) > 1 else ""
        s_fraction = self.fraction_part(s_fraction)
        t_fraction = self.fraction_part(t_fraction)
        s_value = s_fraction+s_integer
        t_value = t_fraction+t_integer
        s_value.reduce()
        t_value.reduce()
        return s_value==t_value

    def integer_part(self, s):
        if s == "":
            return 0
        return int(s)

    def fraction_part(self, s):
        if s == "":
            return Rational(0,0)
        repet = re.search("\(\d+\)", s)
        if repet is None:
            return Rational(int(s),pow(10, len(s)))
        non_repet_end = s.index("(")
        non_repet = int(s[:non_repet_end]) if non_repet_end > 0 else 0
        multipier = pow(10, non_repet_end)
        repet = repet.group()[1:-1]
        repet = Rational(int(repet),(pow(10, len(repet)) - 1))
        return (repet+non_repet) / multipier

if __name__ == "__main__":
    a = "0.1666(6)"
    b = "0.166(66)"
    print(Solution().isRationalEqual(a,b))