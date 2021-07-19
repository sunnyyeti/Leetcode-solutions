# In a string s of lowercase letters, these letters form consecutive groups of the same character.

# For example, a string like s = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z", and "yy".

# A group is identified by an interval [start, end], where start and end denote the start and end indices (inclusive) of the group. In the above example, "xxxx" has the interval [3,6].

# A group is considered large if it has 3 or more characters.

# Return the intervals of every large group sorted in increasing order by start index.

 

# Example 1:

# Input: s = "abbxxxxzzy"
# Output: [[3,6]]
# Explanation: "xxxx" is the only large group with start index 3 and end index 6.
# Example 2:

# Input: s = "abc"
# Output: []
# Explanation: We have groups "a", "b", and "c", none of which are large groups.
# Example 3:

# Input: s = "abcdddeeeeaabbbcd"
# Output: [[3,5],[6,9],[12,14]]
# Explanation: The large groups are "ddd", "eeee", and "bbb".
# Example 4:

# Input: s = "aba"
# Output: []
 

# Constraints:

# 1 <= s.length <= 1000
# s contains lower-case English letters only.
class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        ans = []
        if len(s) < 3:
            return ans
        prev_char = s[0]
        prev_start = 0
        for i in range(1, len(s)):
            cur_char = s[i]
            if cur_char != prev_char:
                group_size = i-prev_start
                if group_size > 2:
                    ans.append([prev_start, i-1])
                prev_char = cur_char
                prev_start = i
        if len(s)-prev_start > 2:
            ans.append([prev_start, len(s)-1])
        return ans
