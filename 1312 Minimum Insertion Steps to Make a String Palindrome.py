# Given a string s. In one step you can insert any character at any index of the string.

# Return the minimum number of steps to make s palindrome.

# A Palindrome String is one that reads the same backward as well as forward.

 

# Example 1:

# Input: s = "zzazz"
# Output: 0
# Explanation: The string "zzazz" is already palindrome we don't need any insertions.
# Example 2:

# Input: s = "mbadm"
# Output: 2
# Explanation: String can be "mbdadbm" or "mdbabdm".
# Example 3:

# Input: s = "leetcode"
# Output: 5
# Explanation: Inserting 5 characters the string becomes "leetcodocteel".
# Example 4:

# Input: s = "g"
# Output: 0
# Example 5:

# Input: s = "no"
# Output: 1
 

# Constraints:

# 1 <= s.length <= 500
# All characters of s are lower case English letters.
# Accepted
# 5,705
# Submissions
# 10,365
class Solution:
    def minInsertions(self, s: str) -> int:
        cache = {}
        def help(i,j):
            if (i,j) in cache:
                return cache[(i,j)]
            if i>=j:
                return 0
            if s[i]==s[j]:
                ans = help(i+1,j-1)
            else:
                ans = 1+min(help(i+1,j),help(i,j-1))
            cache[(i,j)] = ans
            return ans
        
        return help(0,len(s)-1)
            
                
            
                