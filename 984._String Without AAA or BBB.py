# Given two integers A and B, return any string S such that:

# S has length A + B and contains exactly A 'a' letters, and exactly B 'b' letters;
# The substring 'aaa' does not occur in S;
# The substring 'bbb' does not occur in S.
 

# Example 1:

# Input: A = 1, B = 2
# Output: "abb"
# Explanation: "abb", "bab" and "bba" are all correct answers.
# Example 2:

# Input: A = 4, B = 1
# Output: "aabaa"
 

# Note:

# 0 <= A <= 100
# 0 <= B <= 100
# It is guaranteed such an S exists for the given A and B.
class Solution:
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        if A>=B:
            longer = A
            longer_s = "a"
            shorter = B
            shorter_s = "b"
        else:
            longer = B
            longer_s = "b"
            shorter = A
            shorter_s = "a"
        if longer==shorter:
            return "".join(longer_s+shorter_s for _ in range(longer))
        if longer//2>=shorter:
            return (longer_s*2+shorter_s)*shorter+longer_s*(longer-shorter*2)
        remain_shorter = shorter-longer//2
        res = ""
        for _ in range(remain_shorter):
            res+=(longer_s+shorter_s)*2
        for _ in range(longer//2-remain_shorter):
            res+=(longer_s*2+shorter_s)
        res+=longer_s*(longer-2*(longer//2))
        return res
        