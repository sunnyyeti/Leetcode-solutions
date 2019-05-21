# A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

# Example 1:
# Input: S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
# Note:

# S will have length in range [1, 500].
# S will consist of lowercase letters ('a' to 'z') only.
class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        pos = {}
        for i, c in enumerate(S):
            pos[c] = max(pos.get(c, 0), i)
        cur_end = 0
        #par = 0
        last_pos = -1
        ans = []
        for i, c in enumerate(S):
            new_end = pos[c]
            cur_end = max(new_end, cur_end)
            if i == cur_end:
                ans.append(i-last_pos)
                last_pos = i
        return ans
            
            