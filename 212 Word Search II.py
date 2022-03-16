# Given an m x n board of characters and a list of strings words, return all words on the board.

# Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

# Example 1:


# Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]
# Example 2:


# Input: board = [["a","b"],["c","d"]], words = ["abcb"]
# Output: []
 

# Constraints:

# m == board.length
# n == board[i].length
# 1 <= m, n <= 12
# board[i][j] is a lowercase English letter.
# 1 <= words.length <= 3 * 104
# 1 <= words[i].length <= 10
# words[i] consists of lowercase English letters.
# All the strings of words are unique.
# Accepted
# 305,238
# Submissions
# 809,765
class Node:
    def __init__(self,word,is_end):
        self.word = word
        self.is_end = is_end
        self.children = {}


class Trie:
    def __init__(self):
        self.root = Node('',False)
        
    def add_word(self,word):
        node = self.root
        for i,char in enumerate(word):
            if char not in node.children:
                tmp = Node(node.word+char,False)
                node.children[char] = tmp
            node = node.children[char]
        node.is_end = True
    


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for w in words:
            trie.add_word(w)
        node = trie.root
        ans = set()
        visited = set()
        def get_next_rc(r,c):
            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr,nc = r+dr,c+dc
                if 0<=nr<len(board) and 0<=nc<len(board[0]) and (nr,nc) not in visited:
                    yield nr,nc
        def dfs(r,c,node):
            visited.add((r,c))
            if node.is_end:
                ans.add(node.word)
            for nr,nc in get_next_rc(r,c):
                if board[nr][nc] in node.children:
                    dfs(nr,nc,node.children[board[nr][nc]])
            visited.remove((r,c))
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in node.children:
                    dfs(i,j,node.children[board[i][j]])
        return list(ans)