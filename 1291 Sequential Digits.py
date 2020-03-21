# An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

# Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

 

# Example 1:

# Input: low = 100, high = 300
# Output: [123,234]
# Example 2:

# Input: low = 1000, high = 13000
# Output: [1234,2345,3456,4567,5678,6789,12345]
 

# Constraints:

# 10 <= low <= high <= 10^9
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        def digits(num,start,end):
            ans =[]
            for s in range(start,min(9-num+2,end+1)):
                v = 0
                for ad in range(num):
                    v = v*10+(s+ad)
                ans.append(v)
            return ans
        def num_ds(v):
            ov = v
            cnt = 0
            while v:
                cnt+=1
                v//=10
            return cnt,ov//(10**(cnt-1))
        lcnt,lmsd = num_ds(low)
        hcnt,hmsd = num_ds(high)
        #print(lcnt,lmsd)
        #print(hcnt,hmsd)
        ans = []
        for nds in range(lcnt,hcnt+1):
            if nds==lcnt:
                ans.extend(digits(nds,lmsd,9))
            elif nds==hcnt:
                ans.extend(digits(nds,1,hmsd))
            else:
                ans.extend(digits(nds,1,9))
        #print(ans)
        return [r  for r in ans if low<=r<=high]
        