# Design an Iterator class, which has:

# A constructor that takes a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
# A function next() that returns the next combination of length combinationLength in lexicographical order.
# A function hasNext() that returns True if and only if there exists a next combination.
 

# Example:

# CombinationIterator iterator = new CombinationIterator("abc", 2); // creates the iterator.

# iterator.next(); // returns "ab"
# iterator.hasNext(); // returns true
# iterator.next(); // returns "ac"
# iterator.hasNext(); // returns true
# iterator.next(); // returns "bc"
# iterator.hasNext(); // returns false
 

# Constraints:

# 1 <= combinationLength <= characters.length <= 15
# There will be at most 10^4 function calls per test.
# It's guaranteed that all calls of the function next are valid.
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.characters = characters
        self.combinationLength = combinationLength
        def coms(i,l):
            if l==1:
                return [self.characters[i]]
            
            ans = []
            for ii in range(i+1,len(self.characters)-(l-1)+1):
                ans.extend(coms(ii,l-1))
            return [self.characters[i]+a for a in ans]
        self.combs = []
        for i in range(len(characters)-combinationLength+1):
            self.combs.extend(coms(i,combinationLength))
        self.ind = 0
        #print(self.combs)
    def numbits(self,value):
        cnt = 0
        while value:
            value &= value-1
            cnt+=1
        return cnt
    
    def next(self) -> str:
        tmp = self.ind
        self.ind+=1
        return self.combs[tmp]

    def hasNext(self) -> bool:
        return self.ind<len(self.combs)

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()