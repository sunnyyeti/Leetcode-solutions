# You are given the number of rows n_rows and number of columns n_cols of a 2D binary matrix where all values are initially 0. Write a function flip which chooses a 0 value uniformly at random, changes it to 1, and then returns the position [row.id, col.id] of that value. Also, write a function reset which sets all values back to 0. Try to minimize the number of calls to system's Math.random() and optimize the time and space complexity.

# Note:

# 1 <= n_rows, n_cols <= 10000
# 0 <= row.id < n_rows and 0 <= col.id < n_cols
# flip will not be called when the matrix has no 0 values left.
# the total number of calls to flip and reset will not exceed 1000.
# Example 1:

# Input: 
# ["Solution","flip","flip","flip","flip"]
# [[2,3],[],[],[],[]]
# Output: [null,[0,1],[1,2],[1,0],[1,1]]
# Example 2:

# Input: 
# ["Solution","flip","flip","reset","flip"]
# [[1,2],[],[],[],[]]
# Output: [null,[0,0],[0,1],null,[0,0]]
# Explanation of Input Syntax:

# The input is two lists: the subroutines called and their arguments. Solution's constructor has two arguments, n_rows and n_cols. flip and reset have no arguments. Arguments are always wrapped with a list, even if there aren't any.
import random


class Solution:

    def __init__(self, n_rows: 'int', n_cols: 'int'):
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.all = n_cols * n_rows
        self.ones = []

    def flip(self) -> 'List[int]':
        pos = random.randint(0, self.all - 1 - len(self.ones))
        insert_ind = self.get_lower_bound(pos,0,len(self.ones)-1)
        #copy_insert = insert_ind
        #copy_pos = pos
        diff = insert_ind
        while diff!=0:
            pos = pos+diff
            new_insert = self.get_lower_bound(pos,insert_ind,len(self.ones)-1)
            diff = new_insert-insert_ind
            insert_ind = new_insert
        self.ones.insert(insert_ind,pos)
        return divmod(pos, self.n_cols)

    def get_lower_bound(self, tar, begin, end):
        while begin <= end:
            mid = (begin + end) // 2
            if self.ones[mid] > tar:
                end = mid - 1
            else:
                begin = mid + 1
        return begin

    def reset(self) -> 'None':
        self.ones = []