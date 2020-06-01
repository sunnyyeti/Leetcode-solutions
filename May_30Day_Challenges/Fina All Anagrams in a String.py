# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

# The order of output does not matter.

# Example 1:

# Input:
# s: "cbaebabacd" p: "abc"

# Output:
# [0, 6]

# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:

# Input:
# s: "abab" p: "ab"

# Output:
# [0, 1, 2]

# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ps = set(p)
        p_c = {}
        for c in p:
            p_c[c] = p_c.get(c,0)+1
        orig_cnt = p_c.copy()
        start = 0
        ans = []
        i = 0
        while i<len(s):
            c = s[i]
            if c in ps:
                if c in p_c:
                    p_c[c]-=1
                    if p_c[c]==0:
                        del p_c[c]
                    if not p_c:
                        ans.append(start)
                        p_c[s[start]] = p_c.get(s[start],0)+1
                        start+=1
                    i+=1
                else:
                    p_c[s[start]] = p_c.get(s[start],0)+1
                    start+=1
            else:
                i+=1
                start = i
                p_c = orig_cnt.copy()
        return ans
   
        
                    