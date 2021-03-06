# Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time.

# Return that integer.

 

# Example 1:

# Input: arr = [1,2,2,6,6,6,6,7,10]
# Output: 6
 

# Constraints:

# 1 <= arr.length <= 10^4
# 0 <= arr[i] <= 10^5
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        thres = len(arr)//4
        cur = None
        cnt = -1
        for i,a in enumerate(arr):
            if a==cur:
                cnt+=1
            else:
                if cnt>thres:
                    return arr[i-1]
                cnt= 1
                cur = a
        if cur>thres:
            return a