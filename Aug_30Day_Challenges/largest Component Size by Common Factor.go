// Given a non-empty array of unique positive integers A, consider the following graph:

// There are A.length nodes, labelled A[0] to A[A.length - 1];
// There is an edge between A[i] and A[j] if and only if A[i] and A[j] share a common factor greater than 1.
// Return the size of the largest connected component in the graph.

// Example 1:

// Input: [4,6,15,35]
// Output: 4

// Example 2:

// Input: [20,50,9,63]
// Output: 2

// Example 3:

// Input: [2,3,6,7,4,12,21,39]
// Output: 8

// Note:

// 1 <= A.length <= 20000
// 1 <= A[i] <= 100000
//import "math"
func largest(arr ...int) int {
	max := ^int((^uint(0)) >> 1)
	for _, v := range arr {
		if v > max {
			max = v
		}
	}
	return max
}

func getPrimes(up int) []int {
	tab := make([]int, up+1)
	tab[1] = 1
	j := 2
	for j <= up {
		tab[j] = 2
		j += 2
	}
	for i := 3; i <= up; i += 2 {
		if tab[i] == 0 {
			j = i
			for j <= up {
				tab[j] = i
				j += i
			}
		}
	}
	return tab

}

func getParent(parents []int, ind int) int {
	for parents[ind] != ind {
		ind = parents[ind]
	}
	return ind
}

func connect(parents []int, i, j int) {
	pi, pj := getParent(parents, i), getParent(parents, j)
	if pi != pj {
		parents[pi] = pj
	}
}

func largestComponentSize(A []int) int {
	maxEle := largest(A...)
	primes := getPrimes(maxEle)
	containsPrimes := make(map[int][]int, len(primes))
	for ind, val := range A {
		for primes[val] != 1 {
			containsPrimes[primes[val]] = append(containsPrimes[primes[val]], ind)
			val /= primes[val]
		}
	}
	parents := make([]int, len(A))
	for i := 0; i < len(A); i++ {
		parents[i] = i
	}
	for _, inds := range containsPrimes {
		for i := 0; i < len(inds)-1; i++ {
			connect(parents, inds[i], inds[i+1])
		}
	}
	//fmt.Println(containsPrimes)
	//fmt.Println(parents)
	size := make(map[int]int)
	for i := 0; i < len(parents); i++ {
		p := getParent(parents, i)
		size[p] = size[p] + 1
	}
	maxC := 1
	for _, v := range size {
		if v > maxC {
			maxC = v
		}
	}
	return maxC

}