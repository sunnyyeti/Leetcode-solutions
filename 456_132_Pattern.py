# Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak such that i < j < k and ai < ak < aj. Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.

# Note: n will be less than 15,000.

# Example 1:
# Input: [1, 2, 3, 4]

# Output: False

# Explanation: There is no 132 pattern in the sequence.
# Example 2:
# Input: [3, 1, 4, 2]

# Output: True

# Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
# Example 3:
# Input: [-1, 3, 2, 0]

# Output: True

# Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
class Solution:
    def find132pattern(self, nums: 'List[int]') -> 'bool':
        if len(nums)<3:
            return False
        stack = [nums[0]]
        candidate = []
        for i in range(1,len(nums)):
            cur_num = nums[i]
            if candidate:
                for can in candidate:
                    if can[0]<cur_num<can[-1]:
                        return True
            if len(stack)==2:
                if stack[0]<cur_num<stack[-1]:
                    return True
                if cur_num>stack[-1]:
                    stack[-1] = cur_num
                elif cur_num<stack[0]:
                    if candidate and stack[0]<=candidate[-1][0] and stack[-1]>=candidate[-1][1]:
                        candidate[-1]=stack
                    else:
                        candidate.append(stack)
                    stack = [cur_num]
            else:
                if cur_num<stack[0]:
                    stack[0] =cur_num
                elif cur_num-stack[0]>1:
                    stack.append(cur_num)
        return False