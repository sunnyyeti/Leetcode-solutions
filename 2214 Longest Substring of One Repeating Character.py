# You are given a 0-indexed string s. You are also given a 0-indexed string queryCharacters of length k and a 0-indexed array of integer indices queryIndices of length k, both of which are used to describe k queries.

# The ith query updates the character in s at index queryIndices[i] to the character queryCharacters[i].

# Return an array lengths of length k where lengths[i] is the length of the longest substring of s consisting of only one repeating character after the ith query is performed.

 

# Example 1:

# Input: s = "babacc", queryCharacters = "bcb", queryIndices = [1,3,3]
# Output: [3,3,4]
# Explanation: 
# - 1st query updates s = "bbbacc". The longest substring consisting of one repeating character is "bbb" with length 3.
# - 2nd query updates s = "bbbccc". 
#   The longest substring consisting of one repeating character can be "bbb" or "ccc" with length 3.
# - 3rd query updates s = "bbbbcc". The longest substring consisting of one repeating character is "bbbb" with length 4.
# Thus, we return [3,3,4].
# Example 2:

# Input: s = "abyzz", queryCharacters = "aa", queryIndices = [2,1]
# Output: [2,3]
# Explanation:
# - 1st query updates s = "abazz". The longest substring consisting of one repeating character is "zz" with length 2.
# - 2nd query updates s = "aaazz". The longest substring consisting of one repeating character is "aaa" with length 3.
# Thus, we return [2,3].
 

# Constraints:

# 1 <= s.length <= 105
# s consists of lowercase English letters.
# k == queryCharacters.length == queryIndices.length
# 1 <= k <= 105
# queryCharacters consists of lowercase English letters.
# 0 <= queryIndices[i] < s.length
from sortedcontainers import SortedList
from sortedcontainers import SortedDict
from typing import  List

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        intervals = SortedList()
        length2ints = SortedDict()
        int2char = {}
        prev_ind = 0
        for i, char in enumerate(s):
            if char != s[prev_ind]:
                intervals.add((prev_ind, i - 1))
                int2char[(prev_ind, i - 1)] = s[prev_ind]
                prev_ind = i
        intervals.add((prev_ind, len(s) - 1))
        int2char[(prev_ind, len(s) - 1)] = s[prev_ind]
        ans = []
        for s, e in intervals:
            length = e - s + 1
            length2ints[length] = length2ints.get(length,0)+1

        def remove_interval(interval):
            intervals.remove(interval)
            int2char.pop(interval)
            rm_int_len = interval[1] - interval[0] + 1
            length2ints[rm_int_len]-=1
            if length2ints[rm_int_len] == 0:
                length2ints.pop(rm_int_len)

        def add_interval(interval, char):
            intervals.add(interval)
            int2char[interval] = char
            new_len = interval[1] - interval[0] + 1
            length2ints[new_len] = length2ints.get(new_len,0)+1

        for char, ind in zip(queryCharacters, queryIndices):
            insert = intervals.bisect_left((ind, ind))
            insert = min(insert,len(intervals)-1)
            cur_interval = intervals[insert]
            cur_s, cur_e = cur_interval
            if not cur_s <= ind <= cur_e:
                insert -= 1
                cur_interval = intervals[insert]
                cur_s, cur_e = cur_interval
            removed = set()
            added = set()
            cur_char = int2char[cur_interval]
            if char == cur_char:
                ans.append(length2ints.keys()[-1])
            elif cur_s == cur_e:
                new_s, new_e = cur_s, cur_e
                prev_ind = insert - 1
                next_ind = insert + 1
                removed.add(cur_interval)
                if prev_ind >= 0:
                    prev_interval = intervals[prev_ind]
                    prev_interval_char = int2char[prev_interval]
                    if char == prev_interval_char:
                        new_s = prev_interval[0]
                        removed.add(prev_interval)
                if next_ind < len(intervals):
                    next_interval = intervals[next_ind]
                    next_interval_char = int2char[next_interval]
                    if char == next_interval_char:
                        new_e = next_interval[1]
                        removed.add(next_interval)
                for rm_int in removed:
                    remove_interval(rm_int)
                add_interval((new_s, new_e), char)
                ans.append(length2ints.keys()[-1])
            elif ind == cur_s:
                prev_ind = insert - 1
                removed.add(cur_interval)
                prev_same = False
                if prev_ind >= 0:
                    prev_interval = intervals[prev_ind]
                    prev_interval_char = int2char[prev_interval]
                    if char == prev_interval_char:
                        prev_same = True
                        removed.add(prev_interval)
                        added.add((prev_interval[0], cur_s, char))
                        added.add((cur_s + 1, cur_e, cur_char))
                if not prev_same:
                    added.add((cur_s, cur_s, char))
                    added.add((cur_s + 1, cur_e, cur_char))
                for rm in removed:
                    remove_interval(rm)
                for ad in added:
                    add_interval(ad[:2], ad[2])
                ans.append(length2ints.keys()[-1])
            elif ind == cur_e:
                next_ind = insert + 1
                removed.add(cur_interval)
                next_same = False
                if next_ind < len(intervals):
                    next_interval = intervals[next_ind]
                    next_interval_char = int2char[next_interval]
                    if char == next_interval_char:
                        next_same = True
                        removed.add(next_interval)
                        added.add((cur_e, next_interval[1], char))
                        added.add((cur_s, cur_e - 1, cur_char))
                if not next_same:
                    added.add((cur_e, cur_e, char))
                    added.add((cur_s, cur_e - 1, cur_char))
                for rm in removed:
                    remove_interval(rm)
                for ad in added:
                    add_interval(ad[:2], ad[2])
                ans.append(length2ints.keys()[-1])
            else:
                removed.add(cur_interval)
                added.add((ind, ind, char))
                added.add((cur_s, ind - 1, cur_char))
                added.add((ind + 1, cur_e, cur_char))
                for rm in removed:
                    remove_interval(rm)
                for ad in added:
                    add_interval(ad[:2], ad[2])
                ans.append(length2ints.keys()[-1])
        return ans