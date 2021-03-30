# Given a string num that contains only digits and an integer target, return all possibilities to add the binary operators '+', '-', or '*' between the digits of num so that the resultant expression evaluates to the target value.

 

# Example 1:

# Input: num = "123", target = 6
# Output: ["1*2*3","1+2+3"]
# Example 2:

# Input: num = "232", target = 8
# Output: ["2*3+2","2+3*2"]
# Example 3:

# Input: num = "105", target = 5
# Output: ["1*0+5","10-5"]
# Example 4:

# Input: num = "00", target = 0
# Output: ["0*0","0+0","0-0"]
# Example 5:

# Input: num = "3456237490", target = 9191
# Output: []
 

# Constraints:

# 1 <= num.length <= 10
# num consists of only digits.
# -231 <= target <= 231 - 1
import re
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        #return []
        ans = [""]*(2*len(num)-1)
        for i,c in enumerate(num):
            ans[2*i] = c
        ops = ['+','-','*','']
        res = []
        def help(i):
            if i==(2*len(num)-1):
                exp = ''.join(ans)                
                if eval(exp) == target:
                    res.append(exp)
            else:
                for op in ops:
                    if op=='' and ans[i-1]=='0' and (i<2 or ans[i-2] in ['+','*','-']):
                        continue
                    ans[i] = op
                    help(i+2)
        help(1)
        return res