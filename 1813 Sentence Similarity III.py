# A sentence is a list of words that are separated by a single space with no leading or trailing spaces. For example, "Hello World", "HELLO", "hello world hello world" are all sentences. Words consist of only uppercase and lowercase English letters.

# Two sentences sentence1 and sentence2 are similar if it is possible to insert an arbitrary sentence (possibly empty) inside one of these sentences such that the two sentences become equal. For example, sentence1 = "Hello my name is Jane" and sentence2 = "Hello Jane" can be made equal by inserting "my name is" between "Hello" and "Jane" in sentence2.

# Given two sentences sentence1 and sentence2, return true if sentence1 and sentence2 are similar. Otherwise, return false.

 

# Example 1:

# Input: sentence1 = "My name is Haley", sentence2 = "My Haley"
# Output: true
# Explanation: sentence2 can be turned to sentence1 by inserting "name is" between "My" and "Haley".
# Example 2:

# Input: sentence1 = "of", sentence2 = "A lot of words"
# Output: false
# Explanation: No single sentence can be inserted inside one of the sentences to make it equal to the other.
# Example 3:

# Input: sentence1 = "Eating right now", sentence2 = "Eating"
# Output: true
# Explanation: sentence2 can be turned to sentence1 by inserting "right now" at the end of the sentence.
# Example 4:

# Input: sentence1 = "Luky", sentence2 = "Lucccky"
# Output: false
 

# Constraints:

# 1 <= sentence1.length, sentence2.length <= 100
# sentence1 and sentence2 consist of lowercase and uppercase English letters and spaces.
# The words in sentence1 and sentence2 are separated by a single space.
from functools import cache
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        terms1 = sentence1.split()
        terms2 = sentence2.split()
        if len(terms1)<len(terms2):
            terms1,terms2 = terms2,terms1
            
        @cache
        def help(s1,e1,s2,e2):
            if s2>=e2:
                return True
            if e2-s2==1:
                return terms2[s2]==terms1[s1] or terms2[e2-1]==terms1[e1-1]
            if terms2[s2] == terms1[s1] and help(s1+1,e1,s2+1,e2):
                return True
            if terms2[e2-1]==terms1[e1-1] and help(s1,e1-1,s2,e2-1):
                return True
            if terms2[s2] == terms1[s1] and terms2[e2-1]==terms1[e1-1] and help(s1+1,e1-1,s2+1,e2-1):
                return True
            return False
        return help(0,len(terms1),0,len(terms2))    