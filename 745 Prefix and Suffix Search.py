# Design a special dictionary with some words that searchs the words in it by a prefix and a suffix.

# Implement the WordFilter class:

# WordFilter(string[] words) Initializes the object with the words in the dictionary.
# f(string prefix, string suffix) Returns the index of the word in the dictionary, which has the prefix prefix and the suffix suffix. If there is more than one valid index, return the largest of them. If there is no such word in the dictionary, return -1.
 

# Example 1:

# Input
# ["WordFilter", "f"]
# [[["apple"]], ["a", "e"]]
# Output
# [null, 0]

# Explanation
# WordFilter wordFilter = new WordFilter(["apple"]);
# wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix = "a" and suffix = 'e".
 

# Constraints:

# 1 <= words.length <= 15000
# 1 <= words[i].length <= 10
# 1 <= prefix.length, suffix.length <= 10
# words[i], prefix and suffix consist of lower-case English letters only.
# At most 15000 calls will be made to the function f.
class Node:
    def __init__(self,word):
        self.word = word
        self.children = {}
        self.inds = -1
    def add_ind(self,ind):
        if ind > self.inds:
            self.inds = ind
        
        
class Tree:
    def __init__(self):
        self.root = Node("")
    
    def add_word(self,word,ind):
        cur_node = self.root
        for c in word:
            if c not in cur_node.children:
                tmp_node = Node(c)
                cur_node.children[c] = tmp_node
                cur_node.add_ind(ind)
                cur_node = tmp_node
            else:
                cur_node.add_ind(ind)
                cur_node = cur_node.children[c]
        cur_node.add_ind(ind)

    def search(self,suffix,prefix):
        cur_node = self.root
        for s in suffix:
            if s not in cur_node.children:
                return -1
            else:
                cur_node = cur_node.children[s]
        if '#' not in cur_node.children:
            return -1
        else:
            cur_node = cur_node.children['#']
        for s in prefix:
            if s not in cur_node.children:
                return -1
            else:
                cur_node = cur_node.children[s]
        return cur_node.inds
    
            
class WordFilter:

    def __init__(self, words: List[str]):
        self.tree = Tree()
        for ind,w in enumerate(words):
            for i in range(len(w)-1,-1,-1):
                self.tree.add_word(f"{w[i:]}#{w}",ind)
                

    def f(self, prefix: str, suffix: str) -> int:
        return self.tree.search(suffix,prefix)


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)