# In an exam room, there are N seats in a single row, numbered 0, 1, 2, ..., N-1.

# When a student enters the room, they must sit in the seat that maximizes the distance to the closest person.  If there are multiple such seats, they sit in the seat with the lowest number.  (Also, if no one is in the room, then the student sits at seat number 0.)

# Return a class ExamRoom(int N) that exposes two functions: ExamRoom.seat() returning an int representing what seat the student sat in, and ExamRoom.leave(int p) representing that the student in seat number p now leaves the room.  It is guaranteed that any calls to ExamRoom.leave(p) have a student sitting in seat p.

 

# Example 1:

# Input: ["ExamRoom","seat","seat","seat","seat","leave","seat"], [[10],[],[],[],[],[4],[]]
# Output: [null,0,9,4,2,null,5]
# Explanation:
# ExamRoom(10) -> null
# seat() -> 0, no one is in the room, then the student sits at seat number 0.
# seat() -> 9, the student sits at the last seat number 9.
# seat() -> 4, the student sits at the last seat number 4.
# seat() -> 2, the student sits at the last seat number 2.
# leave(4) -> null
# seat() -> 5, the student sits at the last seat number 5.
# ​​​​​​​

# Note:

# 1 <= N <= 10^9
# ExamRoom.seat() and ExamRoom.leave() will be called at most 10^4 times across all test cases.
# Calls to ExamRoom.leave(p) are guaranteed to have a student currently sitting in seat number p.

class Interval:
    def __init__(self,begin,end,MAX):
        self.begin = begin
        self.end = end
        self.MAX = MAX

    @property
    def closest(self):
        if self.begin==float("-inf"):
            return self.end
        if self.end == float("inf"):
            return self.MAX - 1 - self.begin
        return (self.end+self.begin)//2-self.begin
    @property
    def seat(self):
        if self.begin==float("-inf"):
            return 0
        if self.end == float("inf"):
            return self.MAX-1
        return (self.end+self.begin)//2

def interval_cmp(int1,int2):
    if int1.closest>int2.closest:
        return 1
    elif int1.closest<int2.closest:
        return -1
    elif int1.seat<int2.seat:
        return 1
    else:
        return -1

