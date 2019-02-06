# Given two strings representing two complex numbers.

# You need to return a string representing their multiplication. Note i2 = -1 according to the definition.

# Example 1:
# Input: "1+1i", "1+1i"
# Output: "0+2i"
# Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
# Example 2:
# Input: "1+-1i", "1+-1i"
# Output: "0+-2i"
# Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
class Solution:
    def complexNumberMultiply(self, a: 'str', b: 'str') -> 'str':
        r1,c1 = a.split("+")
        r1 = int(r1)
        c1 = int(c1[:-1])
        r2,c2 = b.split("+")
        r2 = int(r2)
        c2 = int(c2[:-1])
        r = r1*r2-c1*c2
        c = r1*c2+r2*c1
        return "{}+{}i".format(r,c)