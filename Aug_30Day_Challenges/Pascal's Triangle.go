// Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

// Note that the row index starts from 0.


// In Pascal's triangle, each number is the sum of the two numbers directly above it.

// Example:

// Input: 3
// Output: [1,3,3,1]
// Follow up:

// Could you optimize your algorithm to use only O(k) extra space?
func getRow(rowIndex int) []int {
    row := []int{1}
    for i:=1;i<=rowIndex;i++{
        tmp:=[]int{1}
        for j:=0;j<len(row)-1;j++{
            tmp = append(tmp,row[j]+row[j+1])
        }
        tmp  = append(tmp,1)
        row = tmp
    }
    return row
}