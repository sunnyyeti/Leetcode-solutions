// Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

// Find all the elements that appear twice in this array.

// Could you do it without extra space and in O(n) runtime?

// Example:
// Input:
// [4,3,2,7,8,2,3,1]

// Output:
// [2,3]
func findDuplicates(nums []int) []int {
	res := []int{}
	var tmp int
	for i := 0; i < len(nums); i++ {
		curv := nums[i]
		curi := i + 1
		tmp = curv
		if curv > 0 { // 还没开始探索,不然0代表已经探索过了，负数肯定也往下探索过了
			for nums[curv-1] >= 0 { // not occurred for curv,cuev还没标记为出现
				tmp := nums[curv-1]  //keep the ele indexed at curv-1
				nums[curv-1] = -curi // flag at curv-1, indicating curv has occurred
				if tmp == 0 {
					break
				}
				curi = curv // index of next val
				curv = tmp  // next val
			}

			if tmp != 0 && nums[curv-1] != -curi {
				res = append(res, curv)
			}
			if nums[curi-1] > 0 {
				nums[curi-1] = 0 // 当前的值已经往下探索过了
			}
		}
	}
	return res
}