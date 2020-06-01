# Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

# Note:
# The length of num is less than 10002 and will be ≥ k.
# The given num does not contain any leading zero.
# Example 1:

# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
# Example 2:

# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
# Example 3:

# Input: num = "10", k = 2
# Output: "0"
# Explanation: Remove all the digits from the number and it is left with nothing which is 0.
import bisect
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        def find(pos,low,up):
            left = bisect.bisect_left(pos,low)
            right = bisect.bisect_right(pos,up)
            if left<right:
                return True,pos[left]
            return False,-1
        remain = len(num)-k
        char_pos = {}
        ans = []
        for i,char in enumerate(num):
            char_pos.setdefault(char,[]).append(i)
        for char in '0123456789':
            char_pos.setdefault(char,[]).sort()
        #print(char_pos)
        #print(remain)
        low = 0
        for i in range(remain):
            a_r = remain-i
            up = len(num)-a_r
            ##print(i,a_r,low,up)
            #print(ans)
            if low==up:
                ans.extend(num[low:])
                break
            for char in '0123456789':
                pos = char_pos[char]
                ok,left = find(pos,low,up)
                if ok:
                    ans.append(char)
                    low = left+1
                    break
        ans = "".join(ans).lstrip('0')
        return '0' if not ans else ans