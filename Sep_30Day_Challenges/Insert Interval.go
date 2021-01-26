// Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

// You may assume that the intervals were initially sorted according to their start times.

 

// Example 1:

// Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
// Output: [[1,5],[6,9]]
// Example 2:

// Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
// Output: [[1,2],[3,10],[12,16]]
// Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
// Example 3:

// Input: intervals = [], newInterval = [5,7]
// Output: [[5,7]]
// Example 4:

// Input: intervals = [[1,5]], newInterval = [2,3]
// Output: [[1,5]]
// Example 5:

// Input: intervals = [[1,5]], newInterval = [2,7]
// Output: [[1,7]]
 

// Constraints:

// 0 <= intervals.length <= 104
// intervals[i].length == 2
// 0 <= intervals[i][0] <= intervals[i][1] <= 105
// intervals is sorted by intervals[i][0] in ascending order.
// newInterval.length == 2
// 0 <= newInterval[0] <= newInterval[1] <= 105
func findInterval(intervals [][]int, target int) int{
    start, end := 0, len(intervals)-1
    for start<=end {
        mid := start + (end-start)/2
        interval := intervals[mid]
        if interval[0]<=target && target<=interval[1] {
            return mid
        }else if interval[0]>target{
            end = mid-1
        }else{
            start = mid+1
        }
    }
    return start
}

func insert(intervals [][]int, newInterval []int) [][]int {
    copyintervals := [][]int{}
    for _, inter := range intervals{
        copyintervals = append(copyintervals,inter)
    }
    sint := findInterval(intervals,newInterval[0])
    eint := findInterval(intervals,newInterval[1])
    if sint==len(intervals){
        res := intervals
        res = append(res,newInterval)
        return res
    }
    //fmt.Println(sint,eint)
    if intervals[sint][0]>newInterval[0] && (eint==len(intervals) || intervals[eint][0]>newInterval[1]){
        res := intervals[:sint]
        res = append(res,newInterval)
        res = append(res,copyintervals[eint:]...)
        return res
    }else if intervals[sint][0]>newInterval[0] {
        newInterval = []int{newInterval[0],intervals[eint][1]}
        res := intervals[:sint]
        res = append(res,newInterval)
        res = append(res,copyintervals[eint+1:]...)
        return res
    }else if intervals[sint][0]<=newInterval[0] && (eint==len(intervals) || intervals[eint][0]>newInterval[1]){
        newInterval = []int{intervals[sint][0],newInterval[1]}
        res := intervals[:sint]
        res = append(res,newInterval)
        res = append(res,copyintervals[eint:]...)
        return res
    }else{
        res := intervals[:sint]
        newInterval := []int{intervals[sint][0],intervals[eint][1]}
        res = append(res,newInterval)
        res = append(res,copyintervals[eint+1:]...)
        return res
    }

}