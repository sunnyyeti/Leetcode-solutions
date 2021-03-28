// You are given an m x n integer matrix heights representing the height of each unit cell in a continent. The Pacific ocean touches the continent's left and top edges, and the Atlantic ocean touches the continent's right and bottom edges.

// Water can only flow in four directions: up, down, left, and right. Water flows from a cell to an adjacent one with an equal or lower height.

// Return a list of grid coordinates where water can flow to both the Pacific and Atlantic oceans.

 

// Example 1:


// Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
// Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
// Example 2:

// Input: heights = [[2,1],[1,2]]
// Output: [[0,0],[0,1],[1,0],[1,1]]
 

// Constraints:

// m == heights.length
// n == heights[i].length
// 1 <= m, n <= 200
// 1 <= heights[i][j] <= 105
// Accepted
// 116,484
// Submissions
// 265,783
func getNeighbours(p []int,rows,cols int)[][]int{
    r,c := p[0],p[1]
    ans := make([][]int,0,4)
    for _,dp := range [][]int{[]int{1,0},[]int{-1,0},[]int{0,1},[]int{0,-1}} {
        dr,dc := dp[0],dp[1]
        nr,nc := r+dr,c+dc
        if 0<=nr && nr<rows && 0<=nc && nc<cols{
            ans = append(ans,[]int{nr,nc})
        }
    }
    return ans
}
func pacificAtlantic(heights [][]int) [][]int {
    rows, cols := len(heights),len(heights[0])
    reachable := make([][]int,rows)
    for i:=0; i<len(reachable);i++{
        reachable[i] = make([]int,cols)
    }
    queue := make([][]int,0,rows*cols)
    for c:=0; c<cols;c++{
        queue = append(queue,[]int{0,c})
        reachable[0][c] = 1
    }
    for r:=0;r<rows;r++{
        queue = append(queue,[]int{r,0})
        reachable[r][0] = 1
    }
    for len(queue)>0 {
        cp := queue[0]
        //fmt.Println("Current:",cp)
        queue = queue[1:len(queue)]
        nextPs := getNeighbours(cp,rows,cols)
        //fmt.Println("Next points:",nextPs)
        for _,np := range nextPs {
            if reachable[np[0]][np[1]] == 0 && heights[np[0]][np[1]]>=heights[cp[0]][cp[1]] {
                reachable[np[0]][np[1]] = 1
                queue = append(queue,np)
                //fmt.Println("Set point",np)
            }     
        }
    }
    //fmt.Println(reachable)
    for c:=0; c<cols;c++{
        queue = append(queue,[]int{rows-1,c})
        if reachable[rows-1][c] == 1{
            reachable[rows-1][c] = 2
        }else if reachable[rows-1][c] == 0{
            reachable[rows-1][c] = -1
        }
        
    }
    for r:=0;r<rows;r++{
        queue = append(queue,[]int{r,cols-1})
        if reachable[r][cols-1] == 1{
            reachable[r][cols-1] = 2
        }else if reachable[r][cols-1] == 0{
            reachable[r][cols-1] = -1
        }
    }
    //fmt.Println(reachable)
    for len(queue)>0 {
        cp := queue[0]
        queue = queue[1:len(queue)]
        nextPs := getNeighbours(cp,rows,cols)
        for _,np := range nextPs {
            if heights[np[0]][np[1]]>=heights[cp[0]][cp[1]] {
                if reachable[np[0]][np[1]] == 0 {
                    reachable[np[0]][np[1]] = -1
                    queue = append(queue,np)
                }else if reachable[np[0]][np[1]] == 1 {
                    reachable[np[0]][np[1]] = 2
                    queue = append(queue,np)
                }
                
            }     
        }
    }
    ans := [][]int{}
    for r:=0;r<rows;r++{
        for c:=0;c<cols;c++{
            if  reachable[r][c] == 2 {
                ans = append(ans,[]int{r,c})
            }
        }
    }
    return ans
    
}