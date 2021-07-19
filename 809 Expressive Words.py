# Sometimes people repeat letters to represent extra feeling. For example:

# "hello" -> "heeellooo"
# "hi" -> "hiiii"
# In these strings like "heeellooo", we have groups of adjacent letters that are all the same: "h", "eee", "ll", "ooo".

# You are given a string s and an array of query strings words. A query word is stretchy if it can be made to be equal to s by any number of applications of the following extension operation: choose a group consisting of characters c, and add some number of characters c to the group so that the size of the group is three or more.

# For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get "helloo" since the group "oo" has a size less than three. Also, we could do another extension like "ll" -> "lllll" to get "helllllooo". If s = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = s.
# Return the number of query strings that are stretchy.

 

# Example 1:

# Input: s = "heeellooo", words = ["hello", "hi", "helo"]
# Output: 1
# Explanation: 
# We can extend "e" and "o" in the word "hello" to get "heeellooo".
# We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.
# Example 2:

# Input: s = "zzzzzyyyyy", words = ["zzyy","zy","zyy"]
# Output: 3
 

# Constraints:

# 1 <= s.length, words.length <= 100
# 1 <= words[i].length <= 100
# s and words[i] consist of lowercase letters.
class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def get_groups(word):
            groups = []
            i = 0
            while True:
                j = i
                while j<len(word) and word[j] == word[i]:
                    j+=1
                groups.append((word[i],j-i))
                i = j
                if i>=len(word):
                    break
            return groups
        def is_stretchy(group_s,group_w):
            if len(group_s)!=len(group_w):
                return False
            for g1,g2 in zip(group_s,group_w):
                if g1[0]!=g2[0]:
                    return False
                if g1[1] < g2[1]:
                    return False
                if g1[1]<3 and g1[1]>g2[1]:
                    return False
            return True
        group_s = get_groups(s)
        #print(group_s)
        ans = 0
        for w in words:
            group_w = get_groups(w)
            ans += is_stretchy(group_s,group_w)
        return ans