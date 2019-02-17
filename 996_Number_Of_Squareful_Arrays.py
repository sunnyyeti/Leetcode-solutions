# Given an array A of non-negative integers, the array is squareful if for every pair of adjacent elements, their sum is a perfect square.

# Return the number of permutations of A that are squareful.  Two permutations A1 and A2 differ if and only if there is some index i such that A1[i] != A2[i].

 

# Example 1:

# Input: [1,17,8]
# Output: 2
# Explanation: 
# [1,8,17] and [17,8,1] are the valid permutations.
# Example 2:

# Input: [2,2,2]
# Output: 1
import math
class Solution:
    def numSquarefulPerms(self, A: 'List[int]') -> 'int':
        self.nb = {}
        for i in range(len(A)):
            for j in range(i+1,len(A)):
                if self.isquare(A[i]+A[j]):
                    self.nb.setdefault(i,[]).append(j)
                    self.nb.setdefault(j,[]).append(i)
        if len(self.nb)!=len(A):
            return 0
        self.ans = 0
        self.per = []
        self.A = A
        self.visited = set()
        self.visited_values = set()
        for i in self.nb.keys():
            if self.A[i] not in self.visited_values:
                self.visited_values.add(A[i])
                self.visited.add(i)
                self.permutation(i)
                self.visited.remove(i)
                self.per.pop()
        return self.ans

    def permutation(self,i):
        self.per.append(self.A[i])
        if len(self.per)==len(self.A):
            self.ans+=1
            return
        candiates = self.nb[i]
        visited_values = set()
        for can in candiates:
            if can not in self.visited and self.A[can] not in visited_values:
                visited_values.add(self.A[can])
                self.visited.add(can)
                self.permutation(can)
                self.visited.remove(can)
                self.per.pop()

    def isquare(self,num):
        if int(math.sqrt(num))==math.sqrt(num):
            return True
        return False