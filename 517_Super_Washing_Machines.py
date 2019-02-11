# ou have n super washing machines on a line. Initially, each washing machine has some dresses or is empty.

# For each move, you could choose any m (1 ≤ m ≤ n) washing machines, and pass one dress of each washing machine to one of its adjacent washing machines at the same time .

# Given an integer array representing the number of dresses in each washing machine from left to right on the line, you should find the minimum number of moves to make all the washing machines have the same number of dresses. If it is not possible to do it, return -1.

# Example1

# Input: [1,0,5]

# Output: 3

# Explanation: 
# 1st move:    1     0 <-- 5    =>    1     1     4
# 2nd move:    1 <-- 1 <-- 4    =>    2     1     3    
# 3rd move:    2     1 <-- 3    =>    2     2     2   
# Example2

# Input: [0,3,0]

# Output: 2

# Explanation: 
# 1st move:    0 <-- 3     0    =>    1     2     0    
# 2nd move:    1     2 --> 0    =>    1     1     1     
# Example3

# Input: [0,2,0]

# Output: -1

# Explanation: 
# It's impossible to make all the three washing machines have the same number of dresses. 
class Solution(object):
    def findMinMoves(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        """
        sum_ = sum(machines)
        if sum_%(len(machines))!=0:
            return -1
        tar = sum_//len(machines)
        acc_sums = [0]*(len(machines)+1)
        for i in range(1,len(machines)+1):
            acc_sums[i] = acc_sums[i-1]+machines[i-1]
        #print(acc_sums)
        #import sys
        min_move = -1
        for i in range(len(machines)):
            lcnt = acc_sums[i]-(tar*i)
            rcnt = acc_sums[-1]-acc_sums[i+1]-tar*(len(machines)-i-1)
            #print(lcnt,rcnt)
            if lcnt>0 and rcnt>0:
                min_move = max(min_move,max(lcnt,rcnt))
            elif lcnt<0 and rcnt<0:
                min_move = max(min_move,-lcnt-rcnt)
            else:
                min_move = max(min_move,max(abs(lcnt),abs(rcnt)))
        return min_move
        
        