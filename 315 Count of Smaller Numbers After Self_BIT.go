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
func countSmaller(nums []int) []int {
    if len(nums)==0{
        return nums
    }
    bit := make([]int,20000+2)
    ans := make([]int, len(nums))
    for i:=len(nums)-1;i>-1;i--{
        curele := nums[i]
        ind := curele-(-10000)
        ans[i] =  getSum(bit,ind-1)
        update(bit,ind,1)
    }
    return ans
    
}


func getSum(bit []int, ind int) int{
    ind++
    ans := 0
    for ind>0 {
        ans += bit[ind]
        ind-= ind&(-ind)
    } 
    return ans
}

func update(bit []int, ind, delta int){
    ind++
    for ind<len(bit) {
        bit[ind]+=delta
        ind += ind&(-ind)
    }
}