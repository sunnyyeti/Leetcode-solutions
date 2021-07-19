# From any string, we can form a subsequence of that string by deleting some number of characters (possibly no deletions).

# Given two strings source and target, return the minimum number of subsequences of source such that their concatenation equals target. If the task is impossible, return -1.

 

# Example 1:

# Input: source = "abc", target = "abcbc"
# Output: 2
# Explanation: The target "abcbc" can be formed by "abc" and "bc", which are subsequences of source "abc".
# Example 2:

# Input: source = "abc", target = "acdbc"
# Output: -1
# Explanation: The target string cannot be constructed from the subsequences of source string due to the character "d" in target string.
# Example 3:

# Input: source = "xyz", target = "xzyxz"
# Output: 3
# Explanation: The target string can be constructed as follows "xz" + "y" + "xz".
 

# Constraints:

# Both the source and target strings consist of only lowercase English letters from "a"-"z".
# The lengths of source and target string are between 1 and 1000.
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        source_set_chars = set(source)
        for char in target:
            if char not in source_set_chars:
                return -1
        def sub_sequence(target_start):
            target_char = target[target_start]
            for char in source:
                if char == target_char:
                    target_start += 1
                    if target_start == len(target):
                        return target_start
                    target_char = target[target_start]
            return target_start
        target_start = 0
        cnt = 0
        while target_start < len(target):
            next_target_start = sub_sequence(target_start)
            cnt += 1
            target_start = next_target_start
        return cnt
                
        