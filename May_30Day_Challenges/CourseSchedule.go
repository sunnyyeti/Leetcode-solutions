// There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

// Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

// Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

// Example 1:

// Input: numCourses = 2, prerequisites = [[1,0]]
// Output: true
// Explanation: There are a total of 2 courses to take.
//              To take course 1 you should have finished course 0. So it is possible.
// Example 2:

// Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
// Output: false
// Explanation: There are a total of 2 courses to take.
//              To take course 1 you should have finished course 0, and to take course 0 you should
//              also have finished course 1. So it is impossible.

// Constraints:

// The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
// You may assume that there are no duplicate edges in the input prerequisites.
// 1 <= numCourses <= 10^5
func canFinish(numCourses int, prerequisites [][]int) bool {
	out := make(map[int][]int)
	in := make(map[int]map[int]bool)
	for _, p := range prerequisites {
		out[p[1]] = append(out[p[1]], p[0])
		ins := in[p[0]]
		if ins == nil {
			ins = make(map[int]bool)
		}
		ins[p[1]] = true
		in[p[0]] = ins
	}
	noins_stack := make([]int, 0)
	for i := 0; i < numCourses; i++ {
		if _, ok := in[i]; !ok {
			noins_stack = append(noins_stack, i)
		}
	}
	ans := make([]int, 0)
	for len(noins_stack) > 0 {
		cur := noins_stack[len(noins_stack)-1]
		noins_stack = noins_stack[:len(noins_stack)-1]
		ans = append(ans, cur)
		outs := out[cur]
		for len(outs) > 0 {
			next := outs[len(outs)-1]
			outs = outs[:len(outs)-1]
			ins := in[next]
			delete(ins, cur)
			if len(ins) == 0 {
				noins_stack = append(noins_stack, next)
			}
			in[next] = ins
		}

	}
	return len(ans) == numCourses

}