# Given n cuboids where the dimensions of the ith cuboid is cuboids[i] = [widthi, lengthi, heighti] (0-indexed). Choose a subset of cuboids and place them on each other.

# You can place cuboid i on cuboid j if widthi <= widthj and lengthi <= lengthj and heighti <= heightj. You can rearrange any cuboid's dimensions by rotating it to put it on another cuboid.

# Return the maximum height of the stacked cuboids.

 

# Example 1:



# Input: cuboids = [[50,45,20],[95,37,53],[45,23,12]]
# Output: 190
# Explanation:
# Cuboid 1 is placed on the bottom with the 53x37 side facing down with height 95.
# Cuboid 0 is placed next with the 45x20 side facing down with height 50.
# Cuboid 2 is placed next with the 23x12 side facing down with height 45.
# The total height is 95 + 50 + 45 = 190.
# Example 2:

# Input: cuboids = [[38,25,45],[76,35,3]]
# Output: 76
# Explanation:
# You can't place any of the cuboids on the other.
# We choose cuboid 1 and rotate it so that the 35x3 side is facing down and its height is 76.
# Example 3:

# Input: cuboids = [[7,11,17],[7,17,11],[11,7,17],[11,17,7],[17,7,11],[17,11,7]]
# Output: 102
# Explanation:
# After rearranging the cuboids, you can see that all cuboids have the same dimension.
# You can place the 11x7 side down on all cuboids so their heights are 17.
# The maximum height of stacked cuboids is 6 * 17 = 102.
 

# Constraints:

# n == cuboids.length
# 1 <= n <= 100
# 1 <= widthi, lengthi, heighti <= 100
class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        for c in cuboids:
            c.sort()
        cuboids.sort(key=lambda x: (x[2], x[1], x[0]))
        dp = [0]*len(cuboids)
        dp[-1] = cuboids[-1][2]
        for i in range(len(dp)-2, -1, -1):
            max_h = 0
            w1, l1, h1 = cuboids[i]
            for j in range(i+1, len(dp)):
                w2, l2, h2 = cuboids[j]
                if w1 <= w2 and l1 <= l2 and h1 <= h2:
                    max_h = max(max_h, dp[j])
            dp[i] = h1+max_h
        return max(dp)
