# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given an integer, convert it to a roman numeral.

 

# Example 1:

# Input: num = 3
# Output: "III"
# Example 2:

# Input: num = 4
# Output: "IV"
# Example 3:

# Input: num = 9
# Output: "IX"
# Example 4:

# Input: num = 58
# Output: "LVIII"
# Explanation: L = 50, V = 5, III = 3.
# Example 5:

# Input: num = 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
class Solution:
    def intToRoman(self, num: int) -> str:
        def convert(num):
            if num==0:
                return ''
            elif 1<=num<4:
                return 'I'*num
            elif num==4:
                return 'IV'
            elif num==5:
                return 'V'
            elif 5<num<9:
                return 'V'+'I'*(num-5)
            elif num==9:
                return 'IX'
            elif 10<=num<40:
                return 'X'*(num//10)
            elif num==40:
                return 'XL'
            elif num==50:
                return 'L'
            elif 50<num<90:
                return 'L'+'X'*((num-50)//10)
            elif num==90:
                return 'XC'
            elif 100 <= num < 400:
                return 'C'*(num//100)
            elif num==400:
                return 'CD'
            elif num==500:
                return 'D'
            elif 500<num<900:
                return 'D'+'C'*((num-500)//100)
            elif num == 900:
                return 'CM'
            else:
                return 'M'*(num//1000)
        ans = []
        i = 1
        while num:
            d = num%10
            d *= i
            num //= 10
            i*=10
            ans.append(convert(d))
        return ''.join(reversed(ans))
        