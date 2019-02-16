# Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

 



 
# Example:

# Input: ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska", "Dad"]
class Solution:
    def findWords(self, words: 'List[str]') -> 'List[str]':
        pos = {"q":0,"w":0,"e":0,"r":0,"t":0,"y":0,"u":0,"i":0,"o":0,"p":0,"a":1,"s":1,"d":1,"f":1,"g":1,"h":1,"j":1,"k":1,"l":1,"z":2,"x":2,"c":2,"v":2,"b":2,"n":2,"m":2}
        return [word for word in words if self.samerow(pos,word)]
        
        
    def samerow(self,pos,word):
        ini = pos[word[0].lower()]
        for i in range(1,len(word)):
            if pos[word[i].lower()]!=ini:
                return False
        return True
            