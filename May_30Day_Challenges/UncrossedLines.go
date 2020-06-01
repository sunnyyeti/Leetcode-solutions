// We write the integers of A and B (in the order they are given) on two separate horizontal lines.

// Now, we may draw connecting lines: a straight line connecting two numbers A[i] and B[j] such that:

// A[i] == B[j];
// The line we draw does not intersect any other connecting (non-horizontal) line.
// Note that a connecting lines cannot intersect even at the endpoints: each number can only belong to one connecting line.

// Return the maximum number of connecting lines we can draw in this way.

// Example 1:

// Input: A = [1,4,2], B = [1,2,4]
// Output: 2
// Explanation: We can draw 2 uncrossed lines as in the diagram.
// We cannot draw 3 uncrossed lines, because the line from A[1]=4 to B[2]=4 will intersect the line from A[2]=2 to B[1]=2.
// Example 2:

// Input: A = [2,5,1,2,5], B = [10,5,2,1,5,2]
// Output: 3
// Example 3:

// Input: A = [1,3,7,1,7,5], B = [1,9,2,5,1]
// Output: 2

// Note:

// 1 <= A.length <= 500
// 1 <= B.length <= 500
// 1 <= A[i], B[i] <= 2000
func maxInts(ints ...int) int {
	max := -1
	for _, value := range ints {
		if value > max {
			max = value
		}
	}
	return max
}

func maxUncrossedLines(A []int, B []int) int {
	lenA := len(A)
	lenB := len(B)
	//fmt.Println(lenA,lenB)
	maxLines := make([][]int, lenA)
	for i := 0; i < lenA; i++ {
		maxLines[i] = make([]int, lenB)
	}
	for j := 0; j < lenB; j++ {
		if A[0] == B[j] {
			maxLines[0][j] = 1
		} else if j > 0 {
			maxLines[0][j] = maxLines[0][j-1]
		}
	}
	for i := 0; i < lenA; i++ {
		if A[i] == B[0] {
			maxLines[i][0] = 1
		} else if i > 0 {
			maxLines[i][0] = maxLines[i-1][0]
		}
	}
	for i := 1; i < lenA; i++ {
		for j := 1; j < lenB; j++ {
			//fmt.Println(i,j)
			if A[i] == B[j] {
				maxLines[i][j] = maxLines[i-1][j-1] + 1
			} else {
				maxLines[i][j] = maxInts(maxLines[i-1][j], maxLines[i][j-1])
			}
		}
	}
	return maxLines[lenA-1][lenB-1]

}