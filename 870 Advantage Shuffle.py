# Given two arrays A and B of equal size, the advantage of A with respect to B is the number of indices i for which A[i] > B[i].

# Return any permutation of A that maximizes its advantage with respect to B.

 

# Example 1:

# Input: A = [2,7,11,15], B = [1,10,4,11]
# Output: [2,11,7,15]
# Example 2:

# Input: A = [12,24,8,32], B = [13,25,32,11]
# Output: [24,32,8,12]
 

# Note:

# 1 <= A.length = B.length <= 10000
# 0 <= A[i] <= 10^9
# 0 <= B[i] <= 10^9
import bisect
class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        A.sort()
        lo = 0
        sorted_inds = sorted(range(len(B)),key=lambda x: B[x])
        ans = [-1]*len(B)
        for i,ind in enumerate(sorted_inds):
            bv = B[ind]
            inda = bisect.bisect_right(A,bv,lo,len(A))
            if inda < len(A):
                ans[ind] = A[inda]
                lo = inda+1
                A[inda] = -1
            else:
                k = 0
                for j in range(i,len(B)):
                    while A[k]==-1:
                        k+=1
                    ans[sorted_inds[j]] = A[k]
                    k+=1
                break
        return ans
        