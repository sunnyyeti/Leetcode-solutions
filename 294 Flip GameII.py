# You are playing a Flip Game with your friend.

# You are given a string currentState that contains only '+' and '-'. You and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move, and therefore the other person will be the winner.

# Return true if the starting player can guarantee a win, and false otherwise.

 

# Example 1:

# Input: currentState = "++++"
# Output: true
# Explanation: The starting player can guarantee a win by flipping the middle "++" to become "+--+".
# Example 2:

# Input: currentState = "+"
# Output: false
 

# Constraints:

# 1 <= currentState.length <= 60
# currentState[i] is either '+' or '-'.
from functools import cache
class Solution:
    @cache
    def canWin(self, currentState: str) -> bool:
        for i in range(len(currentState)-1):
            if currentState[i:i+2] == '++':
                new_state = currentState[:i]+'--'+currentState[i+2:]
                if not self.canWin(new_state):
                    return True
        return False