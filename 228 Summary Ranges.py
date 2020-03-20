# Given a sorted integer array without duplicates, return the summary of its ranges.

# Example 1:

# Input:  [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
# Example 2:

# Input:  [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return nums
        if len(nums)==1:
            return [str(nums[0])]
        start = nums[0]
        ans = []
        for i in range(1,len(nums)):
            cur = nums[i]
            if cur-nums[i-1]!=1:
                if start!=nums[i-1]:
                    ans.append("{}->{}".format(start,nums[i-1]))
                else:
                    ans.append(str(start))
                start = cur
        if cur!=nums[i-1]+1:
            ans.append(str(cur))
        else:
            ans.append("{}->{}".format(start,cur))
        return ans
                