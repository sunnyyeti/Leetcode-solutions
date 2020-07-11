// The set [1,2,3,...,n] contains a total of n! unique permutations.

// By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

// "123"
// "132"
// "213"
// "231"
// "312"
// "321"
// Given n and k, return the kth permutation sequence.

// Note:

// Given n will be between 1 and 9 inclusive.
// Given k will be between 1 and n! inclusive.
// Example 1:

// Input: n = 3, k = 3
// Output: "213"
// Example 2:

// Input: n = 4, k = 9
// Output: "2314"
func getPermutation(n int, k int) string {
	digits := []byte{'1', '2', '3', '4', '5', '6', '7', '8', '9'}[:n]
	fac := make([]int, 10)
	fac[0] = 1
	for i := 1; i < 10; i++ {
		fac[i] = i * fac[i-1]
	}
	inds := make([]int, 0)
	k--
	n--
	for k > 0 {
		nind, nr := k/fac[n], k%fac[n]
		k = nr
		inds = append(inds, nind)
		n--
	}
	//fmt.Println(fac)
	//fmt.Println(inds)
	ans := []byte{}
	for _, ind := range inds {
		ans = append(ans, digits[ind])
		digits = append(digits[:ind], digits[ind+1:]...)
	}
	ans = append(ans, digits...)
	return string(ans)

}