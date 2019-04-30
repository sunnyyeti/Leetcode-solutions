# Write a function that takes a string as input and reverse only the vowels of a string.

# Example 1:

# Input: "hello"
# Output: "holle"
# Example 2:

# Input: "leetcode"
# Output: "leotcede"
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        chars = list(s)
        i,j=0,len(chars)-1
        vowels = {"a","e","i","o","u","A","E","I","O","U"}
        while i<j:
            if chars[i] in vowels and chars[j] in vowels:
                chars[i],chars[j]=chars[j],chars[i]
                i+=1
                j-=1
            elif chars[i] in vowels:
                j-=1
            elif chars[j] in vowels:
                i+=1
            else:
                i+=1
                j-=1
        return "".join(chars)