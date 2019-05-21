# Given two strings s1, s2, find the lowest ASCII sum of deleted characters to make two strings equal.

# Example 1:
# Input: s1 = "sea", s2 = "eat"
# Output: 231
# Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
# Deleting "t" from "eat" adds 116 to the sum.
# At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
# Example 2:
# Input: s1 = "delete", s2 = "leet"
# Output: 403
# Explanation: Deleting "dee" from "delete" to turn the string into "let",
# adds 100[d]+101[e]+101[e] to the sum.  Deleting "e" from "leet" adds 101[e] to the sum.
# At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
# If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.
class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        l1 = len(s1)
        l2 = len(s2)
        matrix = [[0] * (l1 + 1) for _ in range(l2 + 1)]
        for i in range(l1 - 1, -1, -1):
            matrix[l2][i] = matrix[l2][i + 1] + ord(s1[i])
        for i in range(l2 - 1, -1, -1):
            matrix[i][-1] = matrix[i + 1][-1] + ord(s2[i])
        for i in range(l2 - 1, -1, -1):
            for j in range(l1 - 1, -1, -1):
                if s2[i] == s1[j]:
                    matrix[i][j] = min(matrix[i][j + 1] + ord(s1[j]), matrix[i + 1][j] + ord(s2[i]),matrix[i + 1][j + 1])
                else:
                    matrix[i][j] = min(matrix[i][j + 1] + ord(s1[j]), matrix[i + 1][j] + ord(s2[i]),
                                       matrix[i + 1][j + 1] + ord(s1[j]) + ord(s2[i]))
        return matrix[0][0]
