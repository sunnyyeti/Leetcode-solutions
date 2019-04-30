# Given a non-empty array of integers, return the k most frequent elements.

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
# Note:

# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
from collections import Counter
import heapq
class Solution(object):
    def topKFrequent_(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = Counter(nums)
        most_commons = counter.most_common(k)
        return [c[0] for c in most_commons]
        
    def topKFrequent(self,nums,k):
        counter = {}
        for n in nums:
            counter[n] = counter.get(n,0)+1
        heap = []
        pairs = list(counter.items())
        for i in range(k):
            heapq.heappush(heap,(pairs[i][1],pairs[i][0]))
        for i in range(k,len(pairs)):
            if pairs[i][1]>heap[0][0]:
                heapq.heapreplace(heap,(pairs[i][1],pairs[i][0]))
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans[::-1]
        
            
        