class Maxheap:
    def __init__(self,arr,cmp):
        self.arr = arr
        self.cmp = cmp
        self.size = len(arr)
        self.pos = {}
        for i,int in enumerate(arr):
            self.pos[int] = i
        self.build_heap()

    def max_heapify(self,ind):
        left = (ind<<1)+1
        largest = ind
        if left<self.size and self.cmp(self.arr[left],self.arr[ind])>0:
                largest = left
        right = left+1
        if right<self.size and self.cmp(self.arr[right],self.arr[largest])>0:
            largest = right
        if largest!=ind:
            self.pos[self.arr[largest]] = ind
            self.pos[self.arr[ind]] = largest
            self.arr[largest],self.arr[ind] = self.arr[ind],self.arr[largest]
            self.max_heapify(largest)

    def build_heap(self):
        for i in range(len(self.arr)//2-1,-1,-1):
            self.max_heapify(i)


    def heap_maximum(self):
        return self.arr[0] if self.arr else None

    def heap_extract_max(self):
        if not self.arr:
            return None
        max_ = self.arr[0]
        self.arr[0] = self.arr[self.size-1]
        self.size-=1
        self.pos.pop(max_)
        if self.size>0:
            self.pos[self.arr[0]] = 0
            self.max_heapify(0)
        return max_

    def flow_up(self,ind):
        parent = (ind-1)//2
        while parent>=0 and self.cmp(self.arr[ind],self.arr[parent])>0:
            self.pos[self.arr[ind]]=parent
            self.pos[self.arr[parent]] = ind
            self.arr[ind],self.arr[parent] = self.arr[parent],self.arr[ind]
            ind=parent
            parent = (ind-1)//2

    def delete_ele_at_ind(self,ind):
        ele = self.arr[ind]
        self.pos.pop(ele)
        self.arr[ind] = self.arr[self.size-1]
        self.size-=1
        if self.size>0:
            self.pos[self.arr[ind]] = ind
            parent = (ind-1)//2
            if parent>-1 and self.cmp(self.arr[ind],self.arr[parent])>0:
                self.flow_up(ind)
            else:
                self.max_heapify(ind)
        return ele

    def delete_ele(self,ele):
        return self.delete_ele_at_ind(self.pos[ele])

    def append(self,ele):
        if self.size<len(self.arr):
            self.arr[self.size] = ele
        else:
            self.arr.append(ele)
        self.size+=1
        self.pos[ele] = self.size-1
        self.flow_up(self.size-1)


class ExamRoom:

    def __init__(self, N: 'int'):
        self.N = N
        self.seat_cnt = 0
        self.ini_finisehd = False
        cmp = interval_cmp
        ini_interval = Interval(0,N-1,N)
        self.ass = {}
        arr = [ini_interval]
        self.maxheap = Maxheap(arr,cmp)

    def seat(self) -> 'int':
        if not self.ini_finisehd and self.seat_cnt!=2:
            if self.seat_cnt==0:
                ans=0
            elif self.seat_cnt==1:
                ans= self.N-1
            self.seat_cnt+=1
            return ans
        else:
            self.ini_finisehd=True
            max_interval = self.maxheap.heap_extract_max()
            seat = max_interval.seat
            ass_intervals = []
            if max_interval.begin>=0:
                new_interval1 = Interval(max_interval.begin,seat,self.N)
                ass_intervals.append(new_interval1)
                if max_interval.begin in self.ass:
                    assints = self.ass[max_interval.begin]
                    assints.remove(max_interval)
                    assints.append(new_interval1)
                else:
                    self.ass.setdefault(max_interval.begin,[]).append(new_interval1)
            if max_interval.end<self.N:
                new_interval2 = Interval(seat,max_interval.end,self.N)
                ass_intervals.append(new_interval2)
                if max_interval.end in self.ass:
                    assints = self.ass[max_interval.end]
                    assints.remove(max_interval)
                    assints.append(new_interval2)
                else:
                    self.ass.setdefault(max_interval.end,[]).append(new_interval2)
            self.ass[seat] = ass_intervals
            for int in ass_intervals:
                self.maxheap.append(int)
            return seat

    def leave(self, p: 'int') -> 'None':
        if not self.ini_finisehd:
            self.seat_cnt-=1
            return
        #ass_intervals = self.ass[p]
        if p==0:
            ass_intervals = self.ass[p]
            self.maxheap.delete_ele(ass_intervals[0])
            new_int = Interval(float("-inf"),ass_intervals[0].end,self.N)
            self.maxheap.append(new_int)
            #self.ass[p] = [new_int]
            end_ints = self.ass[ass_intervals[0].end]
            end_ints.remove(ass_intervals[0])
            end_ints.append(new_int)

        elif p==self.N-1:
            ass_intervals = self.ass[p]
            self.maxheap.delete_ele(ass_intervals[0])
            new_int = Interval(ass_intervals[0].begin,float("inf"),self.N)
            self.maxheap.append(new_int)
            #self.ass[p] = [new_int]
            end_ints = self.ass[ass_intervals[0].begin]
            end_ints.remove(ass_intervals[0])
            end_ints.append(new_int)
        else:
            ass_intervals = self.ass[p]
            ai1 = ass_intervals[0]
            ai2 = ass_intervals[1]
            if ai1.end==p:
                new_begin = ai1.begin
                new_end = ai2.end
                if new_begin in self.ass:
                    self.ass[new_begin].remove(ai1)
                if new_end in self.ass:
                    self.ass[new_end].remove(ai2)
            else:
                new_end = ai1.end
                new_begin = ai2.begin
                if new_end in self.ass:
                    self.ass[new_end].remove(ai1)
                if new_begin in self.ass:
                    self.ass[new_begin].remove(ai2)
            new_interval = Interval(new_begin,new_end,self.N)
            self.maxheap.append(new_interval)
            self.maxheap.delete_ele(ai1)
            self.maxheap.delete_ele(ai2)
            self.ass.pop(p)
            if new_begin!=float("-inf"):
                self.ass[new_begin].append(new_interval)
            if new_end!=float("inf"):
                self.ass[new_end].append(new_interval)