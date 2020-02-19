# Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in ascending order.

# Note:
# Input contains only lowercase English letters.
# Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc" or "zerone" are not permitted.
# Input length is less than 50,000.
# Example 1:
# Input: "owoztneoer"

# Output: "012"
# Example 2:
# Input: "fviefuro"

# Output: "45"

class Solution:
    def originalDigits(self, s: str) -> str:
        #digits = ["zero","one","two","three","four","five","six","seven","eight","nine"]
        cnt = {}
        for c in s:
            cnt[c] = cnt.get(c,0)+1
        #print(cnt)
        ans = [0]*10
        ans[0] = cnt.get('z',0)
        if ans[0]:
            for c in 'zero':
                cnt[c]-=ans[0]
        ans[2] = cnt.get('w',0)
        if ans[2]:
            for c in 'two':
                cnt[c]-=ans[2]
        ans[8] = cnt.get('g',0)
        if ans[8]:
            for c in 'eight':
                cnt[c]-=ans[8]
        
        ans[3] = cnt.get('h',0)
        if ans[3]:
            for c in 'three':
                cnt[c]-=ans[3]
                
        ans[4] = cnt.get('u',0)
        if ans[4]:
            for c in 'four':
                cnt[c]-=ans[4]
        
        ans[5] = cnt.get('f',0)
        if ans[5]:
            for c in 'five':
                cnt[c]-=ans[5]
        
        ans[1] = cnt.get('o',0)
        if ans[1]:
            for c in 'one':
                cnt[c]-=ans[1]
        ans[6] = cnt.get('x',0)
        if ans[6]:
            for c in 'six':
                cnt[c]-=ans[6]
        ans[7] = cnt.get('s',0)
        if ans[7]:
            for c in 'seven':
                cnt[c]-=ans[7]
        ans[9] = cnt.get('i',0)
        #print(ans)
        res = []
        for i,d in enumerate(ans):
            res.extend(str(i)*d)
        #print(res)
        return "".join(sorted(res))
        
        # z, zero
        # w, two
        # g, eight
        # h, three
        # u, four
        # f, five
        # o, one
        # x, six
        # s, seven
        # i, nine
        
        
        