// Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

// Examples:

// s = "leetcode"
// return 0.

// s = "loveleetcode",
// return 2.
// Note: You may assume the string contain only lowercase letters.
func firstUniqChar(s string) int {
	var count []int = make([]int, 26)
	for i := 0; i < len(s); i++ {
		count[s[i]-'a'] += 1
	}
	for i := 0; i < len(s); i++ {
		if count[s[i]-'a'] == 1 {
			return i
		}
	}
	return -1
}