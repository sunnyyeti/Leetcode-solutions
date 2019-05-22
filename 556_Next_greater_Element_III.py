# Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive 32-bit integer exists, you need to return -1.

# Example 1:

# Input: 12
# Output: 21
 

# Example 2:

# Input: 21
# Output: -1
# class Solution:
#     def nextGreaterElement(self, n: int) -> int:
#         self.digits = list(map(int,str(n)))
#         self.cnt ={}
#         for d in self.digits:
#             self.cnt[d] = self.cnt.setdefault(d,0)+1
#         #self.sorted_digits = sorted(self.digits)
#         #self.chosen_inds = set()
#         #self.ans = []
#         ans =  self.helper(0)
#         if ans:
#             ans = int("".join(map(str,ans)))
#             return ans if ans<2147483647 else -1
#         return -1
#
#     def upbound(self,d):
#         begin = 0
#         end = len(self.digits)-1
#         while begin<=end:
#             mid = (begin+end)//2
#             if self.digits[mid]<=d:
#                 begin = mid+1
#             else:
#                 end = mid - 1
#         return end
#
#     def helper(self,tar_ind):
#         tar_digit = self.digits[tar_ind]
#         if tar_ind == len(self.digits)-1:
#             last_ele = list(self.cnt.keys())[0]
#             if last_ele>tar_digit:
#                 return [last_ele]
#             else:
#                 return []
#         res = []
#         for chosen_digit in range(tar_digit,10):
#             if chosen_digit in self.cnt:
#                 res.append(chosen_digit)
#                 self.cnt[chosen_digit]-=1
#                 if self.cnt[chosen_digit]==0:
#                     self.cnt.pop(chosen_digit)
#                 if chosen_digit>tar_digit:
#                     next_res = []
#                     for d,cnt in self.cnt.items():
#                         for _ in range(cnt):
#                             next_res.append(d)
#                     next_res.sort()
#                     return res+next_res
#                 next_res = self.helper(tar_ind+1)
#                 if not next_res:
#                     res = []
#                     self.cnt[chosen_digit] = self.cnt.setdefault(chosen_digit,0)+1
#                 else:
#                     return res+next_res
#         return res

class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        stack = []
        while n:
            lsd = n%10
            n //= 10
            if not stack or lsd>=stack[-1]:
                stack.append(lsd)
            else:
                lsds_arr = [stack.pop()]
                while stack and stack[-1]>lsd:
                    lsds_arr.append(stack.pop())
                n = n*10+lsds_arr.pop()
                for d in stack:
                    n = n*10+d
                n = n*10+lsd
                for d in lsds_arr[::-1]:
                    n = n*10+d
                return n if n<2**31 else -1
        return -1