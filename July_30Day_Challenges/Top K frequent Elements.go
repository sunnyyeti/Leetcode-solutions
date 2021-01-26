// Given a non-empty array of integers, return the k most frequent elements.

// Example 1:

// Input: nums = [1,1,1,2,2,3], k = 2
// Output: [1,2]
// Example 2:

// Input: nums = [1], k = 1
// Output: [1]
// Note:

// You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
// Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
// It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
// You can return the answer in any order.
import "container/heap"

type CNT struct {
    key, count int
}
type IntHeap []CNT

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i].count < h[j].count }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x interface{}) {
	// Push and Pop use pointer receivers because they modify the slice's length,
	// not just its contents.
	*h = append(*h, x.(CNT))
}

func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}
func topKFrequent(nums []int, k int) []int {
    counter := make(map[int]int)
    for _,ele := range nums{
        counter[ele] = counter[ele]+1
    }
    allcnts := []CNT{}
    for key,cnt := range counter {
        allcnts = append(allcnts,CNT{key,cnt})
    }
    firstk := IntHeap(allcnts[:k])
    heapk := &firstk
    heap.Init(heapk)
    for s:=k;s<len(allcnts);s++{
        elecnt := allcnts[s]
        if elecnt.count > (*heapk)[0].count{
            heap.Pop(heapk)
            heap.Push(heapk,elecnt)
        }
    }
    ans := make([]int,0)
    for _,ele := range *heapk{
        ans = append(ans,ele.key)
    }
    return ans
    
    
    
}
