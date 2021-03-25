// Given an integer array arr, and an integer target, return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.

// As the answer can be very large, return it modulo 109 + 7.

// Example 1:

// Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
// Output: 20
// Explanation:
// Enumerating by the values (arr[i], arr[j], arr[k]):
// (1, 2, 5) occurs 8 times;
// (1, 3, 4) occurs 8 times;
// (2, 2, 4) occurs 2 times;
// (2, 3, 3) occurs 2 times.
// Example 2:

// Input: arr = [1,1,2,2,2,2], target = 5
// Output: 12
// Explanation:
// arr[i] = 1, arr[j] = arr[k] = 2 occurs 12 times:
// We choose one 1 from [1,1] in 2 ways,
// and two 2s from [2,2,2,2] in 6 ways.

// Constraints:

// 3 <= arr.length <= 3000
// 0 <= arr[i] <= 100
// 0 <= target <= 300
import "sort"

const M uint64 = 1000000007

type Tuple struct {
	a, b, c int
}

func newTuple(a, b, c int) Tuple {
	s := []int{a, b, c}
	sort.Ints(s)
	return Tuple{s[0], s[1], s[2]}
}

func C(n, k uint64) uint64 {
	var ans uint64 = 1
	for i := n - k + 1; i <= n; i++ {
		ans *= (i)
	}
	fk := uint64(1)
	for i := uint64(1); i <= k; i++ {
		fk *= i
	}
	return ((ans / (fk)) % (M))
}

func threeSumMulti(arr []int, target int) int {
	cnt := make(map[int]uint64)
	for _, v := range arr {
		cnt[v] += 1
	}
	ans := uint64(0)
	occurred := map[Tuple]bool{}
	for k1, _ := range cnt {
		first := k1
		for k2, _ := range cnt {
			second := k2
			third := target - first - second
			tuple := newTuple(first, second, third)
			if _, ok := occurred[tuple]; ok {
				continue
			}
			occurred[tuple] = true
			if _, ok := cnt[third]; ok {
				//fmt.Println(first,second,third)
				if first == second && first == third {
					if cnt[first] >= 3 {
						ans = (ans + C(cnt[first], 3)) % M
					}
				} else if first == second {
					if cnt[first] >= 2 {
						ans = (ans + (C(cnt[first], 2)*(cnt[third]%M))%M) % M
					}
				} else if first == third {
					if cnt[first] >= 2 {
						ans = (ans + (C(cnt[first], 2)*(cnt[second]%M))%M) % M
					}
				} else if second == third {
					if cnt[second] >= 2 {
						ans = (ans + (C(cnt[second], 2)*(cnt[first]%M))%M) % M
					}
				} else {
					ans = (ans + (cnt[second]%M*(cnt[first]%M)*(cnt[third]%M))%M) % M
				}
			}
		}
	}
	return int(ans)
}