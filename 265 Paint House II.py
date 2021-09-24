# There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

# The cost of painting each house with a certain color is represented by an n x k cost matrix costs.

# For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on...
# Return the minimum cost to paint all houses.

 

# Example 1:

# Input: costs = [[1,5,3],[2,9,4]]
# Output: 5
# Explanation:
# Paint house 0 into color 0, paint house 1 into color 2. Minimum cost: 1 + 4 = 5; 
# Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 + 2 = 5.
# Example 2:

# Input: costs = [[1,3],[2,4]]
# Output: 5
 

# Constraints:

# costs.length == n
# costs[i].length == k
# 1 <= n <= 100
# 1 <= k <= 20
# 1 <= costs[i][j] <= 20
 

# Follow up: Could you solve it in O(nk) runtime?
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        #O(nk^2)
        house_cnt, color_cnt = len(costs), len(costs[0])
        previous_costs = costs[0]
        for house_ind in range(1, house_cnt):
            new_costs = []
            for cur_color in range(color_cnt):
                min_cost = min(pre_color_cost for pre_color, pre_color_cost in enumerate(
                    previous_costs) if pre_color != cur_color)+costs[house_ind][cur_color]
                new_costs.append(min_cost)
            previous_costs = new_costs
        return min(previous_costs)
