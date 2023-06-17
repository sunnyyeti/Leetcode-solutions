# <!-- You are given a 0-indexed integer array nums representing the contents of a pile, where nums[0] is the topmost element of the pile.

# In one move, you can perform either of the following:

# If the pile is not empty, remove the topmost element of the pile.
# If there are one or more removed elements, add any one of them back onto the pile. This element becomes the new topmost element.
# You are also given an integer k, which denotes the total number of moves to be made.

# Return the maximum value of the topmost element of the pile possible after exactly k moves. In case it is not possible to obtain a non-empty pile after k moves, return -1.

 

# Example 1:

# Input: nums = [5,2,2,4,0,6], k = 4
# Output: 5
# Explanation:
# One of the ways we can end with 5 at the top of the pile after 4 moves is as follows:
# - Step 1: Remove the topmost element = 5. The pile becomes [2,2,4,0,6].
# - Step 2: Remove the topmost element = 2. The pile becomes [2,4,0,6].
# - Step 3: Remove the topmost element = 2. The pile becomes [4,0,6].
# - Step 4: Add 5 back onto the pile. The pile becomes [5,4,0,6].
# Note that this is not the only way to end with 5 at the top of the pile. It can be shown that 5 is the largest answer possible after 4 moves.
# Example 2:

# Input: nums = [2], k = 1
# Output: -1
# Explanation: 
# In the first move, our only option is to pop the topmost element of the pile.
# Since it is not possible to obtain a non-empty pile after one move, we return -1.
 

# Constraints:

# 1 <= nums.length <= 105
# 0 <= nums[i], k <= 109
#  -->
class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        if k==0:
            return nums[0]#apparent, because nums is not empty
        if k<len(nums):
            #if k is less then the length of nums
            #then we can remove the top k elements, then we get the k+1 element
            #or we can remove the top k-1 elements, then we append the max of the top k-1 elements
            #note that when k==1, k-1 is zero, we need to give the default value of max
            # there is no way to get the kth element in k moves
            return max(max(nums[:k-1],default=-1),nums[k])
        if k==len(nums):
            # if k equals to the length of nums
            # then we can remove the top k-1 elements, then we append the max of the top k-1 elments
            return max(nums[:k-1],default=-1)
        if (k-len(nums))%2==1:
            # if k is larger than the length of nums
            # the larger part is odd
            # then we can remove the k elements, then append the max, 
            # if there are still more moves needed, we can remove the max, and append the max again and repeat
            return max(nums)
        if len(nums) >= 2:
            # if the larger part is even and the nums contains at least two elements
            # then we can append the second max, append the max
            # if there are still other operations, we can remove the max and append the max and repeat
            return max(nums)
        # if larger part is even and only 1 element
        # then it must be empty in the end
        return -1
        
        
        