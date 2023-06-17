# <!-- Given an integer array queries and a positive integer intLength, return an array answer where answer[i] is either the queries[i]th smallest positive palindrome of length intLength or -1 if no such palindrome exists.

# A palindrome is a number that reads the same backwards and forwards. Palindromes cannot have leading zeros.

 

# Example 1:

# Input: queries = [1,2,3,4,5,90], intLength = 3
# Output: [101,111,121,131,141,999]
# Explanation:
# The first few palindromes of length 3 are:
# 101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 202, ...
# The 90th palindrome of length 3 is 999.
# Example 2:

# Input: queries = [2,4,6], intLength = 4
# Output: [1111,1331,1551]
# Explanation:
# The first six palindromes of length 4 are:
# 1001, 1111, 1221, 1331, 1441, and 1551.
 

# Constraints:

# 1 <= queries.length <= 5 * 104
# 1 <= queries[i] <= 109
# 1 <= intLength <= 15 -->
class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        half = (intLength+1)//2
        total_cnt = 10**(half)-10**(half-1)
        ans = []
        for query in queries:
            if query > total_cnt:
                ans.append(-1)
            else:
                query -= 1
                cur = [0]*half
                for i in range(half):
                    #query -= 1
                    length = half-i-1
                    seg_size = 10**length
                    seg,query_n = divmod(query,seg_size)
                    #print(query,seg_size,seg,query_n)
                    if i==0:
                        seg += 1
                    cur[i] = seg
                    query = query_n
                #print(cur)
                if intLength%2==1:
                    cur = cur + cur[-2::-1]
                else:
                    cur = cur + cur[::-1]
                ans.append(int(''.join(map(str,cur))))
        return ans
                    
                
                
        