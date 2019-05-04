# Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

# If possible, output any possible result.  If not possible, return the empty string.

# Example 1:

# Input: S = "aab"
# Output: "aba"
# Example 2:

# Input: S = "aaab"
# Output: ""
# Note:

# S will consist of lowercase letters and have length in range [1, 500].
 import heapq
class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        total = len(S)
        cnt = {}
        for c in S:
            cnt[c] = cnt.get(c,0)+1
        heap = [(total-i,c) for (c,i) in cnt.items()]
        heapq.heapify(heap)
        ans = [""]
        while heap:
            if ans[-1]!=heap[0][1]:
                ans.append(heap[0][1])
                if (heap[0][0]+1)!=total:
                    heapq.heappushpop(heap,(heap[0][0]+1,ans[-1]))
                else:
                    heapq.heappop(heap)
            else:
                store = heapq.heappop(heap)
                if not heap:
                    return ans[0]
                ans.append(heap[0][1])
                if (heap[0][0]+1)!=total:
                    heapq.heappushpop(heap,(heap[0][0]+1,ans[-1]))
                else:
                    heapq.heappop(heap)
                heapq.heappush(heap,store)
        return "".join(ans[1:])
