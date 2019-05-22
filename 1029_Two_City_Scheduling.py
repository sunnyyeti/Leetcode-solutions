# here are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].
#
# Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.
#
#
#
# Example 1:
#
# Input: [[10,20],[30,200],[400,50],[30,20]]
# Output: 110
# Explanation:
# The first person goes to city A for a cost of 10.
# The second person goes to city A for a cost of 30.
# The third person goes to city B for a cost of 50.
# The fourth person goes to city B for a cost of 20.
#
# The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        people_num = len(costs)
        A=[]
        B=[]
        for i in range(people_num):
            if costs[i][0]<=costs[i][1]:
                A.append((i,costs[i][0]))
            else:
                B.append((i,costs[i][1]))
        if len(A)==len(B):
            return sum(v for i,v in A)+sum(v for i,v in B)
        elif len(A)>len(B):
            transfer = (len(A)-len(B))//2
            dif = [costs[i][1]-v for i,v in A]
            dif.sort()
            return sum(v for i,v in A)+sum(v for i,v in B)+sum(dif[:transfer])
        else:
            transfer = -(len(A)-len(B))//2
            dif = [costs[i][0]-v for i,v in B]
            dif.sort()
            return sum(v for i,v in A)+sum(v for i,v in B)+sum(dif[:transfer])