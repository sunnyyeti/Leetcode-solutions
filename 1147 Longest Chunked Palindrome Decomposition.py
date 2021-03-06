# Return the largest possible k such that there exists a_1, a_2, ..., a_k such that:

# Each a_i is a non-empty string;
# Their concatenation a_1 + a_2 + ... + a_k is equal to text;
# For all 1 <= i <= k,  a_i = a_{k+1 - i}.
 

# Example 1:

# Input: text = "ghiabcdefhelloadamhelloabcdefghi"
# Output: 7
# Explanation: We can split the string on "(ghi)(abcdef)(hello)(adam)(hello)(abcdef)(ghi)".
# Example 2:

# Input: text = "merchant"
# Output: 1
# Explanation: We can split the string on "(merchant)".
# Example 3:

# Input: text = "antaprezatepzapreanta"
# Output: 11
# Explanation: We can split the string on "(a)(nt)(a)(pre)(za)(tpe)(za)(pre)(a)(nt)(a)".
# Example 4:

# Input: text = "aaa"
# Output: 3
# Explanation: We can split the string on "(a)(a)(a)".
 

# Constraints:

# text consists only of lowercase English characters.
# 1 <= text.length <= 1000
class Solution:
    def longestDecomposition(self, text: str) -> int:
        ans = 0
        st = []
        start = 0
        end = len(text)-1
        while start<=end:
            tar = text[start]
            st.append(text[end])
            if st[-1]==tar:
                #print(st)
                ts,te = start,-1
                while te>=-len(st) and ts<len(text) and text[ts]==st[te]:
                    ts+=1
                    te-=1
                    #print(ts,te)
                if te<-len(st):
                    ans+=2
                    ans-=(end==start)
                    st = []
                    start=ts
            end-=1
        return ans
        
          
                    