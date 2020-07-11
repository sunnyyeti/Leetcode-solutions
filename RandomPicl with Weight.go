// Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.

// Note:

// 1 <= w.length <= 10000
// 1 <= w[i] <= 10^5
// pickIndex will be called at most 10000 times.
// Example 1:

// Input:
// ["Solution","pickIndex"]
// [[[1]],[]]
// Output: [null,0]
// Example 2:

// Input:
// ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
// [[[1,3]],[],[],[],[],[]]
// Output: [null,0,1,1,1,0]
// Explanation of Input Syntax:

// The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array w. pickIndex has no arguments. Arguments are always wrapped with a list, even if there aren't any.
import "math/rand"

type Solution struct {
	w []int
}

func Constructor(w []int) Solution {
	s := Solution{w}
	for ind := range s.w[1:] {
		s.w[ind+1] += s.w[ind]
	}
	return s

}

func binSearch(arr []int, target int) int {
	i, j := 0, len(arr)-1
	var mid int
	for i <= j {
		mid = i + (j-i)/2
		if arr[mid] < target {
			i = mid + 1
		} else {
			j = mid - 1
		}
	}
	return i
}

func (this *Solution) PickIndex() int {
	r := rand.Intn(this.w[len(this.w)-1]) + 1
	return binSearch(this.w, r)
}

/**
 * Your Solution object will be instantiated and called as such:
 * obj := Constructor(w);
 * param_1 := obj.PickIndex();
 */