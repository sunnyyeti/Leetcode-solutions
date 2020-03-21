# Given n orders, each order consist in pickup and delivery services. 

# Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i). 

# Since the answer may be too large, return it modulo 10^9 + 7.

 

# Example 1:

# Input: n = 1
# Output: 1
# Explanation: Unique order (P1, D1), Delivery 1 always is after of Pickup 1.
# Example 2:

# Input: n = 2
# Output: 6
# Explanation: All possible orders: 
# (P1,P2,D1,D2), (P1,P2,D2,D1), (P1,D1,P2,D2), (P2,P1,D1,D2), (P2,P1,D2,D1) and (P2,D2,P1,D1).
# This is an invalid order (P1,D2,P2,D1) because Pickup 2 is after of Delivery 2.
# Example 3:

# Input: n = 3
# Output: 90
 

# Constraints:

# 1 <= n <= 500
class Solution:
    def countOrders(self, n: int) -> int:
        def fac(n):
            prod = 1
            i = 1
            while i<=n:
                prod*=i
                i+=1
            return prod
        def C(n,k):
            return fac(n)//(fac(k)*fac(n-k))
        pos = 2*n
        ans = 1
        for c in range(pos,0,-2):
            #print(c)
            ans*=C(c,2)
            #print(ans)
        return ans%(10**9+7)