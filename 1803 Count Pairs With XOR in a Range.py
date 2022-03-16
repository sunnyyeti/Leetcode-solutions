# Given a (0-indexed) integer array nums and two integers low and high, return the number of nice pairs.

# A nice pair is a pair (i, j) where 0 <= i < j < nums.length and low <= (nums[i] XOR nums[j]) <= high.

 

# Example 1:

# Input: nums = [1,4,2,7], low = 2, high = 6
# Output: 6
# Explanation: All nice pairs (i, j) are as follows:
#     - (0, 1): nums[0] XOR nums[1] = 5 
#     - (0, 2): nums[0] XOR nums[2] = 3
#     - (0, 3): nums[0] XOR nums[3] = 6
#     - (1, 2): nums[1] XOR nums[2] = 6
#     - (1, 3): nums[1] XOR nums[3] = 3
#     - (2, 3): nums[2] XOR nums[3] = 5
# Example 2:

# Input: nums = [9,8,4,2,1], low = 5, high = 14
# Output: 8
# Explanation: All nice pairs (i, j) are as follows:
# ​​​​​    - (0, 2): nums[0] XOR nums[2] = 13
#     - (0, 3): nums[0] XOR nums[3] = 11
#     - (0, 4): nums[0] XOR nums[4] = 8
#     - (1, 2): nums[1] XOR nums[2] = 12
#     - (1, 3): nums[1] XOR nums[3] = 10
#     - (1, 4): nums[1] XOR nums[4] = 9
#     - (2, 3): nums[2] XOR nums[3] = 6
#     - (2, 4): nums[2] XOR nums[4] = 5
 

# Constraints:

# 1 <= nums.length <= 2 * 104
# 1 <= nums[i] <= 2 * 104
# 1 <= low <= high <= 2 * 104
class Node:
    def __init__(self,cnt=0):
        self.cnt = cnt
        self.c = [None,None]
        
class Tree:
    def __init__(self):
        self.root = Node(0)
    
    def add(self,num):
        cur_node = self.root
        for i in range(15,-1,-1):
            cur_node.cnt += 1
            bit = (num&(1<<i))>>i
            if cur_node.c[bit] is None:
                cur_node.c[bit] = Node(0)
            cur_node = cur_node.c[bit]
        cur_node.cnt += 1
        
    def less_than(self,pair,value,equal):
        ans = 0
        cur_node = self.root
        for i in range(15,-1,-1):
            p_bit = (pair&(1<<i))>>i
            v_bit = (value&(1<<i))>>i

            if p_bit ==0 and v_bit==0:
                cur_node = cur_node.c[0]
            elif p_bit==0 and v_bit==1:
                if cur_node.c[0]:
                    ans += cur_node.c[0].cnt
                cur_node = cur_node.c[1]
            elif p_bit==1 and v_bit==0:
                cur_node = cur_node.c[1]
            else:
                if cur_node.c[1]:
                    ans += cur_node.c[1].cnt
                cur_node = cur_node.c[0]
            if cur_node is None:
                break
        if equal and cur_node:
            ans += cur_node.cnt
        if equal and pair^pair <= value:
            ans -=1
        if not equal and pair^pair<value:
            ans-=1
        return ans
            
        

class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        t = Tree()
        for n in nums:
            t.add(n)
        high = sum(t.less_than(n,high,True) for n in nums)//2
        low = sum(t.less_than(n,low,False) for n in nums)//2
        return high-low