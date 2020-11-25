// Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

// Integers in each row are sorted from left to right.
// The first integer of each row is greater than the last integer of the previous row.
 

// Example 1:


// Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 3
// Output: true
// Example 2:


// Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 13
// Output: false
// Example 3:

// Input: matrix = [], target = 0
// Output: false
 

// Constraints:

// m == matrix.length
// n == matrix[i].length
// 0 <= m, n <= 100
// -104 <= matrix[i][j], target <= 104
func searchMatrix(matrix [][]int, target int) bool {
    if len(matrix)==0 {
        return false
    }
    rows, cols := len(matrix),len(matrix[0])
    if cols == 0 {
        return false
    }
    start, end := 0, rows*cols-1
    for start<=end {
        mid := start + (end-start)/2
        crow, ccol := mid/cols, mid%cols
        cval := matrix[crow][ccol]
        if cval == target {
            return true
        }else if cval < target {
            start = mid + 1
        }else{
            end = mid - 1
        }
    }
    return false
}