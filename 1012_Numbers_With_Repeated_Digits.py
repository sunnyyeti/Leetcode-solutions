# Given a positive integer N, return the number of positive integers less than or equal to N that have at least 1 repeated digit.

 

# Example 1:

# Input: 20
# Output: 1
# Explanation: The only positive number (<= 20) with at least 1 repeated digit is 11.
# Example 2:

# Input: 100
# Output: 10
# Explanation: The positive numbers (<= 100) with atleast 1 repeated digit are 11, 22, 33, 44, 55, 66, 77, 88, 99, and 100.
# Example 3:

# Input: 1000
# Output: 262
 

# Note:

# 1 <= N <= 10^9
import math
class Solution:
    def numDupDigitsAtMostN(self, N: int) -> int:
        n_len = len(str(N))
        no_dp = 0
        for i in range(1,n_len+1):
            no_dp+=self.k_nodup(i)
        bigg_no_dp = self.bigger_than_no_duplicate(N)
        no_dp -= bigg_no_dp
        return N-no_dp


    def k_nodup(self, k):
        if k == 10:
            return math.factorial(9) * 9
        return math.factorial(9) // math.factorial(9 - k) + math.factorial(9) * (k - 1) // math.factorial(10 - k)

    def bigger_than_no_duplicate(self,n):
        def bigger_num_in_set(dset,tar):
            return len([d for d in dset if d >tar])
        def c(n,m):
            return math.factorial(n)//(math.factorial(n-m)*math.factorial(m))
        str_n = str(n)
        str_len = len(str_n)
        digits = set(range(10))
        occured = set()
        res = 0
        for i,d in enumerate(str_n):
            d = int(d)
            bigger_cnt = bigger_num_in_set(digits,d)
            tmp =  bigger_cnt*(c(len(digits)-1,str_len-i-1))*math.factorial(str_len-i-1)
            res+=tmp
            if d in digits:
                digits.remove(d)
            if d not in occured:
                occured.add(d)
            else:
                break
        return res