# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

 

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
 

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        self.parent = {}
        self.rank = {}
        seen = set()
        for n in nums:
            if n-1 in seen:
                self.union(n-1,n)
            if n+1 in seen:
                self.union(n+1,n)
            seen.add(n)
        cnt = {}
        for n in seen: 
            p = self.find_parent(n)
            cnt[p] = cnt.get(p,0)+1
        return max(cnt.values(),default=0)
    def find_parent(self,num):
        self.parent.setdefault(num,num)
        if self.parent[num]==num:
            return num
        else:
            self.parent[num] = self.find_parent(self.parent[num])
            return self.parent[num]
        
    def union(self,n1,n2):
        p1,p2 = self.find_parent(n1),self.find_parent(n2)
        if p1!=p2:
            if self.rank.get(p1,0) < self.rank.get(p2,0):
                self.parent[p1] = p2
                self.rank[p2] = self.rank.get(p2,0)+1
            elif self.rank.get(p1,0) > self.rank.get(p2,0):
                self.parent[p2] = p1
                self.rank[p1] = self.rank.get(p1,0)+1
            else:
                self.parent[p1]= p2
                self.rank[p2] = self.rank.get(p2,0)+1