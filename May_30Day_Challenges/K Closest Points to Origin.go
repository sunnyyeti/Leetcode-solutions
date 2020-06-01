// We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

// (Here, the distance between two points on a plane is the Euclidean distance.)

// You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

 

// Example 1:

// Input: points = [[1,3],[-2,2]], K = 1
// Output: [[-2,2]]
// Explanation: 
// The distance between (1, 3) and the origin is sqrt(10).
// The distance between (-2, 2) and the origin is sqrt(8).
// Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
// We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
// Example 2:

// Input: points = [[3,3],[5,-1],[-2,4]], K = 2
// Output: [[3,3],[-2,4]]
// (The answer [[-2,4],[3,3]] would also be accepted.)
 

// Note:

// 1 <= K <= points.length <= 10000
// -10000 < points[i][0] < 10000
// -10000 < points[i][1] < 10000
import "container/heap"

type MaxIntHeap [][]int

func (h MaxIntHeap) Len() int {return len(h)}
func (h MaxIntHeap) Less(i,j int) bool {return h[i][0]*h[i][0]+h[i][1]*h[i][1]>h[j][0]*h[j][0]+h[j][1]*h[j][1]}
func (h MaxIntHeap) Swap(i, j int) {h[i],h[j]=h[j],h[i]}
func (h *MaxIntHeap) Push (x interface{}) {
    *h = append(*h,x.([]int))
}
func (h *MaxIntHeap) Pop() interface{} {
    old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func kClosest(points [][]int, k int) [][]int {
    if len(points)<=k {
        return points
    }
    hh := (MaxIntHeap(points[:k]))
    h := &hh
    heap.Init(h)
    for i:=k;i<len(points);i++{
        cp:=points[i]
        cmax:=(*h)[0]
        if cp[0]*cp[0]+cp[1]*cp[1]<cmax[0]*cmax[0]+cmax[1]*cmax[1]{
            heap.Pop(h)
            heap.Push(h,cp)
        }
    }
    return [][]int(*h)
    
}