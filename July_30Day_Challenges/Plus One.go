// Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

// The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

// You may assume the integer does not contain any leading zero, except the number 0 itself.

// Example 1:

// Input: [1,2,3]
// Output: [1,2,4]
// Explanation: The array represents the integer 123.
// Example 2:

// Input: [4,3,2,1]
// Output: [4,3,2,2]
// Explanation: The array represents the integer 4321.
func plusOne(digits []int) []int {
	res := make([]int, len(digits)+1)
	c := 1
	ind := len(res) - 1
	var sum int
	for ind >= 0 {
		if ind > 0 {
			sum = digits[ind-1] + c
		} else {
			sum = c
		}

		res[ind] = sum % 10
		c = sum / 10
		ind--
	}
	var start int
	for ; res[start] == 0; start++ {
	}
	return res[start:]

}