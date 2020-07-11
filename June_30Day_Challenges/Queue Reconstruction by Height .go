// Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

// Note:
// The number of people is less than 1,100.

// Example

// Input:
// [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

// Output:
// [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

import "sort"

type queue [][]int

func (q queue) Len() int {
	return len(q)
}

func (q queue) Less(i, j int) bool {
	a := q[i]
	b := q[j]
	if a[0] < b[0] {
		return true
	} else if a[0] > b[0] {
		return false
	} else {
		return a[1] > b[1]
	}

}

func (q queue) Swap(i, j int) {
	q[i], q[j] = q[j], q[i]
}

func reconstructQueue(people [][]int) [][]int {
	q := queue(people)
	sort.Sort(q)
	//fmt.Println(q)
	ans := make([][]int, len(people))
	used := make([]bool, len(people))
	for _, p := range q {
		t := p[1] + 1
		k := 0
		for i := 0; i < len(used); i++ {
			if !used[i] {
				k++
				if k == t {
					ans[i] = p
					used[i] = true
					break
				}
			}
		}
	}
	return ans

}