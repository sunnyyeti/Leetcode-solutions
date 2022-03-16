# Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

# You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

 

# Example 1:

# Input: name = "alex", typed = "aaleex"
# Output: true
# Explanation: 'a' and 'e' in 'alex' were long pressed.
# Example 2:

# Input: name = "saeed", typed = "ssaaedd"
# Output: false
# Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.
# Example 3:

# Input: name = "leelee", typed = "lleeelee"
# Output: true
# Example 4:

# Input: name = "laiden", typed = "laiden"
# Output: true
# Explanation: It's not necessary to long press any character.
 

# Constraints:

# 1 <= name.length <= 1000
# 1 <= typed.length <= 1000
# name and typed contain only lowercase English letters.
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        def groups(string):
            prev = None
            prev_ind = None
            ans = []
            for i,c in enumerate(string):
                if c!=prev:
                    if prev_ind!=None:
                        ans.append((prev,i-prev_ind))
                    prev = c
                    prev_ind = i
            ans.append((prev,len(string)-prev_ind))
            return ans
        groups_name = groups(name)
        groups_typed = groups(typed)
        if len(groups_name)!=len(groups_typed):
            return False
        for gn, gt in zip(groups_name,groups_typed):
            if not (gn[0]==gt[0] and gn[1]<=gt[1]):
                return False
        return True