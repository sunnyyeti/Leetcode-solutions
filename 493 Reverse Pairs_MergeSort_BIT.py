# Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

# You need to return the number of important reverse pairs in the given array.

# Example1:

# Input: [1,3,2,3,1]
# Output: 2
# Example2:

# Input: [2,4,3,5,1]
# Output: 3
# Note:
# The length of the given array will not exceed 50,000.
# All the numbers in the input array are in the range of 32-bit integer.
import bisect
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.ans = 0
        sorted_nums = sorted(set(nums))
        inds_map = {e:i for i,e in enumerate(sorted_nums)}
        bit = [0]*(len(inds_map)+1)
        for e in reversed(nums):
            t = e/2
            ind = bisect.bisect_left(sorted_nums,t)
            self.ans += self.get_sum_to(bit,ind-1)
            self.add_delta_to(bit,inds_map[e],1)
        return self.ans

    def get_sum_to(self, bit, ind):
        ind+=1
        ans = 0
        while ind>0:
            ans += bit[ind]
            ind -= ind&(-ind)
        return ans
    
    def add_delta_to(self,bit,ind,delta):
        ind+=1
        while ind<len(bit):
            bit[ind]+=delta
            ind+=ind&(-ind)