# 859. Buddy Strings
# Easy

# 382

# 241

# Favorite

# Share
# Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.

 

# Example 1:

# Input: A = "ab", B = "ba"
# Output: true
# Example 2:

# Input: A = "ab", B = "ab"
# Output: false
# Example 3:

# Input: A = "aa", B = "aa"
# Output: true
# Example 4:

# Input: A = "aaaaaaabc", B = "aaaaaaacb"
# Output: true
# Example 5:

# Input: A = "", B = "aa"
# Output: false
 

# Note:

# 0 <= A.length <= 20000
# 0 <= B.length <= 20000
# A and B consist only of lowercase letters.
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A)!=len(B):
            return False
        if  len(A) in (0,1):
            return False
        dif_inds=[i for i in range(len(A)) if A[i]!=B[i]]
        if len(dif_inds)!=2 and len(dif_inds):
            return False
        if len(dif_inds):
            if A[dif_inds[0]]==B[dif_inds[1]] and A[dif_inds[1]]==B[dif_inds[0]]:
                return True
            else:
                return False
        else:
            counter = {}
            for c in A:
                counter[c] = counter.get(c,0)+1
                if counter[c]>=2:
                    return True
            return False
        