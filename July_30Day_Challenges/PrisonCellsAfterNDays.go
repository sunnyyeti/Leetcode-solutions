// There are 8 prison cells in a row, and each cell is either occupied or vacant.

// Each day, whether the cell is occupied or vacant changes according to the following rules:

// If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
// Otherwise, it becomes vacant.
// (Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)

// We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.

// Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)

// Example 1:

// Input: cells = [0,1,0,1,1,0,0,1], N = 7
// Output: [0,0,1,1,0,0,0,0]
// Explanation:
// The following table summarizes the state of the prison on each day:
// Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
// Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
// Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
// Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
// Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
// Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
// Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
// Day 7: [0, 0, 1, 1, 0, 0, 0, 0]

// Example 2:

// Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
// Output: [0,0,1,1,1,1,1,0]

// Note:

// cells.length == 8
// cells[i] is in {0, 1}
// 1 <= N <= 10^9
func prisonAfterNDays(cells []int, N int) []int {
	var dayVal byte = 0
	var remain int
	for _, bit := range cells {
		dayVal = dayVal*2 + byte(bit)
	}
	pos := map[byte]int{dayVal: 0}
	for day := 1; day <= N; day++ {
		dayVal = ^((dayVal << 1) ^ (dayVal >> 1))
		dayVal &^= 1 << 7
		dayVal &^= 1
		if previousDay, ok := pos[dayVal]; ok {
			period := day - previousDay
			remain = (N - previousDay + 1) % period
			if remain == 0 {
				remain = period
			}
			break

		} else {
			pos[dayVal] = day
		}

	}
	//fmt.Println(pos)
	for k := 1; k < remain; k++ {
		dayVal = ^((dayVal << 1) ^ (dayVal >> 1))
		dayVal &^= 1 << 7
		dayVal &^= 1
	}
	ans := make([]int, 8)
	ind := 7
	for dayVal > 0 {
		ans[ind] = int(dayVal & 1)
		dayVal >>= 1
		ind--
	}
	return ans
}