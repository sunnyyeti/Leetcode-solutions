class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left,right = 0,0
        num_zeros = int(nums[left]==0)
        ans = 0
        while True:
            while right<len(nums) and num_zeros <= k:
                ans = max(ans,right-left+1)
                right+=1
                if right==len(nums):
                    break
                num_zeros += nums[right]==0
            if right==len(nums):
                break
            while num_zeros > k:
                num_zeros -= nums[left]==0
                left+=1
        return ans