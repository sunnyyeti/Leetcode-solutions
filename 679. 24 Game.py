# You have 4 cards each containing a number from 1 to 9. You need to judge whether they could operated through *, /, +, -, (, ) to get the value of 24.

# Example 1:
# Input: [4, 1, 8, 7]
# Output: True
# Explanation: (8-4) * (7-1) = 24
# Example 2:
# Input: [1, 2, 1, 2]
# Output: False
# Note:
# The division operator / represents real division, not integer division. For example, 4 / (1 - 2/3) = 12.
# Every operation done is between two numbers. In particular, we cannot use - as a unary operator. For example, with [1, 1, 1, 1] as input, the expression -1 - 1 - 1 - 1 is not allowed.
# You cannot concatenate numbers together. For example, if the input is [1, 2, 1, 2], we cannot write this as 12 + 12.
# Accepted
# 30.7K
# Submissions
# 68.3K
from fractions import Fraction



class Solution:
    def judgePoint24(self, nums) -> bool:
        nums = [Fraction(n) for n in nums]
        #print(self.par(nums, Fraction(24)))
        #print(self.seq(nums, Fraction(24)))
        return self.par(nums, Fraction(24)) or self.seq(nums, Fraction(24))

    def cal(self, a, b, op):
        if op == "*":
            return a * b
        if op == "+":
            return a + b
        if op == "-":
            return a - b
        if op == "/":
            return a / b
        if op == "-r":
            return b - a
        if op == "/r":
            return b / a

    def par(self, nums, target):
        a = nums[0]
        for j in range(1, len(nums)):
            b = nums[j]
            remain = nums[1:j] + nums[j + 1:]
            for op in ["*", "+", "-", "/", "-r", "/r"]:
                cur = self.cal(a, b, op)
                if any((
                        self.seq(remain, target - cur),
                        self.seq(remain, target / cur) if cur != 0 else False,
                        self.seq(remain, cur - target),
                        self.seq(remain, cur + target),
                        self.seq(remain, cur / target) if cur!=0 else False ,
                        self.seq(remain, cur * target) if cur!=0 else False

                )
                ):
                    return True
        return False

    def seq(self, nums, target):
        if len(nums) == 2:
            a, b = nums
            return any((
                a + b == target,
                a * b == target,
                a - b == target,
                b - a == target,
                a / b == target,
                b / a == target
            )
            )
        for i in range(len(nums)):
            cur = nums[i]
            remain = nums[:i] + nums[i + 1:]
            if any((self.seq(remain, target - cur),
                    self.seq(remain, target / cur) ,
                    self.seq(remain, cur - target),
                    self.seq(remain, cur + target),
                    self.seq(remain, cur / target) if target!=0 else False,
                    self.seq(remain, cur * target)
                    )):
                return True
        return False


