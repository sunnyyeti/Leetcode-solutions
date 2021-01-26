# A string s is called good if there are no two different characters in s that have the same frequency.

# Given a string s, return the minimum number of characters you need to delete to make s good.

# The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

 

# Example 1:

# Input: s = "aab"
# Output: 0
# Explanation: s is already good.
# Example 2:

# Input: s = "aaabbbcc"
# Output: 2
# Explanation: You can delete two 'b's resulting in the good string "aaabcc".
# Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".
# Example 3:

# Input: s = "ceabaacb"
# Output: 2
# Explanation: You can delete both 'c's resulting in the good string "eabaab".
# Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).
 

# Constraints:

# 1 <= s.length <= 105
# s contains only lowercase English letters.
# Accepted
# 4,668
# Submissions
# 9,267
class Solution:
    def minDeletions(self, s: str) -> int:
        cnt = {}
        for c in s:
            cnt[c] = cnt.get(c,0)+1
        fre = sorted(cnt.values(),reverse=True)
        #print(fre)
        slots = sorted(set(range(fre[0],0,-1))-set(fre),reverse=True)
        slots.append(0)
        #print(slots)
        occurred = set()
        i = 0
        ans = 0
        for f in fre:
            if f not in occurred:
                occurred.add(f)
            else:
                while slots[i] >= f:
                    i+=1
                ans += f-slots[i]
                occurred.add(slots[i])
                i+=1
                i = min(i,len(slots)-1)

        return ans
                
            
        