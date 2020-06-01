// You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

// The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

// Example 1:

// Input: J = "aA", S = "aAAbbbb"
// Output: 3
// Example 2:

// Input: J = "z", S = "ZZ"
// Output: 0
// Note:

// S and J will consist of letters and have length at most 50.
// The characters in J are distinct.
func numJewelsInStones(J string, S string) int {
	jewels := make(map[byte]bool)
	for i := 0; i < len(J); i++ {
		char := J[i]
		jewels[char] = true
	}
	var cnt int = 0
	for i := 0; i < len(S); i++ {
		if _, ok := jewels[S[i]]; ok {
			cnt += 1
		}
	}
	return cnt
}