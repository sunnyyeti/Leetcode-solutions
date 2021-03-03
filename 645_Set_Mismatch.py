# The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.

# Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

# Example 1:
# Input: nums = [1,2,2,4]
# Output: [2,3]
# Note:
# The given array size will in the range [2, 10000].
# The given array's numbers won't have any order.


class Solution:
    def findErrorNums(self, nums: 'List[int]') -> 'List[int]':
        occured = set()
        acc_sum = 0
        i = 0
        max_v = 0
        while i<len(nums):
            n = nums[i]
            if n in occured:
                rep = n
            else:
                occured.add(n)
                acc_sum+=n
                max_v = max(max_v,n)
            i+=1
        missing = (max_v+1)*max_v//2-acc_sum
        if missing==0:
            missing = max_v+1
        return [rep,missing]

        
class Solution1:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                rep =  nums[i]
        miss = (1+len(nums))*len(nums)//2-sum(nums)+rep
        return [rep,miss]