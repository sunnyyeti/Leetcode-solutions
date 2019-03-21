# Given a data stream input of non-negative integers a1, a2, ..., an, ..., summarize the numbers seen so far as a list of disjoint intervals.

# For example, suppose the integers from the data stream are 1, 3, 7, 2, 6, ..., then the summary will be:

# [1, 1]
# [1, 1], [3, 3]
# [1, 1], [3, 3], [7, 7]
# [1, 3], [7, 7]
# [1, 3], [6, 7]
# Follow up:
# What if there are lots of merges and the number of disjoint intervals are small compared to the data stream's size?
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []
        

    def addNum(self, val: int) -> None:
        if not self.arr:
            self.arr.append(Interval(val,val))
        lb = self.bin_lower_bound(val)
        cur_int = self.arr[lb]
        if cur_int.start<=val<=cur_int.end:
            return
        if lb==len(self.arr)-1:
            if val==cur_int.end+1:
                cur_int.end +=1
            else:
                self.arr.append(Interval(val,val))
        else:
            next_int = self.arr[lb+1]
            if cur_int.end+1==val and next_int.start-1==val:
                self.arr.pop(lb)
                next_int.start = cur_int.start
            elif cur_int.end+1==val:
                cur_int.end+=1
            elif next_int.start-1==val:
                next_int.start-=1
            else:
                self.arr.insert(lb+1,Interval(val,val))
                
    def bin_lower_bound(self,val):
        begin = 0
        end = len(self.arr)-1
        while begin<=end:
            mid = (begin+end)//2
            cur_int = self.arr[mid]
            if cur_int.start>val:
                end=mid-1
            else:
                begin = mid+1
        return end

    def getIntervals(self) -> List[Interval]:
        return self.arr


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()