# Given a string s, encode the string such that its encoded length is the shortest.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. k should be a positive integer.

# If an encoding process does not make the string shorter, then do not encode it. If there are several solutions, return any of them.

 

# Example 1:

# Input: s = "aaa"
# Output: "aaa"
# Explanation: There is no way to encode it such that it is shorter than the input string, so we do not encode it.
# Example 2:

# Input: s = "aaaaa"
# Output: "5[a]"
# Explanation: "5[a]" is shorter than "aaaaa" by 1 character.
# Example 3:

# Input: s = "aaaaaaaaaa"
# Output: "10[a]"
# Explanation: "a9[a]" or "9[a]a" are also valid solutions, both of them have the same length = 5, which is the same as "10[a]".
# Example 4:

# Input: s = "aabcaabcd"
# Output: "2[aabc]d"
# Explanation: "aabc" occurs twice, so one answer can be "2[aabc]d".
# Example 5:

# Input: s = "abbbabbbcabbbabbbc"
# Output: "2[2[abbb]c]"
# Explanation: "abbbabbbc" occurs twice, but "abbbabbbc" can also be encoded to "2[abbb]c", so one answer can be "2[2[abbb]c]".
 

# Constraints:

# 1 <= s.length <= 150
# s consists of only lowercase English letters.
from functools import cache


class Solution:
    def encode(self, s: str) -> str:
        self.s = s
        shortest = self.encode_from_to(0, len(s)-1)
        ans = self.strfy(shortest)
        return ans if len(ans) < len(s) else s

    def strfy(self, res_tuple):
        return res_tuple[1] if res_tuple[0] == 1 else f"{res_tuple[0]}[{res_tuple[1]}]"

    @cache
    def encode_from_to(self, start, end):
        def length(res_tuple):
            return len(res_tuple[1])+2+len(str(res_tuple[0]))

        if start == end:
            return 1, self.s[start]
        shortest = (1, self.s[start:end+1])
        for split in range(start+1, end+1):
            cnt1, substring1 = self.encode_from_to(start, split-1)
            cnt2, substring2 = self.encode_from_to(split, end)
            if substring1 == substring2:
                cnt = cnt1+cnt2
                new_pair = (cnt, substring1)

            else:
                substring1_full = self.strfy((cnt1, substring1))
                substring2_full = self.strfy((cnt2, substring2))
                new_pair = (1, substring1_full+substring2_full)
            if length(new_pair) < length(shortest):
                shortest = new_pair
        return shortest

        #print(start,end)
#         if start == end:
#             return self.s[start]
#         length = end-start+1
#         shortest_encoded = self.s[start:end+1]
#         for split in range(length,1,-1):
#             if length%split == 0:
#                 cnt_per_split = length//split
#                 if len(set(self.s[i:i+cnt_per_split] for i in range(start,end+1,cnt_per_split)))==1:
#                     cand = f"{split}[{self.encode_from_to(start,start+cnt_per_split-1)}]"
#                     #print(cand)
#                     if len(cand) < len(shortest_encoded):
#                         #print("HERE")
#                         shortest_encoded = cand
#                         break
#         else:
#             for split in range(start+1,end+1):
#                 cand = f"{self.encode_from_to(start,split-1)}{self.encode_from_to(split,end)}"
#                 if cand < shortest_encoded:
#                     shortest_encoded = cand
#         return shortest_encoded
