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
    def findAnagrams(self, s: 'str', p: 'str') -> 'List[int]':
        cnt = {}
        setp = set(p)
        ans = []
        for c in p:
            cnt[c] = cnt.setdefault(c,0)+1
        i = 0
        length = 0
        for j in range(len(s)):
            c = s[j]
            length+=1
            if c not in setp:
                while i<j:
                    addc = s[i]
                    if addc in cnt:
                        cnt[addc]+=1
                    else:
                        cnt[addc] = 1
                    i+=1
                i+=1
                length = 0
            else:
                if c in cnt:
                    cnt[c]-=1
                    if cnt[c]==0:
                        cnt.pop(c)
                else:
                    cnt[c] = cnt.setdefault(c,0)-1
                    while cnt[c]<0:
                        cnt[s[i]] = cnt.setdefault(s[i], 0) + 1
                        i += 1
                        length -= 1
                    cnt.pop(c)

            if length == len(p) and len(cnt)==0:
                ans.append(i)
                cnt[s[i]] = 1
                i+=1
                length -=1
        return ans