// Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

// Example:

// Input: 3
// Output: 5
// Explanation:
// Given n = 3, there are a total of 5 unique BST's:

//    1         3     3      2      1
//     \       /     /      / \      \
//      3     2     1      1   3      2
//     /     /       \                 \
//    2     1         2                 3

var cache map[int]int = make(map[int]int)


func numTrees(n int) int {
    if n==1||n==0 {
        return 1
    }
    if value,ok:=cache[n];ok{
        return value
    }
    cnt := 0
    for i:=0;i<=n-1;i++{
        cnt+=numTrees(i)*numTrees(n-1-i)
    }
    cache[n] = cnt
    return cnt
}