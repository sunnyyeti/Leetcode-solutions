# You are given a square board of characters. You can move on the board starting at the bottom right square marked with the character 'S'.

# You need to reach the top left square marked with the character 'E'. The rest of the squares are labeled either with a numeric character 1, 2, ..., 9 or with an obstacle 'X'. In one move you can go up, left or up-left (diagonally) only if there is no obstacle there.

# Return a list of two integers: the first integer is the maximum sum of numeric characters you can collect, and the second is the number of such paths that you can take to get that maximum sum, taken modulo 10^9 + 7.

# In case there is no path, return [0, 0].

 

# Example 1:

# Input: board = ["E23","2X2","12S"]
# Output: [7,1]
# Example 2:

# Input: board = ["E12","1X1","21S"]
# Output: [4,2]
# Example 3:

# Input: board = ["E11","XXX","11S"]
# Output: [0,0]
 

# Constraints:

# 2 <= board.length == board[i].length <= 100
class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        def v(char):
            if char=="E" or char=="S":
                return 0
            if char=="X":
                return float('-inf')
            return int(char)
        length = len(board)
        res1 = [(0,0) for _ in range(length)]
        res1[0] = (0,1)
        for j in range(1,length):
            val = v(board[0][j])
            res1[j] = val+res1[j-1][0],res1[j-1][1]
        res2 = res1[::]
        for row in range(1,length):
            for col in range(length):
                cur_char = board[row][col]
                cur_val = v(cur_char)
                if col==0:
                    _sum,_num = res1[0]
                    res2[0] = cur_val+_sum,_num
                else:
                    _sum_a,_num_a = res1[col]
                    _sum_l,_num_l = res2[col-1]
                    _sum_d,_num_d = res1[col-1]
                    _sums = [_sum_a,_sum_l,_sum_d]
                    _nums = [_num_a,_num_l,_num_d]
                    max_s = max(_sums)
                    inds = [i for i in range(3) if _sums[i]==max_s]
                    res2[col] = max_s+cur_val, sum(_nums[i] for i in inds)
            #print(res2)
            res1,res2 = res2,res1
        if res1[-1][0]==float("-inf"):
            return [0,0]
        return res1[-1][0],res1[-1][1]%(10**9+7)
        
                    
                    