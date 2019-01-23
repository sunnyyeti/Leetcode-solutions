# Given a wordlist, we want to implement a spellchecker that converts a query word into a correct word.

# For a given query word, the spell checker handles two categories of spelling mistakes:

# Capitalization: If the query matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the case in the wordlist.
# Example: wordlist = ["yellow"], query = "YellOw": correct = "yellow"
# Example: wordlist = ["Yellow"], query = "yellow": correct = "Yellow"
# Example: wordlist = ["yellow"], query = "yellow": correct = "yellow"
# Vowel Errors: If after replacing the vowels ('a', 'e', 'i', 'o', 'u') of the query word with any vowel individually, it matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the match in the wordlist.
# Example: wordlist = ["YellOw"], query = "yollow": correct = "YellOw"
# Example: wordlist = ["YellOw"], query = "yeellow": correct = "" (no match)
# Example: wordlist = ["YellOw"], query = "yllw": correct = "" (no match)
# In addition, the spell checker operates under the following precedence rules:

# When the query exactly matches a word in the wordlist (case-sensitive), you should return the same word back.
# When the query matches a word up to capitlization, you should return the first such match in the wordlist.
# When the query matches a word up to vowel errors, you should return the first such match in the wordlist.
# If the query has no matches in the wordlist, you should return the empty string.
# Given some queries, return a list of words answer, where answer[i] is the correct word for query = queries[i].

class Solution:
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        wordset = set(wordlist)
        pos_dict = {}
        devowl_pos_dict = {}
        for i,w in enumerate(wordlist):
            pos_dict[w.lower()] = min(pos_dict.setdefault(w.lower(),len(wordlist)),i)
            devowl = self.get_replaced_word(w.lower())
            devowl_pos_dict[devowl] = min(devowl_pos_dict.setdefault(devowl,len(wordlist)),i)
        res = []
        for q in queries:
            if q in wordset:
                res.append(q)
            elif q.lower() in pos_dict:
                res.append(wordlist[pos_dict[q.lower()]])
            elif self.get_replaced_word(q.lower()) in devowl_pos_dict:
                res.append(wordlist[devowl_pos_dict[self.get_replaced_word(q.lower())]])
            else:
                res.append("")
        return res
        
    
    def get_replaced_word(self,word):
        vowels = {"a","e","i","o","u"}
        return "".join("*" if c in vowels else c for c in word )