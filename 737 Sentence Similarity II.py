# We can represent a sentence as an array of words, for example, the sentence "I am happy with leetcode" can be represented as arr = ["I","am",happy","with","leetcode"].

# Given two sentences sentence1 and sentence2 each represented as a string array and given an array of string pairs similarPairs where similarPairs[i] = [xi, yi] indicates that the two words xi and yi are similar.

# Return true if sentence1 and sentence2 are similar, or false if they are not similar.

# Two sentences are similar if:

# They have the same length (i.e., the same number of words)
# sentence1[i] and sentence2[i] are similar.
# Notice that a word is always similar to itself, also notice that the similarity relation is transitive. For example, if the words a and b are similar, and the words b and c are similar, then a and c are similar.

 

# Example 1:

# Input: sentence1 = ["great","acting","skills"], sentence2 = ["fine","drama","talent"], similarPairs = [["great","good"],["fine","good"],["drama","acting"],["skills","talent"]]
# Output: true
# Explanation: The two sentences have the same length and each word i of sentence1 is also similar to the corresponding word in sentence2.
# Example 2:

# Input: sentence1 = ["I","love","leetcode"], sentence2 = ["I","love","onepiece"], similarPairs = [["manga","onepiece"],["platform","anime"],["leetcode","platform"],["anime","manga"]]
# Output: true
# Explanation: "leetcode" --> "platform" --> "anime" --> "manga" --> "onepiece".
# Since "leetcode is similar to "onepiece" and the first two words are the same, the two sentences are similar.
# Example 3:

# Input: sentence1 = ["I","love","leetcode"], sentence2 = ["I","love","onepiece"], similarPairs = [["manga","hunterXhunter"],["platform","anime"],["leetcode","platform"],["anime","manga"]]
# Output: false
# Explanation: "leetcode" is not similar to "onepiece".
 

# Constraints:

# 1 <= sentence1.length, sentence2.length <= 1000
# 1 <= sentence1[i].length, sentence2[i].length <= 20
# sentence1[i] and sentence2[i] consist of lower-case and upper-case English letters.
# 0 <= similarPairs.length <= 2000
# similarPairs[i].length == 2
# 1 <= xi.length, yi.length <= 20
# xi and yi consist of English letters.
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n

    def find_parent(self, p):
        if self.parent[p] == p:
            return p
        self.parent[p] = self.find_parent(self.parent[p])
        return self.parent[p]

    def union(self, n1, n2):
        p1 = self.find_parent(n1)
        p2 = self.find_parent(n2)
        if self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        elif self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        else:
            self.parent[p1] = p2
            self.rank[p2] += 1


class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        word_to_index = {}
        for w1, w2 in similarPairs:
            if w1 not in word_to_index:
                word_to_index[w1] = len(word_to_index)
            if w2 not in word_to_index:
                word_to_index[w2] = len(word_to_index)
        union_finder = UnionFind(len(word_to_index))
        for w1, w2 in similarPairs:
            ind1, ind2 = word_to_index[w1], word_to_index[w2]
            union_finder.union(ind1, ind2)
        #is_similar = True
        for w1, w2 in zip(sentence1, sentence2):
            if w1 != w2:
                ind1, ind2 = word_to_index.get(
                    w1, -1), word_to_index.get(w2, -1)
                if -1 in [ind1, ind2]:
                    return False
                p1, p2 = union_finder.find_parent(
                    ind1), union_finder.find_parent(ind2)
                if p1 != p2:
                    return False
        return True
