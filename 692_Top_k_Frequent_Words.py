# Given a non-empty list of words, return the k most frequent elements.

# Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

# Example 1:
# Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
# Output: ["i", "love"]
# Explanation: "i" and "love" are the two most frequent words.
    # Note that "i" comes before "love" due to a lower alphabetical order.
# Example 2:
# Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
# Output: ["the", "is", "sunny", "day"]
# Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    # with the number of occurrence being 4, 3, 2 and 1 respectively.
# Note:
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Input words contain only lowercase letters.
# Follow up:
# Try to solve it in O(n log k) time and O(n) extra space.
# Accepted
# 48,379
# Submissions
# 108,767
def comp(cnt_word1,cnt_word2):
    cnt1,word1 = cnt_word1
    cnt2,word2 = cnt_word2
    if cnt1<cnt2:
        return -1
    elif cnt1>cnt2:
        return 1
    else:
        if word1<word2:
            return 1
        elif word1>word2:
            return -1
        else:
            return 0
from functools import cmp_to_key
comp_key = cmp_to_key(comp)
import heapq
class Solution:
    def topKFrequent(self, words: 'List[str]', k: 'int') -> 'List[str]':
        cnt ={}
        for word in words:
            cnt[word] = cnt.setdefault(word,0)+1
        cnt_word = [(comp_key((v,k)),(v,k)) for k,v in cnt.items()]
        heap = cnt_word[:k]
        heapq.heapify(heap)
        for i in range(k,len(cnt_word)):
            if cnt_word[i]>heap[0]:
                heapq.heapreplace(heap,cnt_word[i])
        return [ heapq.heappop(heap)[1][1] for i in range(k)][::-1]