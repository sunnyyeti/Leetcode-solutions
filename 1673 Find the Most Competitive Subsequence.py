# Given an integer array nums and a positive integer k, return the most competitive subsequence of nums of size k.

# An array's subsequence is a resulting sequence obtained by erasing some (possibly zero) elements from the array.

# We define that a subsequence a is more competitive than a subsequence b (of the same length) if in the first position where a and b differ, subsequence a has a number less than the corresponding number in b. For example, [1,3,4] is more competitive than [1,3,5] because the first position they differ is at the final number, and 4 is less than 5.

 

# Example 1:

# Input: nums = [3,5,2,6], k = 2
# Output: [2,6]
# Explanation: Among the set of every possible subsequence: {[3,5], [3,2], [3,6], [5,2], [5,6], [2,6]}, [2,6] is the most competitive.
# Example 2:

# Input: nums = [2,4,3,3,5,4,9,6], k = 4
# Output: [2,3,3,4]
 

# Constraints:

# 1 <= nums.length <= 105
# 0 <= nums[i] <= 109
# 1 <= k <= nums.length
import math
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        height = int(math.ceil(math.log(len(nums),2)))
        cap = 2**(height+1)-1
        tree = [(-1,float("inf"))]*cap
        self.nums = nums
        self.construct(tree,0,len(nums)-1,0)
        ans = []
        last = -1
        for i in range(k):
            ind,val = self.get_min(tree,0,len(nums)-1,last+1,len(nums)-k+i,0)
            last = ind
            ans.append(val)
        return ans
        
    def construct(self,tree,ss,se,ind):
        if ss==se:
            tree[ind] = (ss,self.nums[ss])
        else:
            mid = (ss+se)//2
            lind,lmin = self.construct(tree,ss,mid,ind*2+1)
            rind,rmin = self.construct(tree,mid+1,se,ind*2+2)
            if lmin<=rmin:
                tree[ind] = (lind,lmin)
            else:
                tree[ind] = (rind,rmin)
        return tree[ind]
    
    def get_min(self,tree,ss,se,qs,qe,ind):
        if qs<=ss and qe>=se:
            return tree[ind]
        if qs>se or qe<ss:
            return -1,float("inf")
        mid = (ss+se)//2
        lind,lmin = self.get_min(tree,ss,mid,qs,qe,ind*2+1)
        rind,rmin = self.get_min(tree,mid+1,se,qs,qe,ind*2+2)
        if lmin<=rmin:
            return lind,lmin
        else:
            return rind,rmin

import math
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        for i,v in enumerate(nums):
            #print(stack,i,v)
            while stack and v<stack[-1] and len(stack)+len(nums)-i>k:
                stack.pop()
            stack.append(v)
        return stack[:k]