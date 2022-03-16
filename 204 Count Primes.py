# Count the number of prime numbers less than a non-negative number, n.

 

# Example 1:

# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# Example 2:

# Input: n = 0
# Output: 0
# Example 3:

# Input: n = 1
# Output: 0
 

# Constraints:

# 0 <= n <= 5 * 106
# Accepted
# 486,140
# Submissions
# 1,482,370
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2:
            return 0            
        arr = [1]*n
        arr[0]=arr[1]=0
        for i in range(2,n):
            if arr[i]==1:
                j=2
                a = i*j
                while a<n:
                    arr[a]=0
                    j+=1
                    a=i*j
        return sum(arr)