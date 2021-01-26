// You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

 

// Example 1:

// Input: nums = [5,2,6,1]
// Output: [2,1,1,0]
// Explanation:
// To the right of 5 there are 2 smaller elements (2 and 1).
// To the right of 2 there is only 1 smaller element (1).
// To the right of 6 there is 1 smaller element (1).
// To the right of 1 there is 0 smaller element.
 

// Constraints:

// 0 <= nums.length <= 10^5
// -10^4 <= nums[i] <= 10^4
// Accepted
// 156,871
// Submissions
// 368,248
// Seen this question in a real interview before?
func countSmaller(nums []int) []int {
    if len(nums)==0{
        return nums
    }
    ids := make([]int,len(nums))
    for i:=0;i<len(ids);i++{
        ids[i]=i
    }
    
    less := make(map[int]int,len(nums))
    mergeSort(ids,0,len(ids)-1,nums,less)
    //fmt.Println(ids,less)
    ans := make([]int,len(nums))
    for i:=0;i<len(ans);i++{
        ans[i] = less[i]
    }
    return ans
}

func mergeSort(ids []int, start int, end int, nums []int, less map[int]int){
    if start==end {
        return
    }
    mid := start + (end-start)/2
    mergeSort(ids, start, mid, nums,less)
    mergeSort(ids,mid+1,end,nums,less)
    left := make([]int,mid-start+1)
    for i:=start;i<=mid;i++{
        left[i-start]=ids[i]
    }
    right := make([]int,end-mid)
    for i:=mid+1;i<=end;i++{
        right[i-mid-1] = ids[i]
    }
    //fmt.Println(left,right)
    i,j,k :=0,0,0
    for i<len(left) && j<len(right) {
        if nums[left[i]] > nums[right[j]] {
            ids[k+start] = left[i]
            less[left[i]]+=len(right)-j
            i++
        }else{
            ids[k+start] = right[j]
            j++
        }
        k++
    }
    for i<len(left){
        ids[k+start]=left[i]
        i++
        k++
    }
    for j<len(right){
        ids[k+start] = right[j]
        j++
        k++
    }
    //fmt.Println(ids)
}