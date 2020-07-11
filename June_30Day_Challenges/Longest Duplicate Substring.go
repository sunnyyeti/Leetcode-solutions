// Given a string S, consider all duplicated substrings: (contiguous) substrings of S that occur 2 or more times.  (The occurrences may overlap.)

// Return any duplicated substring that has the longest possible length.  (If S does not have a duplicated substring, the answer is "".)

// Example 1:

// Input: "banana"
// Output: "ana"
// Example 2:

// Input: "abcd"
// Output: ""

// Note:

// 2 <= S.length <= 10^5
// S consists of lowercase English letters.
func longestDupSubstring(S string) string {
	start := 1
	end := len(S) - 1
	var ans string
	for start <= end {
		l := start + (end-start)/2
		//fmt.Println(l)
		d := RKD(S, l)
		if d != "" {
			ans = d
			start = l + 1
		} else {
			end = l - 1
		}
	}
	return ans

}

func hashStr(str string) uint {
	var sum uint = 0
	for i := 0; i < len(str); i++ {
		val := uint(str[i] - 'a')
		sum = (sum*26 + val) % 101
	}
	return sum
}

type span struct {
	start, end int
}

func RKD(S string, l int) string {
	hashSpan := make(map[uint][]span)
	firstSubString := S[:l]
	hash := hashStr(firstSubString)
	hashSpan[hash] = []span{span{0, l}}
	var shift uint = 1
	for i := 1; i < l; i++ {
		shift = (shift * 26) % 101
	}
	for i := l; i < len(S); i++ {
		val := uint(S[i] - 'a')
		ini := uint(S[i-l] - 'a')
		hash = ((hash+101-(ini*shift)%101)*26 + val) % 101
		if val, ok := hashSpan[hash]; ok {
			for _, span := range val {
				if S[span.start:span.end] == S[i-l+1:i+1] {
					return S[i-l+1 : i+1]
				}
			}
			val = append(val, span{i - l + 1, i + 1})
			hashSpan[hash] = val
		} else {
			hashSpan[hash] = []span{span{i - l + 1, i + 1}}
		}
	}
	return ""
}