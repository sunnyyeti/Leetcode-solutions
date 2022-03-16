# We are given n different types of stickers. Each sticker has a lowercase English word on it.

# You would like to spell out the given string target by cutting individual letters from your collection of stickers and rearranging them. You can use each sticker more than once if you want, and you have infinite quantities of each sticker.

# Return the minimum number of stickers that you need to spell out target. If the task is impossible, return -1.

# Note: In all test cases, all words were chosen randomly from the 1000 most common US English words, and target was chosen as a concatenation of two random words.

 

# Example 1:

# Input: stickers = ["with","example","science"], target = "thehat"
# Output: 3
# Explanation:
# We can use 2 "with" stickers, and 1 "example" sticker.
# After cutting and rearrange the letters of those stickers, we can form the target "thehat".
# Also, this is the minimum number of stickers necessary to form the target string.
# Example 2:

# Input: stickers = ["notice","possible"], target = "basicbasic"
# Output: -1
# Explanation:
# We cannot form the target "basicbasic" from cutting letters from the given stickers.
 

# Constraints:

# n == stickers.length
# 1 <= n <= 50
# 1 <= stickers[i].length <= 10
# 1 <= target <= 15
# stickers[i] and target consist of lowercase English letters.
from collections import Counter
from functools import cache


class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        target_chars = set(target)
        stickers = [''.join(char for char in s if char in target_chars)
                    for s in stickers]
        stickers = [s for s in stickers if s]

        def is_greater(counter1, counter2):
            return all(counter2[key] <= counter1[key] for key in target_chars)
        to_be_removed = set()
        for i in range(len(stickers)-1):
            cnt1 = Counter(stickers[i])
            for j in range(i+1, len(stickers)):
                cnt2 = Counter(stickers[j])
                if cnt1 == cnt2:
                    to_be_removed.add(j)
                elif is_greater(cnt1, cnt2):
                    to_be_removed.add(j)
                elif is_greater(cnt2, cnt1):
                    to_be_removed.add(i)
        stickers = [s for i, s in enumerate(
            stickers) if i not in to_be_removed]

        @cache
        def min_num_from_ind(ind, target):
            if not target:
                return 0
            if ind >= len(stickers):
                return float('inf')
            cand1 = min_num_from_ind(ind+1, target)
            target_cnt = Counter(target)
            selected = stickers[ind]
            if not any(c in target_cnt for c in selected):
                return cand1
            for char in selected:
                target_cnt[char] -= 1
            new_target = []
            for char, cnt in target_cnt.items():
                if cnt > 0:
                    new_target.extend([char]*cnt)
            new_target = tuple(sorted(new_target))
            cand2 = min_num_from_ind(ind, new_target)+1
            return min(cand1, cand2)
        min_num = min_num_from_ind(0, tuple(sorted(target)))
        if min_num == float("inf"):
            return -1
        return min_num
