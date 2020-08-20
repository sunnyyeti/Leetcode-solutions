// Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

// This is case sensitive, for example "Aa" is not considered a palindrome here.

// Note:
// Assume the length of given string will not exceed 1,010.

// Example:

// Input:
// "abccccdd"

// Output:
// 7

// Explanation:
// One longest palindrome that can be built is "dccaccd", whose length is 7.
func longestPalindrome(s string) int {
	cnt := make(map[byte]int)
	for i := 0; i < len(s); i++ {
		cnt[s[i]]++
	}
	res := 0
	ifodd := false
	for _, v := range cnt {
		if v&1 == 0 {
			res += v
		} else {
			ifodd = true

			res += v - 1

		}
	}
	if ifodd {
		return res + 1
	}
	return res
}