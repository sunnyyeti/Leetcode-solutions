# Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list.
# Example 1:
# Input: ["23:59","00:00"]
# Output: 1
# Note:
# The number of time points in the given list is at least 2 and won't exceed 20000.
# The input time is legal and ranges from 00:00 to 23:59.
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def toms(time):
            h,m = time.split(":")
            return int(h)*60+int(m)
        timePoints = list(map(toms,timePoints))
        timePoints.sort()
        mind = float("inf")
        for i in range(len(timePoints)-1,-1,-1):
            if i:
                mind = min(mind,abs(timePoints[i]-timePoints[i-1]))
            else:
                mind = min(mind,timePoints[0]+1440-timePoints[-1])
        return mind