// You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

// Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

// The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

// Example:

// Input:
// [[0,1,0,0],
//  [1,1,1,0],
//  [0,1,0,0],
//  [1,1,0,0]]

// Output: 16

// Explanation: The perimeter is the 16 yellow stripes in the image below:

type Pos struct {
	row, col int
}
func islandPerimeter(grid [][]int) int {
	if len(grid) == 0 {
		return 0
	}
	rows, cols := len(grid), len(grid[0])
	visited := make(map[Pos]bool)
	perimeter := 0
	perimeterCalc := func(grid [][]int, pos Pos) {
		queue := []Pos{pos}
		for len(queue) > 0 {
			//fmt.Println(queue)
			curPos := queue[0]
			queue = queue[1:]
			waterCnt := 0
			for _, delPos := range []Pos{Pos{0, 1}, Pos{0, -1}, Pos{1, 0}, Pos{-1, 0}} {
				nextRow := curPos.row + delPos.row
				nextCol := curPos.col + delPos.col
				if nextRow < 0 || nextRow >= rows || nextCol < 0 || nextCol >= cols || grid[nextRow][nextCol] == 0 {
					waterCnt++
				} else {
					nextPos := Pos{nextRow, nextCol}
					if visited[nextPos] == false {
						visited[nextPos] = true
						queue = append(queue, nextPos)
					}
				}
			}
			//fmt.Println(waterCnt)
			perimeter += waterCnt

		}
	}
outer:
	for i := 0; i < rows; i++ {
		for j := 0; j < cols; j++ {
			if grid[i][j] == 1 {
				visited[Pos{i, j}] = true
				perimeterCalc(grid, Pos{i, j})
				break outer
			}
		}
	}
	return perimeter
}