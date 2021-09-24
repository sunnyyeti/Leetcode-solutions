# Alice and Bob continue their games with piles of stones. There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array stoneValue.

# Alice and Bob take turns, with Alice starting first. On each player's turn, that player can take 1, 2 or 3 stones from the first remaining stones in the row.

# The score of each player is the sum of values of the stones taken. The score of each player is 0 initially.

# The objective of the game is to end with the highest score, and the winner is the player with the highest score and there could be a tie. The game continues until all the stones have been taken.

# Assume Alice and Bob play optimally.

# Return "Alice" if Alice will win, "Bob" if Bob will win or "Tie" if they end the game with the same score.

 

# Example 1:

# Input: values = [1,2,3,7]
# Output: "Bob"
# Explanation: Alice will always lose. Her best move will be to take three piles and the score become 6. Now the score of Bob is 7 and Bob wins.
# Example 2:

# Input: values = [1,2,3,-9]
# Output: "Alice"
# Explanation: Alice must choose all the three piles at the first move to win and leave Bob with negative score.
# If Alice chooses one pile her score will be 1 and the next move Bob's score becomes 5. The next move Alice will take the pile with value = -9 and lose.
# If Alice chooses two piles her score will be 3 and the next move Bob's score becomes 3. The next move Alice will take the pile with value = -9 and also lose.
# Remember that both play optimally so here Alice will choose the scenario that makes her win.
# Example 3:

# Input: values = [1,2,3,6]
# Output: "Tie"
# Explanation: Alice cannot win this game. She can end the game in a draw if she decided to choose all the first three piles, otherwise she will lose.
# Example 4:

# Input: values = [1,2,3,-1,-2,-3,7]
# Output: "Alice"
# Example 5:

# Input: values = [-1,-2,-3]
# Output: "Tie"
 

# Constraints:

# 1 <= values.length <= 50000
# -1000 <= values[i] <= 1000
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        def res(dp):
            return 'Alice' if dp[0]>dp[1] else 'Tie' if dp[0]==dp[1] else 'Bob'
        dp1,dp2,dp3 = [],[],[stoneValue[-1],0]
        if len(stoneValue) == 1:
            return res(dp3)
        dp2_cand1 = [stoneValue[-2],stoneValue[-1]]
        dp2_cand2 = [stoneValue[-2]+stoneValue[-1],0]
        if dp2_cand1[0] >= dp2_cand2[0]:
            dp2 = dp2_cand1
        else:
            dp2 = dp2_cand2
        if len(stoneValue)==2:
            return res(dp2)
        dp1 = [stoneValue[-3]+stoneValue[-2]+stoneValue[-1],0]
        dp1_cand = [stoneValue[-3]+stoneValue[-2]+dp3[1],dp3[0]]
        if dp1_cand[0] > dp1[0]:
            dp1 = dp1_cand
        dp1_cand = [stoneValue[-3]+dp2[1],dp2[0]]
        if dp1_cand[0] > dp1[0]:
            dp1 = dp1_cand
        if len(stoneValue)==3:
            return res(dp1)
        for i in reversed(range(len(stoneValue)-3)):
            dps = [dp1,dp2,dp3]
            sum_ = 0
            new_dp = [float('-inf'),0]
            for j in range(i,i+3):
                sum_ += stoneValue[j]
                next_dp = dps[j-i]
                tmp = [sum_+next_dp[1],next_dp[0]]
                if tmp[0]>new_dp[0]:
                    new_dp = tmp
            dp1,dp2,dp3 = new_dp,dp1,dp2
        return res(dp1)
                
        
        
        