// In a given grid, each cell can have one of three values:

// the value 0 representing an empty cell;
// the value 1 representing a fresh orange;
// the value 2 representing a rotten orange.
// Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

// Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

 

// Example 1:



// Input: [[2,1,1],[1,1,0],[0,1,1]]
// Output: 4
// Example 2:

// Input: [[2,1,1],[0,1,1],[1,0,1]]
// Output: -1
// Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
// Example 3:

// Input: [[0,2]]
// Output: 0
// Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
 

// Note:

// 1 <= grid.length <= 10
// 1 <= grid[0].length <= 10
// grid[i][j] is only 0, 1, or 2.

type cor struct {
    r,c,t int
}
func orangesRotting(grid [][]int) int {
    fresh := 0
    rotten := []cor{}
    deltas := []cor{{0,1,0},{0,-1,0},{1,0,0},{-1,0,0}}
    minute := 0
    for i:=0;i<len(grid);i++{
        for j:=0;j<len(grid[0]);j++{
            if grid[i][j]==2 { //rotten
                rotten = append(rotten,cor{i,j,0})
            }else if grid[i][j]==1 {
                fresh++
            }
        }
    }
    //fmt.Println(rotten)
    for len(rotten)>0{
        curcor := rotten[0]
        if curcor.t > minute {
            minute = curcor.t
        }
        rotten = rotten[1:]
        //fmt.Println(1)
        for _, delcor := range deltas {
            //fmt.Println(i)
            nextdel := cor{curcor.r+delcor.r,curcor.c+delcor.c,curcor.t+1}
            if  0<=nextdel.r && nextdel.r<len(grid) && 0<=nextdel.c && nextdel.c<len(grid[0]) && grid[nextdel.r][nextdel.c] == 1 {
                fresh--
                grid[nextdel.r][nextdel.c] = 2
                rotten = append(rotten,nextdel)
            }
        }
    }
    if fresh==0 {
        return minute
    }
    return -1
}