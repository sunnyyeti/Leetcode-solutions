# You may recall that an array arr is a mountain array if and only if:

# arr.length >= 3
# There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given an integer array arr, return the length of the longest subarray, which is a mountain. Return 0 if there is no mountain subarray.

 

# Example 1:

# Input: arr = [2,1,4,7,3,2,5]
# Output: 5
# Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
# Example 2:

# Input: arr = [2,2,2]
# Output: 0
# Explanation: There is no mountain.
 

# Constraints:

# 1 <= arr.length <= 104
# 0 <= arr[i] <= 104
 

# Follow up:

# Can you solve it using only one pass?
# Can you solve it in O(1) space?
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        max_length = 0
        state = "-"
        last_start = -1
        for i in range(1,len(arr)):
            cur = arr[i]
            last = arr[i-1]
            cur_state = "/" if cur>last else "\\" if cur<last else "-"
            if state == "-":
                if cur_state=="/":
                    last_start = i-1
                    state = "/"
            if state == "/":
                if cur_state == "-":
                    state = "-"
                if cur_state == "\\":
                    state = "\\"
            if state == "\\":
                if cur_state == "-":
                    state = "-"
                    cur_length = i-last_start
                    max_length = max(max_length,cur_length)
                if cur_state == "/":
                    cur_length = i - last_start
                    max_length = max(max_length,cur_length)
                    state = "/"
                    last_start = i-1
        if state == "\\":
            max_length = max(max_length,len(arr)-last_start)
        return max_length
        
                    
                    
                    

            
        