# A Range Module is a module that tracks ranges of numbers. Design a data structure to track the ranges represented as half-open intervals and query about them.

# A half-open interval [left, right) denotes all the real numbers x where left <= x < right.

# Implement the RangeModule class:

# RangeModule() Initializes the object of the data structure.
# void addRange(int left, int right) Adds the half-open interval [left, right), tracking every real number in that interval. Adding an interval that partially overlaps with currently tracked numbers should add any numbers in the interval [left, right) that are not already tracked.
# boolean queryRange(int left, int right) Returns true if every real number in the interval [left, right) is currently being tracked, and false otherwise.
# void removeRange(int left, int right) Stops tracking every real number currently being tracked in the half-open interval [left, right).
 

# Example 1:

# Input
# ["RangeModule", "addRange", "removeRange", "queryRange", "queryRange", "queryRange"]
# [[], [10, 20], [14, 16], [10, 14], [13, 15], [16, 17]]
# Output
# [null, null, null, true, false, true]

# Explanation
# RangeModule rangeModule = new RangeModule();
# rangeModule.addRange(10, 20);
# rangeModule.removeRange(14, 16);
# rangeModule.queryRange(10, 14); // return True,(Every number in [10, 14) is being tracked)
# rangeModule.queryRange(13, 15); // return False,(Numbers like 14, 14.03, 14.17 in [13, 15) are not being tracked)
# rangeModule.queryRange(16, 17); // return True, (The number 16 in [16, 17) is still being tracked, despite the remove operation)
 

# Constraints:

# 1 <= left < right <= 109
# At most 104 calls will be made to addRange, queryRange, and removeRange.
from sortedcontainers import SortedList

class RangeModule:

    def __init__(self):
        self.sl = SortedList()

    def addRange(self, left: int, right: int) -> None:
        insert_ind = self.sl.bisect_right([left,right])
        new_int = [left,right]
        removed = []
        if insert_ind > 0:
            left_int = self.sl[insert_ind-1]
            if left <= left_int[1]:
                new_int = [min(left,left_int[0]),max(right,left_int[1])]
                removed.append(left_int)
        while insert_ind < len(self.sl):
            right_int = self.sl[insert_ind]
            if new_int[1]>=right_int[0]:
                new_int = [min(new_int[0],right_int[0]),max(new_int[1],right_int[1])]
                removed.append(right_int)
                insert_ind += 1
            else:
                break
        for r in removed:
            self.sl.discard(r)
        self.sl.add(new_int)
        
    def queryRange(self, left: int, right: int) -> bool:
        insert_ind = self.sl.bisect_right([left,right])
        if insert_ind > 0:
            left_int = self.sl[insert_ind-1]
            if left >= left_int[0] and right<=left_int[1]:
                return True
        if insert_ind < len(self.sl):
            right_int = self.sl[insert_ind]
            if left >= right_int[0] and right<=right_int[1]:
                return True
        return False       

    def removeRange(self, left: int, right: int) -> None:
        insert_ind = self.sl.bisect_right([left,right])
        new_int = []
        removed = []
        if insert_ind > 0:
            left_int = self.sl[insert_ind-1]
            if left < left_int[1]:
                removed.append(left_int)
                if left>left_int[0]:
                    new_int.append([left_int[0],left])
            if right < left_int[1]:
                new_int.append([right,left_int[1]])
        while insert_ind < len(self.sl):
            right_int = self.sl[insert_ind]
            if right > right_int[0] and right<right_int[1]:
                new_int.append([right,right_int[1]])
                removed.append(right_int)
                break
            elif right>=right_int[1]:
                removed.append(right_int)
            else:
                break
            insert_ind += 1
        for r in removed:
            self.sl.discard(r)
        self.sl.update(new_int)       


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)