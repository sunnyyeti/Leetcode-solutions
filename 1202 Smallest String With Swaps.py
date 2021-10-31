# You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.

# You can swap the characters at any pair of indices in the given pairs any number of times.

# Return the lexicographically smallest string that s can be changed to after using the swaps.

 

# Example 1:

# Input: s = "dcab", pairs = [[0,3],[1,2]]
# Output: "bacd"
# Explaination: 
# Swap s[0] and s[3], s = "bcad"
# Swap s[1] and s[2], s = "bacd"
# Example 2:

# Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
# Output: "abcd"
# Explaination: 
# Swap s[0] and s[3], s = "bcad"
# Swap s[0] and s[2], s = "acbd"
# Swap s[1] and s[2], s = "abcd"
# Example 3:

# Input: s = "cba", pairs = [[0,1],[1,2]]
# Output: "abc"
# Explaination: 
# Swap s[0] and s[1], s = "bca"
# Swap s[1] and s[2], s = "bac"
# Swap s[0] and s[1], s = "abc"
 

# Constraints:

# 1 <= s.length <= 10^5
# 0 <= pairs.length <= 10^5
# 0 <= pairs[i][0], pairs[i][1] < s.length
# s only contains lower case English letters.
class UF:
    def __init__(self,length):
        self.parent = list(range(length))
        self.rank = [0]*length
        
    def find_parent(self,ind):
        if self.parent[ind] == ind:
            return ind
        self.parent[ind] = self.find_parent(self.parent[ind])
        return self.parent[ind]
    
    def union(self,ind1,ind2):
        p1,p2 = self.find_parent(ind1),self.find_parent(ind2)
        if self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        elif self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        else:
            self.parent[p1] = p2
            self.rank[p2] += 1
    
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        chars = list(s)
        uf = UF(len(s))
        for a,b in pairs:
            uf.union(a,b)
        groups = {}
        for i in range(len(s)):
            groups.setdefault(uf.find_parent(i),[]).append(i)
        for _, inds in groups.items():
            cand_chars = [chars[i] for i in inds]
            cand_chars.sort()
            for i,ind in enumerate(inds):
                chars[ind] = cand_chars[i]
        return ''.join(chars)
                