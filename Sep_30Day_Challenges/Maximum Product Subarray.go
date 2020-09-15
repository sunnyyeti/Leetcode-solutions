// Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

// Example 1:

// Input: [2,3,-2,4]
// Output: 6
// Explanation: [2,3] has the largest product 6.
// Example 2:

// Input: [-2,0,-1]
// Output: 0
// Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

func maxProduct(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	allmax := nums[0]
	max, min := nums[0], nums[0]
	var tmax, tmin int
	for _, v := range nums[1:] {
		if v >= 0 {
			if max*v > v {
				tmax = max * v
			} else {
				tmax = v
			}
			if tmax > allmax {
				allmax = tmax
			}
			if min*v < v {
				tmin = min * v
			} else {
				tmin = v
			}
		} else {
			if min*v > v {
				tmax = min * v
			} else {
				tmax = v
			}
			if tmax > allmax {
				allmax = tmax
			}
			if max*v < v {
				tmin = max * v
			} else {
				tmin = v
			}
		}
		max, min = tmax, tmin
		//fmt.Println(max,min,allmax)
	}
	return allmax
}