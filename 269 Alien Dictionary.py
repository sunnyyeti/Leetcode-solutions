# Share
# There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.

# You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted lexicographically by the rules of this new language.

# Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.

# A string s is lexicographically smaller than a string t if at the first letter where they differ, the letter in s comes before the letter in t in the alien language. If the first min(s.length, t.length) letters are the same, then s is smaller if and only if s.length < t.length.

 

# Example 1:

# Input: words = ["wrt","wrf","er","ett","rftt"]
# Output: "wertf"
# Example 2:

# Input: words = ["z","x"]
# Output: "zx"
# Example 3:

# Input: words = ["z","x","z"]
# Output: ""
# Explanation: The order is invalid, so return "".
 

# Constraints:

# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists of only lowercase English letters.
from collections import Counter
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        all_chrs = set(''.join(words))
        graph = {}
        incomes = Counter()
        for i in range(len(words)-1):
            cur_word = words[i]
            next_word = words[i+1]
            for j in range(min(len(cur_word),len(next_word))):
                if cur_word[j] != next_word[j]:
                    nexts = graph.setdefault(cur_word[j],set())
                    if next_word[j] not in nexts:
                        nexts.add(next_word[j])
                        incomes[next_word[j]] += 1 
                    break
            else:
                if len(cur_word) > len(next_word):
                    return ''
        #print(graph)
        #print(incomes)
        stack = []
        for k in all_chrs:
            if incomes[k] == 0:
                stack.append(k)
        ans = []
        while stack:
            #print("append",stack[-1])
            ans.append(stack.pop())
            for next_char in graph.get(ans[-1],set()):
                incomes[next_char]-=1
                if incomes[next_char] == 0:
                    stack.append(next_char)
                    del incomes[next_char]
                #print(incomes)
        #print(ans,incomes)
        return ''.join(ans) if len(incomes)==0 else ""