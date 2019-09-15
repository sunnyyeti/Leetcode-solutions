# Given a string text, we are allowed to swap two of the characters in the string. Find the length of the longest substring with repeated characters.

 

# Example 1:

# Input: text = "ababa"
# Output: 3
# Explanation: We can swap the first 'b' with the last 'a', or the last 'b' with the first 'a'. Then, the longest repeated character substring is "aaa", which its length is 3.
# Example 2:

# Input: text = "aaabaaa"
# Output: 6
# Explanation: Swap 'b' with the last 'a' (or the first 'a'), and we get longest repeated character substring "aaaaaa", which its length is 6.
# Example 3:

# Input: text = "aaabbaaa"
# Output: 4
# Example 4:

# Input: text = "aaaaa"
# Output: 5
# Explanation: No need to swap, longest repeated character substring is "aaaaa", length is 5.
# Example 5:

# Input: text = "abcdef"
# Output: 1
 

# Constraints:

# 1 <= text.length <= 20000
# text consist of lowercase English characters only.

class Solution:
    def maxRepOpt1(self, text: str) -> int:
        alpha_span = {}
        spans = []
        prev_c = text[0]
        cur_span = 1
        for i in range(1,len(text)):##encode the string 'aaabaaa' -> [(a,3),(b,1),(a,3)]; 'ababa' -> [(a,1),(b,1),(a,1),(b,1),(a,1)]
            cur_c = text[i]
            if cur_c==prev_c:
                cur_span+=1
            else:
                spans.append((prev_c,cur_span))
                prev_c = cur_c
                cur_span=1
        spans.append((prev_c,cur_span))
        for c,p in spans:
            alpha_span.setdefault(c,[]).append(p) ## 'aaabaaa' -> {'a':[3,3],'b':[1]}
        max_repeat = float('-inf')
        for i in range(1,len(spans)-1): ## consider two consecutive spans with only one gap between them like 'aaabaaa'
            if spans[i-1][0]==spans[i+1][0] and spans[i][1]==1:
                max_repeat = max(max_repeat,spans[i-1][1]+(len(alpha_span[spans[i-1][0]])>2)+spans[i+1][1])
        for alpha in alpha_span: ## consider one-side block
            max_alpha_span = max(alpha_span[alpha])
            max_repeat = max(max_repeat,max_alpha_span+(len(alpha_span[alpha])>1))
        return max_repeat
            
        
                
            