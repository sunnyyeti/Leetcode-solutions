# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

 

# Example 1:

# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2
# Example 2:

# Input: intervals = [[7,10],[2,4]]
# Output: 1
 

# Constraints:

# 1 <= intervals.length <= 104
# 0 <= starti < endi <= 106
from sortedcontainers import SortedList
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        sl = SortedList()
        ans = 0
        for itv in intervals:
            right = sl.bisect_right(itv[0])
            #print(itv,len(sl)-right+1)
            ans = max(ans,len(sl)-right+1)
            sl.add(itv[1])
        return ans