# Suppose you have N integers from 1 to N. We define a beautiful arrangement as an array that is constructed by these N numbers successfully if one of the following is true for the ith position (1 <= i <= N) in this array:

# The number at the ith position is divisible by i.
# i is divisible by the number at the ith position.
 

# Now given N, how many beautiful arrangements can you construct?

# Example 1:

# Input: 2
# Output: 2
# Explanation: 

# The first beautiful arrangement is [1, 2]:

# Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).

# Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).

# The second beautiful arrangement is [2, 1]:

# Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).

# Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.
 

# Note:

# N is a positive integer and will not exceed 15.
class Solution:
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        self.candidates = {}
        self.N = N
        for i in range(1,N+1):
            j = i
            while j<=N:
                self.candidates.setdefault(i,set()).add(j)
                self.candidates.setdefault(j,set()).add(i)
                j+=i
        #print(self.candidates)
        self.visited = set()
        return self.dfs(1)
    
    def dfs(self,ind):
        if ind>self.N:
            return 1
        cands = self.candidates[ind]
        cnt = 0
        for c in cands:
            if c not in self.visited:
                self.visited.add(c)
                cnt+= self.dfs(ind+1)
                self.visited.remove(c)
        return cnt
        
        
            

