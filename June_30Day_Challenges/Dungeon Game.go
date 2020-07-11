// The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

// The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

// Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

// In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

 

// Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

// For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

// -2 (K)	-3	3
// -5	-10	1
// 10	30	-5 (P)
 

// Note:

// The knight's health has no upper bound.
// Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.
func maxInts(ints ...int) int{
    maxValue := ^(int(^uint(0)>>1))
    for _,v := range ints{
        if v>maxValue{
            maxValue = v
        }
    }
    return maxValue
}
func minInts(ints ...int) int {
    minValue := (int(^uint(0)>>1))
    for _,v := range ints{
        if v<minValue{
            minValue = v
        }
    }
    return minValue
}

func calculateMinimumHP(dungeon [][]int) int {
    rows,cols := len(dungeon),len(dungeon[0])
    dungeon[rows-1][cols-1] = maxInts(1-dungeon[rows-1][cols-1],1)
    for c:=cols-2;c>=0;c--{
        dungeon[rows-1][c] = maxInts(1,dungeon[rows-1][c+1]-dungeon[rows-1][c])
    }
    for r:=rows-2;r>=0;r--{
        dungeon[r][cols-1] = maxInts(1,dungeon[r+1][cols-1]-dungeon[r][cols-1])
    }
    for r:=rows-2;r>=0;r--{
        for c:=cols-2;c>=0;c--{
            dungeon[r][c] = minInts(
            maxInts(1,dungeon[r][c+1]-dungeon[r][c]),maxInts(1,dungeon[r+1][c]-dungeon[r][c]),
            )
        }
    }
    return dungeon[0][0]
}