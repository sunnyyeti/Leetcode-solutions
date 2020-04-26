# Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.

# Example 1:

# Input: "2-1-1"
# Output: [0, 2]
# Explanation: 
# ((2-1)-1) = 0 
# (2-(1-1)) = 2
# Example 2:

# Input: "2*3-4*5"
# Output: [-34, -14, -10, -10, 10]
# Explanation: 
# (2*(3-(4*5))) = -34 
# ((2*3)-(4*5)) = -14 
# ((2*(3-4))*5) = -10 
# (2*((3-4)*5)) = -10 
# (((2*3)-4)*5) = 10
# Accepted
# 92.4K
# Submissions
# 173K

class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        def combine(op,left,right):
            def cal(op,left,right):
                if op=="+":
                    return left+right
                if op=="*":
                    return left*right
                if op=="-":
                    return left-right
            return [cal(op,l,r)  for l in left for r in right]
        cache = {}
        def cals(i,j):
            if i==j:
                return [int(input[i])]
            if (i,j) in cache:
                return cache[(i,j)]
            ans = []
            for ind in range(i+1,j):
                if input[ind] in ["+","-","*"]:
                    left = cals(i,ind-1)
                    right = cals(ind+1,j)
                    ans.extend(combine(input[ind],left,right))
            if not ans:
                ans = [int(input[i:j+1])]
            cache[(i,j)] = ans
            return ans
        return cals(0,len(input)-1)
        