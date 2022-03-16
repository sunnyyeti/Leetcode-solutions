# Given a list of strings dict where all the strings are of the same length.

# Return true if there are 2 strings that only differ by 1 character in the same index, otherwise return false.

 

# Example 1:

# Input: dict = ["abcd","acbd", "aacd"]
# Output: true
# Explanation: Strings "abcd" and "aacd" differ only by one character in the index 1.
# Example 2:

# Input: dict = ["ab","cd","yz"]
# Output: false
# Example 3:

# Input: dict = ["abcd","cccc","abyd","abab"]
# Output: true
 

# Constraints:

# The number of characters in dict <= 105
# dict[i].length == dict[j].length
# dict[i] should be unique.
# dict[i] contains only lowercase English letters.
 

# Follow up: Could you solve this problem in O(n * m) where n is the length of dict and m is the length of each string.
class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        seen = set()
        for word in dict:
            for i in range(len(word)):
                cand = word[:i]+'*'+word[i+1:]
                if cand in seen:
                    return True
                seen.add(cand)
        return False