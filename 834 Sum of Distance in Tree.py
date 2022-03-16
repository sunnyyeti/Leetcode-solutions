# There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

# You are given the integer n and the array edges where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

# Return an array answer of length n where answer[i] is the sum of the distances between the ith node in the tree and all other nodes.

 

# Example 1:


# Input: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
# Output: [8,12,6,10,10,10]
# Explanation: The tree is shown above.
# We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
# equals 1 + 1 + 2 + 2 + 2 = 8.
# Hence, answer[0] = 8, and so on.
# Example 2:


# Input: n = 1, edges = []
# Output: [0]
# Example 3:


# Input: n = 2, edges = [[1,0]]
# Output: [1,1]
 

# Constraints:

# 1 <= n <= 3 * 104
# edges.length == n - 1
# edges[i].length == 2
# 0 <= ai, bi < n
# ai != bi
# The given input represents a valid tree.
from functools import cache


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = {}
        for a, b in edges:
            graph.setdefault(a, []).append(b)
            graph.setdefault(b, []).append(a)

        @cache
        def helper(node, parent) -> Tuple[int, int]:
            # 用dp 解决
            # 对每一个node，当parent确定的时候，子树数目 和  距离之和（自己和自己距离为零）
            children = graph.get(node, [])
            children_num_dis = [helper(child, node)
                                for child in children if child != parent]
            if not children_num_dis:
                return 1, 0
            total_num = sum(map(lambda x: x[0], children_num_dis))+1
            total_dis = sum(map(sum, children_num_dis))
            return total_num, total_dis
        ans = [0]*n
        for i in range(n):
            ans[i] = helper(i, None)[1]
        return ans
