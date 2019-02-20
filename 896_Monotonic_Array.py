# An array is monotonic if it is either monotone increasing or monotone decreasing.

# An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

# Return true if and only if the given array A is monotonic.

 

# Example 1:

# Input: [1,2,2,3]
# Output: true
# Example 2:

# Input: [6,5,4,4]
# Output: true
# Example 3:

# Input: [1,3,2]
# Output: false
# Example 4:

# Input: [1,2,4,5]
# Output: true
# Example 5:

# Input: [1,1,1]
# Output: true
 

# Note:

# 1 <= A.length <= 50000
# -100000 <= A[i] <= 100000
class Solution:
    def isMonotonic(self, A: 'List[int]') -> 'bool':
        if len(A)<=2:
            return True
        for i in range(0,len(A)-1):
            if A[i]>A[i+1]:
                ini = -1
                break
            elif A[i]<A[i+1]:
                ini = 1
                break
        if i == len(A)-2:
            return True
        for j in range(i+1,len(A)-1):
            if (A[j]-A[j+1])*ini>0:
                return False
        return True
            