# Let's define a function f(s) over a non-empty string s, which calculates the frequency of the smallest character in s. For example, if s = "dcce" then f(s) = 2 because the smallest character is "c" and its frequency is 2.

# Now, given string arrays queries and words, return an integer array answer, where each answer[i] is the number of words such that f(queries[i]) < f(W), where W is a word in words.

 

# Example 1:

# Input: queries = ["cbd"], words = ["zaaaz"]
# Output: [1]
# Explanation: On the first query we have f("cbd") = 1, f("zaaaz") = 3 so f("cbd") < f("zaaaz").
# Example 2:

# Input: queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
# Output: [1,2]
# Explanation: On the first query only f("bbb") < f("aaaa"). On the second query both f("aaa") and f("aaaa") are both > f("cc").
 

# Constraints:

# 1 <= queries.length <= 2000
# 1 <= words.length <= 2000
# 1 <= queries[i].length, words[i].length <= 10
# queries[i][j], words[i][j] are English lowercase letters.
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        words_fs = [self.f(w) for w in words]
        words_fs.sort()
        return [self.lb(words_fs,self.f(q)) for q in queries]
    
    def f(self,word):
        sc = chr(ord('z')+1)
        sn = 0
        for c in word:
            if c<sc:
                sc=c
                sn=1
            elif c==sc:
                sn+=1
        return sn
    
    def lb(self,arr,tar):
        start,end = 0, len(arr)-1
        while start<=end:
            mid = (start+end)//2
            if arr[mid]>tar:
                end = mid-1
            else:
                start = mid+1
        return len(arr)-start