// Given a string, sort it in decreasing order based on the frequency of characters.

// Example 1:

// Input:
// "tree"

// Output:
// "eert"

// Explanation:
// 'e' appears twice while 'r' and 't' both appear once.
// So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
// Example 2:

// Input:
// "cccaaa"

// Output:
// "cccaaa"

// Explanation:
// Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
// Note that "cacaca" is incorrect, as the same characters must be together.
// Example 3:

// Input:
// "Aabb"

// Output:
// "bbAa"

// Explanation:
// "bbaA" is also a valid answer, but "Aabb" is incorrect.
// Note that 'A' and 'a' are treated as two different characters.
type pair struct {
	key   byte
	count int
}

func quick_sort(pairlist []pair, start, end int) {
	if start >= end {
		return
	}
	pairlist[start], pairlist[end] = pairlist[end], pairlist[start]
	i, j := start, start
	for j < end {
		if pairlist[j].count > pairlist[end].count {
			pairlist[i], pairlist[j] = pairlist[j], pairlist[i]
			j++
			i++
		} else {
			j++
		}
	}
	pairlist[i], pairlist[end] = pairlist[end], pairlist[i]
	quick_sort(pairlist, start, i-1)
	quick_sort(pairlist, i+1, end)
}
func frequencySort(s string) string {
	cnt := make(map[byte]int)
	for i := 0; i < len(s); i++ {
		cur_char := s[i]
		cnt[cur_char] = cnt[cur_char] + 1
	}
	//fmt.Println(cnt)
	pair_list := make([]pair, len(cnt))
	ind := 0
	for k, v := range cnt {
		pair_list[ind] = pair{k, v}
		ind++
	}
	//fmt.Println(pair_list)
	quick_sort(pair_list, 0, len(pair_list)-1)
	//fmt.Println(pair_list)
	bytes := make([]byte, 0, len(pair_list))
	for _, pair_ele := range pair_list {
		repeat := 0
		for repeat < pair_ele.count {
			bytes = append(bytes, pair_ele.key)
			repeat++
		}

	}
	//fmt.Println(bytes)
	return string(bytes)

}