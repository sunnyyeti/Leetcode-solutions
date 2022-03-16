# Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

# Return all the possible results. You may return the answer in any order.

 

# Example 1:

# Input: s = "()())()"
# Output: ["(())()","()()()"]
# Example 2:

# Input: s = "(a)())()"
# Output: ["(a())()","(a)()()"]
# Example 3:

# Input: s = ")("
# Output: [""]
 

# Constraints:

# 1 <= s.length <= 25
# s consists of lowercase English letters and parentheses '(' and ')'.
# There will be at most 20 parentheses in s.
# Accepted
# 270,723
# Submissions
# 599,946
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        s = s.rstrip('(')
        s = s.lstrip(')')
        left,right = 0,0
        for c in s:
            if c=='(':
                left += 1
            elif c==')':
                if left==0:
                    right += 1
                else:
                    left -= 1
        ans = set()
        tmp = []
        def help(i,l,r,cnt):#l  how many left have been discarded, r: how many rights have been discarded, cnt: #left-#right (# number of)
            if i == len(s):
                if cnt==0: # only if cnt==0, then it is a valid parentheses
                    ans.add(''.join(tmp))
                return
            c = s[i]
            if c== '(':
                tmp.append(c) #not discarded
                cnt += 1
                help(i+1,l,r,cnt)
                tmp.pop()
                cnt -= 1
                if l < left: # if can be discarded
                    l += 1
                    help(i+1,l,r,cnt)
                    l -= 1
            elif c==')':
                if cnt > 0:
                    tmp.append(c) # not discarded
                    cnt -= 1
                    help(i+1,l,r,cnt)
                    tmp.pop()
                    cnt += 1
                if r<right: # if can be discarded
                    r+=1
                    help(i+1,l,r,cnt)
                    r-=1
            else:
                tmp.append(c)
                help(i+1,l,r,cnt)
                tmp.pop()
        help(0,0,0,0)
        return list(ans)
                    