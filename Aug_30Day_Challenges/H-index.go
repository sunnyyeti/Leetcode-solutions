import "sort"
//A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each.

func lowerBound(arr []int, begin, end, target int) int {
    for begin<=end{
        mid := begin+(end-begin)/2
        if arr[mid]>=target{
            end = mid-1
        } else {
            begin = mid+1
        }
    }
    return begin
}
func hIndex(citations []int) int {
    sort.Ints(citations)
    left, right := 0, len(citations)
    for left<=right {
        guess := left+(right-left)/2
        lower := lowerBound(citations,0,len(citations)-1,guess)
        if len(citations)-lower < guess {
            right = guess-1
        }else if len(citations)-lower == guess || citations[len(citations)-guess-1]<=guess {
            return guess
        }else {
            left = guess+1
        }
    }
    return left
}