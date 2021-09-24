# You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

# For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
# You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.

# Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.

 

# Example 1:

# Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
# Output: 2
# Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
# Example 2:

# Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
# Output: -1
 

# Constraints:

# 1 <= routes.length <= 500.
# 1 <= routes[i].length <= 105
# All the values of routes[i] are unique.
# sum(routes[i].length) <= 105
# 0 <= routes[i][j] < 106
# 0 <= source, target < 106
from collections import deque
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        graph = {}
        stop2bus = {}
        routes = [set(r) for r in routes]
        for bus,route in enumerate(routes):
            for stop in route:
                stop2bus.setdefault(stop,[]).append(bus)
            for nextbus in range(bus+1,len(routes)):
                next_route = routes[nextbus]
                if route & next_route:
                    graph.setdefault(bus,[]).append(nextbus)
                    graph.setdefault(nextbus,[]).append(bus)
        if source not in stop2bus or target not in stop2bus:
            return -1
        queue = deque(((bus,1) for bus in stop2bus[source]))
        seen = set(stop2bus[source])
        targets = set(stop2bus[target])
        while queue:
            cur_bus, dis = queue.popleft()
            if cur_bus in targets:
                return dis
            for next_bus in graph.get(cur_bus,[]):
                if next_bus not in seen:
                    seen.add(next_bus)
                    queue.append((next_bus,dis+1))
        return -1