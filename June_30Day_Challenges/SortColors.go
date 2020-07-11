func sortColors(nums []int) {
	c, t, z := 0, len(nums)-1, 0
	for c <= t {
		if nums[c] == 1 {
			c++
		} else if nums[c] == 2 {
			nums[c], nums[t] = nums[t], nums[c]
			t--
		} else {
			nums[c], nums[z] = nums[z], nums[c]
			z++
			c++
		}
	}
}