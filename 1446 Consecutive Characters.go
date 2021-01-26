// Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.

// Return the power of the string.

 

// Example 1:

// Input: s = "leetcode"
// Output: 2
// Explanation: The substring "ee" is of length 2 with the character 'e' only.
// Example 2:

// Input: s = "abbcccddddeeeeedcba"
// Output: 5
// Explanation: The substring "eeeee" is of length 5 with the character 'e' only.
// Example 3:

// Input: s = "triplepillooooow"
// Output: 5
// Example 4:

// Input: s = "hooraaaaaaaaaaay"
// Output: 11
// Example 5:

// Input: s = "tourist"
// Output: 1
 

// Constraints:

// 1 <= s.length <= 500
// s contains only lowercase English letters.
func maxPower(s string) int {
    var last_char  byte = 'A'
    last_len :=0
    max_len := 0
    for i:=0; i<len(s); i++ {
        cur_char := s[i]
        if cur_char==last_char{
            last_len++
        }else{
            if last_len > max_len {
                max_len = last_len
            }
            last_len = 1
            last_char = cur_char
        }
    }
    if last_len > max_len {
        max_len = last_len
    }
    return max_len
}