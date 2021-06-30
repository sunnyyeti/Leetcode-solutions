# Given an integer n, return all the strobogrammatic numbers that are of length n. You may return the answer in any order.

# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

 

# Example 1:

# Input: n = 2
# Output: ["11","69","88","96"]
# Example 2:

# Input: n = 1
# Output: ["0","1","8"]
 

# Constraints:

# 1 <= n <= 14
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        mappings = {
            '0':'0',
            '1':'1',
            '8':'8',
            '6':'9',
            '9':'6'
        }
        ans = []
        tmp = ['']*n
        def help(i,n):
            for k in mappings:
                tmp[i] = k
                if n%2 == 0:
                    tmp[n-1-i] = mappings[k]
                    if i==(n-1)//2:
                        ans.append(''.join(tmp))
                    else:
                        help(i+1,n)
                else:
                    if i==(n-1)//2:
                        if tmp[i] not in ['6','9']:
                            ans.append(''.join(tmp))
                    else:
                        tmp[n-1-i] = mappings[k]
                        help(i+1,n)
        help(0,n)
        if n>1:
            ans = [n for n in ans if not n.startswith('0')]
        return ans