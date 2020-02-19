# Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

# Example:
# Given a / b = 2.0, b / c = 3.0.
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
# return [6.0, 0.5, -1.0, 1.0, -1.0 ].

# The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

# According to the example above:

# equations = [ ["a", "b"], ["b", "c"] ],
# values = [2.0, 3.0],
# queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
 

# The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        self.d = {}
        for e,v in zip(equations,values):
            self.d.setdefault(e[0],{})[e[1]] = v
            self.d.setdefault(e[1],{})[e[0]] = 1/v
        #print(self.d)
        ans = []
        for s,e in queries:
            self.visited = set()
            ans.append(self.help(s,e))
            #print(ans)
        return ans
        
    def help(self,s,e):
        if s not in self.d:
            return -1.0
        nexts = self.d[s]
        if e in nexts:
            return nexts[e]
        self.visited.add(s)
        for k in nexts.keys():
            if k not in self.visited:
                tmp = self.help(k,e)
                if tmp!=-1.0:
                    return nexts[k]*tmp
        return -1.0
                