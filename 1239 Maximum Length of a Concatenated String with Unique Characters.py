# Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.

# Return the maximum possible length of s.


# Example 1:

# Input: arr = ["un", "iq", "ue"]
# Output: 4
# Explanation: All possible concatenations are "", "un", "iq", "ue", "uniq" and "ique".
# Maximum length is 4.
# Example 2:

# Input: arr = ["cha", "r", "act", "ers"]
# Output: 6
# Explanation: Possible solutions are "chaers" and "acters".
# Example 3:

# Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
# Output: 26


# Constraints:

# 1 <= arr.length <= 16
# 1 <= arr[i].length <= 26
# arr[i] contains only lower case English letters.

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        ans = 0

        def bt(ind):
            nonlocal ans
            if ind == len(arr):
                ans = max(ans, len(chars))
                return
            cur_str = arr[ind]
            if len(cur_str) == len(set(cur_str)) and all(c not in chars for c in cur_str):
                for c in cur_str:
                    chars.add(c)
                bt(ind+1)
                for c in cur_str:
                    chars.remove(c)
            bt(ind+1)
        chars = set()
        bt(0)
        return ans
