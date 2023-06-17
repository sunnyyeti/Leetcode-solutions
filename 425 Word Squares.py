# Given an array of unique strings words, return all the word squares you can build from words. The same word from words can be used multiple times. You can return the answer in any order.

# A sequence of strings forms a valid word square if the kth row and column read the same string, where 0 <= k < max(numRows, numColumns).

# For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads the same both horizontally and vertically.
 

# Example 1:

# Input: words = ["area","lead","wall","lady","ball"]
# Output: [["ball","area","lead","lady"],["wall","area","lead","lady"]]
# Explanation:
# The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
# Example 2:

# Input: words = ["abat","baba","atan","atal"]
# Output: [["baba","abat","baba","atal"],["baba","abat","baba","atan"]]
# Explanation:
# The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
 

# Constraints:

# 1 <= words.length <= 1000
# 1 <= words[i].length <= 4
# All words[i] have the same length.
# words[i] consists of only lowercase English letters.
# All words[i] are unique.
class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        trie = {}
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char,{})
            node['#'] = True
        squares = []
        square = []
        def get_all_words(node):
            if '#' in node:
                yield ""
                return
            for key, next in node.items():
                for next_word in get_all_words(next):
                    yield key+next_word
        def helper():
            if len(square) == len(square[0]):
                squares.append(square[:])
                return
            cur_col = len(square)
            node = trie
            cur_word = []
            for r in range(len(square)):
                cur_word.append(square[r][cur_col])
                node = node.get(square[r][cur_col],{})
                if not node:
                    return 
            for word in get_all_words(node):
                cur_word.append(word)
                square.append(''.join(cur_word))
                helper()
                square.pop()
                cur_word.pop()
        for word in words:
            square.append(word)
            helper()
            square.pop()
        return squares
            
            
            
            