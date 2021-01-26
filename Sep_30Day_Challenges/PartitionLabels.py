#  string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

 

# Example 1:

# Input: S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
 

# Note:

# S will have length in range [1, 500].
# S will consist of lowercase English letters ('a' to 'z') only.
 
 class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        inds = {}
        for i, c in enumerate(S):
            inds.setdefault(c,[]).append(i)
        curtar = 0
        i = 0
        res = [0]
        while True:
            curtar = inds[S[i]][-1]
            while i<=curtar:
                curc = S[i]
                newtar = inds[curc][-1]
                curtar = max(curtar,newtar)
                i+=1
            res.append(i)
            if i>=len(S):
                break
        return [res[i]-res[i-1] for i in range(1,len(res))]