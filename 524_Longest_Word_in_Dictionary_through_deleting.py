# Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

# Example 1:
# Input:
# s = "abpcplea", d = ["ale","apple","monkey","plea"]

# Output: 
# "apple"
# Example 2:
# Input:
# s = "abpcplea", d = ["a","b","c"]

# Output: 
# "a"
# Note:
# All the strings in the input will only contain lower-case letters.
# The size of the dictionary won't exceed 1,000.
# The length of all the strings in the input won't exceed 1,000.
class Solution:
    def findLongestWord(self, s: 'str', d: 'List[str]') -> 'str':
        ans = ""
        for can in d:
            if self.issubstring(can,s):
                if self.isbetter(can,ans):
                    ans = can
        return ans


    def isbetter(self,str1,str2):
        if len(str1)>len(str2):
            return True
        if len(str1)<len(str2):
            return False
        return str1<str2

    def issubstring(self,str1,str2):
        if not str1:
            return True
        if not str2:
            return False
        i = 0
        tar = str1[0]
        for c in str2:
            if c==tar:
                i+=1
                if i==len(str1):
                    return True
                tar = str1[i]
        return False

class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        def is_reachable(s1,s2):
            i,j = 0,0
            t = s2[j]
            while i<len(s1):
                if s1[i]==t:
                    j+=1
                    if j==len(s2):
                        return True
                    t = s2[j]
                i+=1
            return False
        ans = ""
        for string in d:
            if is_reachable(s,string):
                #print(string)
                if len(string)>len(ans) or (len(string)==len(ans) and string<ans):
                    ans = string
        return ans