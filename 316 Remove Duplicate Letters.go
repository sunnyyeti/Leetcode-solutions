// Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

// Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

 

// Example 1:

// Input: s = "bcabc"
// Output: "abc"
// Example 2:

// Input: s = "cbacdcbc"
// Output: "acdb"
 

// Constraints:

// 1 <= s.length <= 104
// s consists of lowercase English letters.
func removeDuplicateLetters(s string) string {
    last_index := make([]int,26)
    for i:=0; i<len(s); i++ {
        last_index[s[i]-97] = i
    }
    stack := make([]byte,0)
    visited := make([]bool,26)
    for i:=0; i<len(s); i++ {
        if !visited[s[i]-97] {
            if len(stack)==0 || s[i]>=stack[len(stack)-1] {
                stack = append(stack,s[i])
                //fmt.Println(string(stack))
                visited[s[i]-97] = true
            }else {
                for len(stack) > 0 && stack[len(stack)-1]>s[i] && last_index[stack[len(stack)-1]-97] > i {
                    visited[stack[len(stack)-1]-97]=false
                    stack = stack[:len(stack)-1]
                }
                stack = append(stack,s[i])
                //fmt.Println(string(stack))
                visited[s[i]-97] = true
            }
      }  
   }
     return string(stack)
}