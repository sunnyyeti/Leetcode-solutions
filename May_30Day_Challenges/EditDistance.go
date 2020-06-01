// Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

// You have the following 3 operations permitted on a word:

// Insert a character
// Delete a character
// Replace a character
// Example 1:

// Input: word1 = "horse", word2 = "ros"
// Output: 3
// Explanation:
// horse -> rorse (replace 'h' with 'r')
// rorse -> rose (remove 'r')
// rose -> ros (remove 'e')
// Example 2:

// Input: word1 = "intention", word2 = "execution"
// Output: 5
// Explanation:
// intention -> inention (remove 't')
// inention -> enention (replace 'i' with 'e')
// enention -> exention (replace 'n' with 'x')
// exention -> exection (replace 'n' with 'c')
// exection -> execution (insert 'u')
func minInts(ints ...int) int {
	min := int(^uint(0) >> 1)
	for _, v := range ints {
		if v < min {
			min = v
		}
	}
	return min
}
func minDistance(word1 string, word2 string) int {
	l1, l2 := len(word1)+1, len(word2)+1
	d := make([][]int, l1)
	for i := 0; i < l1; i++ {
		d[i] = make([]int, l2)
	}
	for c := 1; c < l2; c++ {
		d[0][c] = c
	}
	for r := 1; r < l1; r++ {
		d[r][0] = r
	}
	for i := 0; i < len(word1); i++ {
		for j := 0; j < len(word2); j++ {
			c1 := word1[i]
			c2 := word2[j]
			if c1 == c2 {
				d[i+1][j+1] = d[i][j]
			} else {
				d[i+1][j+1] = minInts(d[i+1][j], d[i][j+1], d[i][j]) + 1
			}
		}
	}
	return d[l1-1][l2-1]
}