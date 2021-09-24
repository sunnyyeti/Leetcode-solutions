# You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

# All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

# For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

 

# Example 1:


# Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
# Output: ["JFK","MUC","LHR","SFO","SJC"]
# Example 2:


# Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.
 

# Constraints:

# 1 <= tickets.length <= 300
# tickets[i].length == 2
# fromi.length == 3
# toi.length == 3
# fromi and toi consist of uppercase English letters.
# fromi != toi
from collections import Counter


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = {}
        for s, t in tickets:
            graph.setdefault(s, []).append(t)
        for k, v in graph.items():
            graph[k] = Counter(v)

        def dfs(place, path):
            path.append(place)
            if len(path) == len(tickets)+1:
                return True
            next_place_counter = graph.get(place, Counter())
            next_places = sorted(next_place_counter.keys())
            for next_place in next_places:
                next_place_counter[next_place] -= 1
                if next_place_counter[next_place] == 0:
                    del next_place_counter[next_place]
                if dfs(next_place, path):
                    return True
                else:
                    next_place_counter[next_place] += 1
            path.pop()
            return False
        path = []
        dfs("JFK", path)
        return path
