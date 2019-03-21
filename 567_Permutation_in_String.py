# Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.
# Example 1:
# Input:s1 = "ab" s2 = "eidbaooo"
# Output:True
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:
# Input:s1= "ab" s2 = "eidboaoo"
# Output: False
# Note:
# The input strings only contain lower case letters.
# The length of both given strings is in range [1, 10,000].
import copy
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt = {}
        for s in s1:
            cnt[s] = cnt.setdefault(s,0)+1
        sets1 = set(s1)
        i=j=0
        copycnt = copy.deepcopy(cnt)
        while i<len(s2)-len(s1)+1:
            j = i
            while j<i+len(s1):
                if j==len(s2):
                    return False
                c = s2[j]
                if c not in sets1:
                    i = j+1
                    copycnt = copy.deepcopy(cnt)
                    break
                else:
                    if c in copycnt:
                        copycnt[c]-=1
                        if copycnt[c]==0:
                            copycnt.pop(c)
                        if len(copycnt)==0:
                            return True
                    else:
                        while s2[i]!=c:
                            copycnt[s2[i]] = copycnt.setdefault(s2[i],0)+1
                            i+=1
                        i+=1
                    j+=1
        return False
