// Given a string s, find the length of the longest substring without repeating characters.

 

// Example 1:

// Input: s = "abcabcbb"
// Output: 3
// Explanation: The answer is "abc", with the length of 3.
// Example 2:

// Input: s = "bbbbb"
// Output: 1
// Explanation: The answer is "b", with the length of 1.
// Example 3:

// Input: s = "pwwkew"
// Output: 3
// Explanation: The answer is "wke", with the length of 3.
// Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
// Example 4:

// Input: s = ""
// Output: 0
 

// Constraints:

// 0 <= s.length <= 5 * 104
// s consists of English letters, digits, symbols and spaces.
func lengthOfLongestSubstring(s string) int {
    if len(s)<=1 {
        return len(s)
    }
    pos := map[byte]int{}
    ans := -1
    cur := 1
    i,j := 0,1
    pos[s[0]] = 0
    for j<len(s) {
        curbyte := s[j]
        //fmt.Println(j,curbyte)
        if lastPos,ok:=pos[curbyte];ok{
            for ;i<lastPos+1;i++{
                delete(pos,s[i])
            }
            i = lastPos+1
            //fmt.Println("i",i,"j",j)
            cur = j-i+1
            if cur > ans {
                ans = cur
            }
            pos[curbyte] = j
        }else{
            pos[curbyte] = j
            cur++
            if cur>ans{
                ans = cur
            }
            //fmt.Println("i",i,"j",j)
        }
        j++
    }
    return ans
}