# Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

# Note:
# n is positive and will fit within the range of a 32-bit signed integer (n < 231).

# Example 1:

# Input:
# 3

# Output:
# 3
# Example 2:

# Input:
# 11

# Output:
# 0

# Explanation:
# The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
class Solution:
    def findNthDigit(self, n: int) -> int:
        t = 0
        i = 1
        while t<n:
            t+=self.total(i)
            i+=1
        i-=1
        back_cnt = (t-n)//i
        back_remain = (t-n)%i            
        back_start = 10**(i)-1-back_cnt
        return (back_start)%(10**(back_remain+1))//(10**(back_remain))
    def total(self,i):
        return (10**(i)-10**(i-1))*i