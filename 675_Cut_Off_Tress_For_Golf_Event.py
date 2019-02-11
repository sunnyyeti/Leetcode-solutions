# You are asked to cut off trees in a forest for a golf event. The forest is represented as a non-negative 2D map, in this map:

# 0 represents the obstacle can't be reached.
# 1 represents the ground can be walked through.
# The place with number bigger than 1 represents a tree can be walked through, and this positive number represents the tree's height.
 

# You are asked to cut off all the trees in this forest in the order of tree's height - always cut off the tree with lowest height first. And after cutting, the original place has the tree will become a grass (value 1).

# You will start from the point (0, 0) and you should output the minimum steps you need to walk to cut off all the trees. If you can't cut off all the trees, output -1 in that situation.

# You are guaranteed that no two trees have the same height and there is at least one tree needs to be cut off.

# Example 1:

# Input: 
# [
 # [1,2,3],
 # [0,0,4],
 # [7,6,5]
# ]
# Output: 6
 

# Example 2:

# Input: 
# [
 # [1,2,3],
 # [0,0,0],
 # [7,6,5]
# ]
# Output: -1
 

# Example 3:

# Input: 
# [
 # [2,3,4],
 # [0,0,5],
 # [8,7,6]
# ]
# Output: 6
# Explanation: You started from the point (0,0) and you can cut off the tree in (0,0) directly without walking.
 

# Hint: size of the given matrix will not exceed 50x50.

# Accepted
# 11,254
# Submissions
# 38,579
from collections import deque
class Solution:
    def cutOffTree(self, forest: 'List[List[int]]') -> 'int':
        rows = len(forest)
        if not rows:
            return 0
        cols = len(forest[0])
        if not cols:
            return 0
        trees = []
        for i in range(rows):
            for j in range(cols):
                if forest[i][j] > 1:
                    trees.append(forest[i][j])
        if not trees:
            return 0
        trees.sort()
        return self.min_steps(0,0,0,forest,trees,rows,cols)

    def min_steps(self,row,col,tar_ind,forest,trees,rows,cols):
        #print(rows,cols)
        total_steps = 0
        while tar_ind<len(trees):
            tar_height=trees[tar_ind]
            step,row,col  = self.bfs(row,col,tar_height,forest,rows,cols)
            if step==-1:
                return -1
            total_steps+=step
            tar_ind+=1
        return total_steps


    def bfs(self,row,col,tar_height,forest,rows,cols):
        queue = deque()
        queue.append((row,col,0))
        visited = set()
        visited.add((row,col))
        while queue:
            cur_r,cur_c,step = queue.popleft()
            if forest[cur_r][cur_c]==tar_height:
                return step,cur_r,cur_c
            if cur_r+1<rows and forest[cur_r+1][cur_c]!=0 and (cur_r+1,cur_c) not in visited:
                queue.append((cur_r+1,cur_c,step+1))
                visited.add((cur_r+1,cur_c))
            if cur_r-1>-1 and forest[cur_r-1][cur_c]!=0 and (cur_r-1,cur_c) not in visited:
                visited.add((cur_r-1,cur_c))
                queue.append((cur_r-1,cur_c,step+1))
            if cur_c+1<cols and forest[cur_r][cur_c+1]!=0 and (cur_r,cur_c+1) not in visited:
                queue.append((cur_r,cur_c+1,step+1))
                visited.add((cur_r,cur_c+1))
            if cur_c-1>-1 and forest[cur_r][cur_c-1]!=0 and (cur_r,cur_c-1) not in visited:
                queue.append((cur_r,cur_c-1,step+1))
                visited.add((cur_r,cur_c-1))
        return -1,None,None




