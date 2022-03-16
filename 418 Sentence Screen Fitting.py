# Given a rows x cols screen and a sentence represented as a list of strings, return the number of times the given sentence can be fitted on the screen.

# The order of words in the sentence must remain unchanged, and a word cannot be split into two lines. A single space must separate two consecutive words in a line.


# Example 1:

# Input: sentence = ["hello", "world"], rows = 2, cols = 8
# Output: 1
# Explanation:
# hello---
# world---
# The character '-' signifies an empty space on the screen.
# Example 2:

# Input: sentence = ["a", "bcd", "e"], rows = 3, cols = 6
# Output: 2
# Explanation:
# a-bcd-
# e-a---
# bcd-e-
# The character '-' signifies an empty space on the screen.
# Example 3:

# Input: sentence = ["i", "had", "apple", "pie"], rows = 4, cols = 5
# Output: 1
# Explanation:
# i-had
# apple
# pie-i
# had--
# The character '-' signifies an empty space on the screen.


# Constraints:

# 1 <= sentence.length <= 100
# 1 <= sentence[i].length <= 10
# sentence[i] consists of lowercase English letters.
# 1 <= rows, cols <= 2 * 104
class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        rcols = sum(len(s)+1 for s in sentence)
        cur_r = 0
        ans = 0
        ind = 0
        mcols = cols+1
        while cur_r < rows:
            j = ind
            cur_r_length = len(sentence[j])+1
            if cur_r_length > mcols:
                return 0
            rounds = mcols//rcols
            remains = mcols % rcols
            ans += rounds
            while cur_r_length <= remains:
                j += 1
                j = j % len(sentence)
                cur_r_length += len(sentence[j])+1
            if j < ind:
                ans += 1
            ind = j
            cur_r += 1
        return ans
