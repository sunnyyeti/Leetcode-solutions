# Given two sequences pushed and popped with distinct values, return true if and only if this could have been the result of a sequence of push and pop operations on an initially empty stack.

 

# Example 1:

# Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
# Output: true
# Explanation: We might do the following sequence:
# push(1), push(2), push(3), push(4), pop() -> 4,
# push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
# Example 2:

# Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
# Output: false
# Explanation: 1 cannot be popped before 2.
 

# Note:

# 0 <= pushed.length == popped.length <= 1000
# 0 <= pushed[i], popped[i] < 1000
# pushed is a permutation of popped.
# pushed and popped have distinct values.
# Accepted
# 8,404
# Submissions
# 14,548
class Solution:
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        if not pushed and not popped:
            return True
        if not pushed:
            return False
        if not popped:
            return False
        stack = []
        j = 0
        i = 0
        tar = popped[i]
        while True:
            while ((not stack) or stack[-1]!=tar) and (j<len(pushed)):
                stack.append(pushed[j])
                j+=1
            if (not stack) or stack[-1]!=tar:
                return False
            while (stack) and stack[-1]==tar:
                stack.pop()
                i+=1
                if i==len(popped):
                    return True
                tar = popped[i]