# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

# Example 1:


# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9
 

# Constraints:

# n == height.length
# 0 <= n <= 3 * 104
# 0 <= height[i] <= 105
# Accepted
# 745,494
# Submissions
# 1,434,921
class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [0]
        for i in range(len(height)-1):
            h = height[i]
            left_max.append(max(h,left_max[-1]))
        right_max = [0]*len(height)
        for i in range(len(height)-1,0,-1):
            h = height[i]
            right_max[i-1] = max(h,right_max[i])
        #print(left_max)
        #print(right_max)
        ans = 0
        for i,h in enumerate(height):
            ans += max(min(left_max[i],right_max[i])-h,0)
        return ans
        
                