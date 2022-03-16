# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.

 

# Example 1:

# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
# Example 3:

# Input: nums = [1,-1], k = 1
# Output: [1,-1]
# Example 4:

# Input: nums = [9,11], k = 2
# Output: [11]
# Example 5:

# Input: nums = [4,-2], k = 2
# Output: [4]
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# 1 <= k <= nums.length
# Accepted
# 428,985
# Submissions
# 947,451
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        first_max = float("-inf")
        first_max_ind = None
        for i in range(k):
            if nums[i] > first_max:
                first_max = nums[i]
                first_max_ind = i
        queue = deque([first_max_ind])
        for i in range(first_max_ind+1,k):
            cur_ele = nums[i]
            while queue and nums[queue[-1]]<=cur_ele:
                queue.pop()
            queue.append(i)
        ans = [first_max]
        for i in range(k,len(nums)):
            cur_ele = nums[i]
            while queue and queue[0] <= i-k:
                queue.popleft()
            while queue and nums[queue[-1]]<=cur_ele:
                queue.pop()
            queue.append(i)
            ans.append(nums[queue[0]])
        return ans