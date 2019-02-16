# You are given an array of positive and negative integers. If a number n at an index is positive, then move forward n steps. Conversely, if it's negative (-n), move backward n steps. Assume the first element of the array is forward next to the last element, and the last element is backward next to the first element. Determine if there is a loop in this array. A loop starts and ends at a particular index with more than 1 element along the loop. The loop must be "forward" or "backward'.

# Example 1: Given the array [2, -1, 1, 2, 2], there is a loop, from index 0 -> 2 -> 3 -> 0.

# Example 2: Given the array [-1, 2], there is no loop.

# Note: The given array is guaranteed to contain no element "0".

# Can you do it in O(n) time complexity and O(1) space complexity?
class Solution:
    def circularArrayLoop(self, nums: 'List[int]') -> 'bool':
        if len(nums)<2:
            return False
        visited = [0]*len(nums)
        for i,n in enumerate(nums):
            path = 1
            flag=True
            while not visited[i]:
                visited[i]=path
                i = (i+n)%len(nums)
                next_n = nums[i]
                if n*next_n<0:
                    flag=False
                    break
                n=next_n
                path+=1
            if flag and path-visited[i]>1:
                return True
        return False