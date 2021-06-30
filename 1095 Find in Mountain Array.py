# (This problem is an interactive problem.)

# You may recall that an array A is a mountain array if and only if:

# A.length >= 3
# There exists some i with 0 < i < A.length - 1 such that:
# A[0] < A[1] < ... A[i-1] < A[i]
# A[i] > A[i+1] > ... > A[A.length - 1]
# Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target.  If such an index doesn't exist, return -1.

# You can't access the mountain array directly.  You may only access the array using a MountainArray interface:

# MountainArray.get(k) returns the element of the array at index k (0-indexed).
# MountainArray.length() returns the length of the array.
# Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer.  Also, any solutions that attempt to circumvent the judge will result in disqualification.

 

# Example 1:

# Input: array = [1,2,3,4,5,3,1], target = 3
# Output: 2
# Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.
# Example 2:

# Input: array = [0,1,2,4,2,1], target = 3
# Output: -1
# Explanation: 3 does not exist in the array, so we return -1.
 

# Constraints:

# 3 <= mountain_arr.length() <= 10000
# 0 <= target <= 10^9
# 0 <= mountain_arr.get(index) <= 10^9
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        length = mountain_arr.length()
        l, r = 0, length-1
        while l <= r:
            mid = l+(r-l)//2
            if 0 < mid < length-1:
                pre = mountain_arr.get(mid-1)
                nex = mountain_arr.get(mid+1)
                cur = mountain_arr.get(mid)
                if pre < cur and cur > nex:
                    break
                elif pre < cur:
                    l = mid + 1
                else:
                    r = mid - 1
            elif mid == 0:
                l = mid+1
            else:
                r = mid-1
        if cur == target:
            return mid
        #print(mid)

        def find1(l, r):
            while l <= r:
                mid = l+(r-l)//2
                cur = mountain_arr.get(mid)
                if cur == target:
                    return mid
                elif cur < target:
                    l = mid+1
                else:
                    r = mid-1
            return -1

        def find2(l, r):
            #print(l,r)
            while l <= r:
                mid = l+(r-l)//2
                cur = mountain_arr.get(mid)
                if cur == target:
                    return mid
                elif cur > target:
                    l = mid+1
                else:
                    r = mid-1
            return -1
        first_half = find1(0, mid-1)
        #print(first_half)
        if first_half != -1:
            return first_half
        second_half = find2(mid+1, length-1)
        return second_half
