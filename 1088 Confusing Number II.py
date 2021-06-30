# We can rotate digits by 180 degrees to form new digits. When 0, 1, 6, 8, 9 are rotated 180 degrees, they become 0, 1, 9, 8, 6 respectively. When 2, 3, 4, 5 and 7 are rotated 180 degrees, they become invalid.

# A confusing number is a number that when rotated 180 degrees becomes a different number with each digit valid.(Note that the rotated number can be greater than the original number.)

# Given a positive integer n, return the number of confusing numbers between 1 and n inclusive.

 

# Example 1:

# Input: n = 20
# Output: 6
# Explanation: 
# The confusing numbers are [6,9,10,16,18,19].
# 6 converts to 9.
# 9 converts to 6.
# 10 converts to 01 which is just 1.
# 16 converts to 91.
# 18 converts to 81.
# 19 converts to 61.
# Example 2:

# Input: n = 100
# Output: 19
# Explanation: 
# The confusing numbers are [6,9,10,16,18,19,60,61,66,68,80,81,86,89,90,91,98,99,100].
 
from collections import deque


class Solution:
    def confusingNumberII(self, n: int) -> int:
        mappings = {
            0: 0,
            1: 1,
            6: 9,
            8: 8,
            9: 6
        }
        strn = list(str(n))
        intn = [int(s) for s in strn]
        numcands = [0, 1, 6, 8, 9]
        cand = []
        reverse = []
        ans = 0

        def help(ind, prev, prev_equal):
            nonlocal ans
            if ind == len(intn):
                if prev != 0:
                    first_non_zero = next(
                        i for i, c in enumerate(cand) if c != 0)
                    reverse_num = 0
                    for i in range(len(reverse)-1, first_non_zero-1, -1):
                        reverse_num = reverse_num*10+reverse[i]
                    if reverse_num != prev:
                        ans += 1
                return
            up = intn[ind]
            for nc in numcands:
                if prev_equal:
                    if nc <= up:
                        cand.append(nc)
                        reverse.append(mappings[nc])
                        prev = prev*10+nc
                        help(ind+1, prev, nc == up)
                        prev = (prev-nc)//10
                        cand.pop()
                        reverse.pop()
                else:
                    cand.append(nc)
                    reverse.append(mappings[nc])
                    prev = prev*10+nc
                    help(ind+1, prev, False)
                    prev = (prev-nc)//10
                    cand.pop()
                    reverse.pop()
        help(0, 0, True)
        return ans
