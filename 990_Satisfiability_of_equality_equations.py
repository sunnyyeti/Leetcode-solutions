# Given an array equations of strings that represent relationships between variables, each string equations[i] has length 4 and takes one of two different forms: "a==b" or "a!=b".  Here, a and b are lowercase letters (not necessarily different) that represent one-letter variable names.

# Return true if and only if it is possible to assign integers to variable names so as to satisfy all the given equations.

 

# Example 1:

# Input: ["a==b","b!=a"]
# Output: false
# Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.  There is no way to assign the variables to satisfy both equations.
# Example 2:

# Input: ["b==a","a==b"]
# Output: true
# Explanation: We could assign a = 1 and b = 1 to satisfy both equations.
# Example 3:

# Input: ["a==b","b==c","a==c"]
# Output: true
# Example 4:

# Input: ["a==b","b!=c","c==a"]
# Output: false
# Example 5:

# Input: ["c==c","b==d","x!=z"]
# Output: true
 

# Note:

# 1 <= equations.length <= 500
# equations[i].length == 4
# equations[i][0] and equations[i][3] are lowercase letters
# equations[i][1] is either '=' or '!'
# equations[i][2] is '='
class Solution:
    def equationsPossible(self, equations: 'List[str]') -> 'bool':
        not_equal = []
        self.nbs = {}
        for eq in equations:
            a,b,equal = self.parse_equation(eq)
            if equal:
                if a!=b:
                    self.nbs.setdefault(a,set()).add(b)
                    self.nbs.setdefault(b,set()).add(a)
            else:
                if a==b:
                    return False
                not_equal.append((a,b))
        for a,b in not_equal:
            visited = set()
            if self.exists_path_between(a,b,visited):
                return False
        return True
        
    def exists_path_between(self,a,b,visited):
        if a not in self.nbs or b not in self.nbs:
            return False
        if a==b:
            return True
        visited.add(a)
        nexts = self.nbs[a]
        for n in nexts:
            if n not in visited:
                visited.add(n)
                if self.exists_path_between(n,b,visited):
                    return True
                visited.remove(n)
        return False
        
    def parse_equation(self,equation):
        a = equation[0]
        b = equation[-1]
        return (a,b,"!" not in equation)