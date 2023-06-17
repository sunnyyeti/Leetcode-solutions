# <!-- An original string, consisting of lowercase English letters, can be encoded by the following steps:

# Arbitrarily split it into a sequence of some number of non-empty substrings.
# Arbitrarily choose some elements (possibly none) of the sequence, and replace each with its length (as a numeric string).
# Concatenate the sequence as the encoded string.
# For example, one way to encode an original string "abcdefghijklmnop" might be:

# Split it as a sequence: ["ab", "cdefghijklmn", "o", "p"].
# Choose the second and third elements to be replaced by their lengths, respectively. The sequence becomes ["ab", "12", "1", "p"].
# Concatenate the elements of the sequence to get the encoded string: "ab121p".
# Given two encoded strings s1 and s2, consisting of lowercase English letters and digits 1-9 (inclusive), return true if there exists an original string that could be encoded as both s1 and s2. Otherwise, return false.

# Note: The test cases are generated such that the number of consecutive digits in s1 and s2 does not exceed 3.

 

# Example 1:

# Input: s1 = "internationalization", s2 = "i18n"
# Output: true
# Explanation: It is possible that "internationalization" was the original string.
# - "internationalization" 
#   -> Split:       ["internationalization"]
#   -> Do not replace any element
#   -> Concatenate:  "internationalization", which is s1.
# - "internationalization"
#   -> Split:       ["i", "nternationalizatio", "n"]
#   -> Replace:     ["i", "18",                 "n"]
#   -> Concatenate:  "i18n", which is s2
# Example 2:

# Input: s1 = "l123e", s2 = "44"
# Output: true
# Explanation: It is possible that "leetcode" was the original string.
# - "leetcode" 
#   -> Split:      ["l", "e", "et", "cod", "e"]
#   -> Replace:    ["l", "1", "2",  "3",   "e"]
#   -> Concatenate: "l123e", which is s1.
# - "leetcode" 
#   -> Split:      ["leet", "code"]
#   -> Replace:    ["4",    "4"]
#   -> Concatenate: "44", which is s2.
# Example 3:

# Input: s1 = "a5b", s2 = "c5b"
# Output: false
# Explanation: It is impossible.
# - The original string encoded as s1 must start with the letter 'a'.
# - The original string encoded as s2 must start with the letter 'c'.
 

# Constraints:

# 1 <= s1.length, s2.length <= 40
# s1 and s2 consist of digits 1-9 (inclusive), and lowercase English letters only.
# The number of consecutive digits in s1 and s2 does not exceed 3. -->
from functools import cache
class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:
        def alpha_digit(ind1, ind2):
            v = 0
            for i in range(3):
                index = ind2 + i
                if (index < len(s2)) and s2[index].isdigit():
                    v = v * 10 + int(s2[index])
                    if v - 1 == 0:
                        if helper(ind1 + 1, None, index + 1, None):
                            return True
                    else:
                        if helper(ind1 + 1, None, index, v - 1):
                            return True
                else:
                    break
            return False

        def digit_alpha(ind1, ind2):
            v = 0
            for i in range(3):
                index = ind1 + i
                if (index < len(s1)) and s1[index].isdigit():
                    v = v * 10 + int(s1[index])
                    if v - 1 == 0:
                        if helper(index + 1, None, ind2 + 1, None):
                            return True
                    else:
                        if helper(index, v - 1, ind2 + 1, None):
                            return True
                else:
                    break
            return False

        def digit_value(ind1, ind2, value):
            v = 0
            for i in range(3):
                index = ind1 + i
                if index < len(s1) and s1[index].isdigit():
                    v = v * 10 + int(s1[index])
                    if v > value:
                        if helper(index, v - value, ind2 + 1, None):
                            return True
                    elif v == value:
                        if helper(index + 1, None, ind2 + 1, None):
                            return True
                    else:
                        if helper(index + 1, None, ind2, value - v):
                            return True
                else:
                    break
            return False

        def value_digit(ind1, ind2, value):
            v = 0
            for i in range(3):
                index = ind2 + i
                if index < len(s2) and s2[index].isdigit():
                    v = v * 10 + int(s2[index])
                    if v > value:
                        if helper(ind1 + 1, None, index, v - value):
                            return True
                    elif v == value:
                        if helper(ind1 + 1, None, index + 1, None):
                            return True
                    else:
                        if helper(ind1, value - v, index + 1, None):
                            return True
                else:
                    break
            return False

        def digit_digit(ind1, ind2):
            v1 = 0
            v2 = 0
            for i in range(3):
                index1 = ind1 + i
                if index1 < len(s1) and s1[index1].isdigit():
                    v1 = v1 * 10 + int(s1[index1])
                    v2 = 0
                    for j in range(3):
                        index2 = ind2 + j
                        if index2 < len(s2) and s2[index2].isdigit():
                            v2 = v2 * 10 + int(s2[index2])
                            if v1 > v2:
                                if helper(index1, v1 - v2, index2 + 1, None):
                                    return True
                            elif v1 == v2:
                                if helper(index1 + 1, None, index2 + 1, None):
                                    return True
                            else:
                                if helper(index1 + 1, None, index2, v2 - v1):
                                    return True
                        else:
                            break
                else:
                    break
            return False

        def alpha_value(ind1, ind2, value):
            if value > 1:
                return helper(ind1 + 1, None, ind2, value - 1)
            else:
                return helper(ind1 + 1, None, ind2 + 1, None)

        def value_alpha(ind1, ind2, value):
            if value > 1:
                return helper(ind1, value - 1, ind2 + 1, None)
            else:
                return helper(ind1 + 1, None, ind2 + 1, None)
        @cache
        def helper(ind1, v1, ind2, v2):
            if ind1 == len(s1) and ind2 == len(s2):
                return True
            elif ind1 == len(s1) or ind2 == len(s2):
                return False
            if v1 is None and v2 is None:
                c1 = s1[ind1]
                c2 = s2[ind2]
                if c1.isalpha() and c2.isalpha():
                    if c1 != c2: return False
                    return helper(ind1 + 1, None, ind2 + 1, None)
                elif c1.isalpha():
                    return alpha_digit(ind1, ind2)
                elif c2.isalpha():
                    return digit_alpha(ind1, ind2)
                else:
                    return digit_digit(ind1, ind2)
            elif v1 is not None:
                c2 = s2[ind2]
                if c2.isalpha():
                    return value_alpha(ind1, ind2, v1)
                else:
                    return value_digit(ind1, ind2, v1)
            elif v2 is not None:
                c1 = s1[ind1]
                if c1.isalpha():
                    return alpha_value(ind1, ind2, v2)
                else:
                    return digit_value(ind1, ind2, v2)

        return helper(0, None, 0, None)
    
    