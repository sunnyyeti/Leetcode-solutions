// Given an array nums and two types of queries where you should update the value of an index in the array, and retrieve the sum of a range in the array.

// Implement the NumArray class:

// NumArray(int[] nums) Initializes the object with the integer array nums.
// void update(int index, int val) Updates the value of nums[index] to be val.
// int sumRange(int left, int right) Returns the sum of the subarray nums[left, right] (i.e., nums[left] + nums[left + 1], ..., nums[right]).
 

// Example 1:

// Input
// ["NumArray", "sumRange", "update", "sumRange"]
// [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
// Output
// [null, 9, null, 8]

// Explanation
// NumArray numArray = new NumArray([1, 3, 5]);
// numArray.sumRange(0, 2); // return 9 = sum([1,3,5])
// numArray.update(1, 2);   // nums = [1,2,5]
// numArray.sumRange(0, 2); // return 8 = sum([1,2,5])
 

// Constraints:

// 1 <= nums.length <= 3 * 104
// -100 <= nums[i] <= 100
// 0 <= index < nums.length
// -100 <= val <= 100
// 0 <= left <= right < nums.length
// At most 3 * 104 calls will be made to update and sumRange.
type NumArray struct {
    bit []int
    nums []int
}


func Constructor(nums []int) NumArray {
    bit := make([]int,len(nums)+1)
    nums_ := make([]int,len(nums))
    numarr := NumArray{bit,nums_}
    for i,v := range nums {
        numarr.UpdateDelta(i,v)
    }
    return numarr
}

func (this *NumArray) UpdateDelta(index int, delta int) {
    this.nums[index]+=delta
    index++
    for index<len(this.bit) {
        this.bit[index]+=delta
        index += index & (-index)
    }
}
func (this *NumArray) Update(index int, val int)  {
    delta := val-this.nums[index]
    this.UpdateDelta(index,delta)
    
}

func (this *NumArray) SumTo(index int) int{
    index++
    ans :=0
    for index>0 {
        ans += this.bit[index]
        index -= index&(-index)
    }
    return ans
}

func (this *NumArray) SumRange(left int, right int) int {
    rightv := this.SumTo(right)
    leftv := this.SumTo(left-1)
    //fmt.Println(rightv,leftv)
    return rightv-leftv
}


/**
 * Your NumArray object will be instantiated and called as such:
 * obj := Constructor(nums);
 * obj.Update(index,val);
 * param_2 := obj.SumRange(left,right);
 */