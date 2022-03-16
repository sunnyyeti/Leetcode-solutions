# Given two strings low and high that represent two integers low and high where low <= high, return the number of strobogrammatic numbers in the range [low, high].

# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

 

# Example 1:

# Input: low = "50", high = "100"
# Output: 3
# Example 2:

# Input: low = "0", high = "0"
# Output: 1
 

# Constraints:

# 1 <= low.length, high.length <= 15
# low and high consist of only digits.
# low <= high
# low and high do not contain any leading zeros except for zero itself.
class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        self.rotates = {
            '0':'0',
            '1':'1',
            '6':'9',
            '8':'8',
            '9':'6'
        }
        self.low = low
        self.high = high
        self.cnt = 0
        length_low = len(low)
        length_high = len(high)
        self.cnt += sum(self.number_at_length(l) for l in range(length_low+1,length_high))
        if length_low==length_high:
            self.construct_length(length_low)
        else:
            self.construct_length(length_low)
            self.construct_length(length_high)
        return self.cnt
        
    def construct_length(self,length):
        string_builder = ['']*length
        def bt(start,end):
            if start > end:
                self.cnt += int(self.low)<=int(''.join(string_builder))<=int(self.high)
                return
            for k,v in self.rotates.items():
                string_builder[start] = k
                string_builder[end] = v
                if length>1 and start==0 and k=='0':
                    continue
                if start == end and k!=v:
                    continue
                bt(start+1,end-1)
        bt(0,length-1)
                
        
    def number_at_length(self,length):
        if length == 1:
            return 3 #0,1,8
        if length == 2:
            return 4
        if length&1==0: # even
            return 5**(length//2)-5**(length//2-1)
        else:
            return 5**(length//2)*3 - 5**(length//2-1)*3
        
        
#         def number_at_length_range(length,low,up,ind,string_builder):
#             if length == 1:
#                 return sum(low<=c<=up  for c in ['0','1','8'] )
#             if ind == (length+1)//2:
#                 return int(low<=''.join(string_builder)<=up)
#             lf = low[ind]
#             uf = up[ind]
#             cnt = 0
#             for char in ['0','1','6','8','9']:
#                 if lf < char < uf:
#                     cnt += 1
#             if length&1 == 0: #even
#                 cnt *= 5**(length//2-ind-1)
#             else:
#                 cnt *= 5**(length//2-ind-1)*3 if ind < length//2 else 1
#             if lf in rotates:
#                 if length&1 and ind == length//2:
#                     if lf in ['0','1','8']:
#                         string_builder[ind] = lf
#                         cnt += number_at_length_range(length,low,up,ind+1,string_builder)
#                 else:
#                     string_builder[ind] = lf
#                     string_builder[length-1-ind] = rotates[lf]
#                     cnt += number_at_length_range(length,low,up,ind+1,string_builder)
#             if uf in rotates and uf!=lf:
#                 if length&1 and ind == length//2:
#                     if uf in ['0','1','8']:
#                         string_builder[ind] = uf
#                         cnt += number_at_length_range(length,low,up,ind+1,string_builder)
#                 else:
#                     string_builder[ind] = uf
#                     string_builder[length-1-ind] = rotates[uf]
#                     cnt += number_at_length_range(length,low,up,ind+1,string_builder)
#             return cnt
            
#         length_low = len(low)
#         length_high = len(high)
#         ans = sum(number_at_length(l) for l in range(length_low+1,length_high))
#         if length_low != length_high:
#             ans += number_at_length_range(length_low,low,'9'*length_low,0,['']*length_low)
#             ans += number_at_length_range(length_high,high,'1'+'0'*(length_high-1),0,['']*length_high)
#         else:
#             ans += number_at_length_range(length_low,low,high,0,['']*length_low)
#         return int(ans)
            

            
        