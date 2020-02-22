# Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

# Note:
# The array size can be very large. Solution that uses too much extra space will not pass the judge.

# Example:

# int[] nums = new int[] {1,2,3,3,3};
# Solution solution = new Solution(nums);

# // pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
# solution.pick(3);

# // pick(1) should return 0. Since in the array only nums[0] is equal to 1.
# solution.pick(1);
import random
import bisect
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = [(n,i) for i,n in enumerate(nums)]
        self.nums.sort()

    def pick(self, target: int) -> int:
        left = bisect.bisect_left(self.nums,(target,-1))
        right = bisect.bisect_right(self.nums,(target,len(self.nums)))
        return self.nums[random.randint(left,right-1)][1]

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)