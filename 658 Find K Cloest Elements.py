# Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

# An integer a is closer to x than an integer b if:

# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b
 

# Example 1:

# Input: arr = [1,2,3,4,5], k = 4, x = 3
# Output: [1,2,3,4]
# Example 2:

# Input: arr = [1,2,3,4,5], k = 4, x = -1
# Output: [1,2,3,4]
 

# Constraints:

# 1 <= k <= arr.length
# 1 <= arr.length <= 104
# arr is sorted in ascending order.
# -104 <= arr[i], x <= 104
# Accepted
# 196,164
# Submissions
# 452,341
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ans = []
        left, right = 0, len(arr)-1
        while left <= right:
            mid = (left+right)//2
            if arr[mid] >= x:
                right = mid-1
            else:
                left = mid+1
        if 0 <= left < len(arr) and arr[left] == x:
            ans.append(x)
            i, j = left-1, left+1
        else:
            i, j = left-1, left
        while True:
            if len(ans) == k:
                break
            if i >= 0:
                cand1 = arr[i]
            else:
                cand1 = float('-inf')
            if j < len(arr):
                cand2 = arr[j]
            else:
                cand2 = float("inf")
            if abs(cand1-x) <= abs(cand2-x):
                ans.append(cand1)
                i -= 1
            else:
                ans.append(cand2)
                j += 1
        ans.sort()
        return ans
