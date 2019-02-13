# In the "100 game," two players take turns adding, to a running total, any integer from 1..10. The player who first causes the running total to reach or exceed 100 wins.

# What if we change the game so that players cannot re-use integers?

# For example, two players might take turns drawing from a common pool of numbers of 1..15 without replacement until they reach a total >= 100.

# Given an integer maxChoosableInteger and another integer desiredTotal, determine if the first player to move can force a win, assuming both players play optimally.

# You can always assume that maxChoosableInteger will not be larger than 20 and desiredTotal will not be larger than 300.

# Example

# Input:
# maxChoosableInteger = 10
# desiredTotal = 11

# Output:
# false

# Explanation:
# No matter which integer the first player choose, the first player will lose.
# The first player can choose an integer from 1 up to 10.
# If the first player choose 1, the second player can only choose integers from 2 up to 10.
# The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
# Same with other integers chosen by the first player, the second player will always win.
class Solution:
    def canIWin(self, maxChoosableInteger: 'int', desiredTotal: 'int') -> 'bool':
        self.candidates = [1]*maxChoosableInteger
        candidate_state = 2**(maxChoosableInteger)-1
        self.cache = {}
        ans = self.helper(candidate_state,desiredTotal)
        return ans>=2
    def helper(self,can_state,target):## 2 肯定赢了， 1 0 代表输了，1是因为对手铁定赢了也就是2， 0输是代表当前自己没有办法达到目标
        if (can_state,target) in self.cache:
            return self.cache[(can_state,target)]
        oppo = -1
        for i in range(len(self.candidates)):
            if self.candidates[i]==1:
                if i+1>=target:
                    self.cache[(can_state, target)] = 2
                    return 2
                self.candidates[i]=0
                can_state &= ~(1<<i)
                oppo = self.helper(can_state,target-i-1)
                self.candidates[i] = 1
                can_state |= 1 << i
                if oppo==2:
                    continue
                if oppo==1:
                    self.cache[(can_state,target)]=2
                    return 2
                if oppo==0:
                    self.cache[(can_state,target)]=0
                    return 0
        if oppo==-1:
            self.cache[(can_state, target)] = 0
            return 0
        else:
            self.cache[(can_state,target)] = 1
            return 1
