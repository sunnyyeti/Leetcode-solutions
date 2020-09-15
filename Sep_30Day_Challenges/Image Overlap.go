// You are given two images img1 and img2 both of size n x n, represented as binary, square matrices of the same size. (A binary matrix has only 0s and 1s as values.)

// We translate one image however we choose (sliding it left, right, up, or down any number of units), and place it on top of the other image.  After, the overlap of this translation is the number of positions that have a 1 in both images.

// (Note also that a translation does not include any kind of rotation.)

// What is the largest possible overlap?

// Example 1:

// Input: img1 = [[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]]
// Output: 3
// Explanation: We slide img1 to right by 1 unit and down by 1 unit.

// The number of positions that have a 1 in both images is 3. (Shown in red)

// Example 2:

// Input: img1 = [[1]], img2 = [[1]]
// Output: 1
// Example 3:

// Input: img1 = [[0]], img2 = [[0]]
// Output: 0

// Constraints:

// n == img1.length
// n == img1[i].length
// n == img2.length
// n == img2[i].length
// 1 <= n <= 30
// img1[i][j] is 0 or 1.
// img2[i][j] is 0 or 1.
type Cor struct {
	x, y int
}

func getOnes(arr [][]int) (res []Cor) {
	for i := 0; i < len(arr); i++ {
		for j := 0; j < len(arr[0]); j++ {
			if arr[i][j] == 1 {
				res = append(res, Cor{i, j})
			}
		}
	}
	return
}
func largestOverlap(A [][]int, B [][]int) int {
	onesA := getOnes(A)
	onesB := getOnes(B)
	vecCnt := make(map[Cor]int)
	ans := 0
	for _, cora := range onesA {
		for _, corb := range onesB {
			del := Cor{corb.x - cora.x, corb.y - cora.y}
			vecCnt[del]++
			if vecCnt[del] > ans {
				ans = vecCnt[del]
			}
		}
	}
	return ans
}