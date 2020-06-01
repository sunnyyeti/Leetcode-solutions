# Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

 

# Example 1:

# Input: s1 = "ab" s2 = "eidbaooo"
# Output: True
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input:s1= "ab" s2 = "eidboaoo"
# Output: False
 

# Constraints:

# The input strings only contain lower case letters.
# The length of both given strings is in range [1, 10,000].
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char_cnt = {}
        for c in s1:
            char_cnt[c] = char_cnt.get(c,0)+1
        origin_cnt = char_cnt.copy()
        start = 0
        i = 0
        while i<len(s2):
            cur_char = s2[i]
            if cur_char not in origin_cnt:
                i+=1
                start = i
                char_cnt = origin_cnt.copy()
            else:
                if cur_char in char_cnt:
                    char_cnt[cur_char]-=1
                    if char_cnt[cur_char]==0:
                        del char_cnt[cur_char]
                    #print(char_cnt)
                    if not char_cnt:
                        return True
                    i+=1
                else: #  减过头了
                    #print(start)
                    char_cnt[s2[start]] = char_cnt.get(s2[start],0)+1
                    start+=1
        return False
                
        