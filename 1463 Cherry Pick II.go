func minInts(ints ...int) int {
	minValue := int((^uint(0)) >> 1)
	for _, ele := range ints {
		if ele < minValue {
			minValue = ele
		}
	}
	return minValue
}
func makeDP(col int) (dp [][]int) {
	dp = make([][]int, col)
	for i := 0; i < col; i++ {
		dp[i] = make([]int, col)
	}
	return
}
func cherryPickup(grid [][]int) int {
	rows, cols := len(grid), len(grid[0])
	cur_row := rows - 1
	reached_cols := minInts(cur_row+1, cols)
	dp1 := makeDP(reached_cols)
	for i := 0; i < reached_cols; i++ {
		for j := 0; j < reached_cols; j++ {
			aj := cols - 1 - j
			if i == aj {
				dp1[i][j] = grid[cur_row][i]
			} else {
				dp1[i][j] = grid[cur_row][i] + grid[cur_row][aj]
			}
		}
	}
	for cur_row > 0 {
		cur_row--
		reached_cols = minInts(cur_row+1, cols)
		dp2 := makeDP(reached_cols)
		for i := 0; i < reached_cols; i++ {
			for j := 0; j < reached_cols; j++ {
				aj := cols - 1 - j
				if i == aj {
					dp2[i][j] = grid[cur_row][i]
				} else {
					dp2[i][j] = grid[cur_row][i] + grid[cur_row][aj]
				}
				next_row_max := 0
				for _, delta_col_i := range []int{-1, 0, 1} {
					next_col_i := i + delta_col_i
					if 0 <= next_col_i && next_col_i < cols {
						for _, delta_col_j := range []int{-1, 0, 1} {
							next_col_aj := aj + delta_col_j
							if 0 <= next_col_aj && next_col_aj < cols {
								next_col_j := cols - 1 - next_col_aj
								if dp1[next_col_i][next_col_j] > next_row_max {
									next_row_max = dp1[next_col_i][next_col_j]
								}
							}
						}
					}
				}
				dp2[i][j] += next_row_max
			}
		}
		dp1 = dp2

	}
	return dp1[0][0]

}