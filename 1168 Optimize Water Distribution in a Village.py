# There are n houses in a village. We want to supply water for all the houses by building wells and laying pipes.

# For each house i, we can either build a well inside it directly with cost wells[i - 1] (note the -1 due to 0-indexing), or pipe in water from another well to it. The costs to lay pipes between houses are given by the array pipes, where each pipes[j] = [house1j, house2j, costj] represents the cost to connect house1j and house2j together using a pipe. Connections are bidirectional.

# Return the minimum total cost to supply water to all houses.

 

# Example 1:



# Input: n = 3, wells = [1,2,2], pipes = [[1,2,1],[2,3,1]]
# Output: 3
# Explanation: 
# The image shows the costs of connecting houses using pipes.
# The best strategy is to build a well in the first house with cost 1 and connect the other houses to it with cost 2 so the total cost is 3.
 

# Constraints:

# 1 <= n <= 104
# wells.length == n
# 0 <= wells[i] <= 105
# 1 <= pipes.length <= 104
# pipes[j].length == 3
# 1 <= house1j, house2j <= n
# 0 <= costj <= 105
# house1j != house2j
class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        vn = 0
        for i,w in enumerate(wells):
            pipes.append([vn,i+1,w])
        pipes.sort(key=lambda x: x[2])
        self.parent = list(range(n+1))
        self.rank = [0]*(n+1)
        weights = 0
        for n1,n2,w in pipes:
            p1,p2 = self.find_parent(n1),self.find_parent(n2)
            if p1 != p2:
                weights += w
                self.union(p1,p2)
        return weights
        
    def find_parent(self,ind):
        if self.parent[ind] == ind:
            return ind
        self.parent[ind] = self.find_parent(self.parent[ind])
        return self.parent[ind]
    
    def union(self,ind1,ind2):
        p1,p2 = self.find_parent(ind1),self.find_parent(ind2)
        if p1!=p2:
            if self.rank[p1] > self.rank[p2]:
                self.parent[p2] = p1
            elif self.rank[p1] < self.rank[p2]:
                self.parent[p1] = p2
            else:
                self.parent[p1] = p2
                self.rank[p2] += 1
        