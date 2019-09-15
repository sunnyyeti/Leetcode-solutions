class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        points = []
        for nums, start, stop in trips:
            points.append((start,nums))
            points.append((stop,-nums))
        points.sort()
        traveller = 0
        for pos, cnt in points:
            traveller+=cnt
            if traveller>capacity:
                return False
        return True

if __name__ =="__main__":
    assert not Solution().carPooling([[2,1,5],[3,3,7]],4) 
    assert Solution().carPooling([[2,1,5],[3,3,7]],5)
    assert Solution().carPooling([[2,1,5],[3,5,7]],5)