# Write a program to find the n-th ugly number.

# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

# Example:

# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
# Note:  

# 1 is typically treated as an ugly number.
# n does not exceed 1690.
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        uglys = [1]
        i2,i3,i5=0,0,0
        while len(uglys)<n:
            n2,n3,n5 =uglys[i2]*2,uglys[i3]*3,uglys[i5]*5 
            new_ugly = min(n2,n3,n5)
            uglys.append(new_ugly)
            if new_ugly==n2:
                i2+=1
            if new_ugly==n3:
                i3+=1
            if new_ugly==n5:
                i5+=1
        return uglys[-1]
                
            