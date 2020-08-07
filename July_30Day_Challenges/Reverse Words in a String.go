// Given an input string, reverse the string word by word.

 

// Example 1:

// Input: "the sky is blue"
// Output: "blue is sky the"
// Example 2:

// Input: "  hello world!  "
// Output: "world! hello"
// Explanation: Your reversed string should not contain leading or trailing spaces.
// Example 3:

// Input: "a good   example"
// Output: "example good a"
// Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

// Note:

// A word is defined as a sequence of non-space characters.
// Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
// You need to reduce multiple spaces between two words to a single space in the reversed string.
 

// Follow up:

// For C programmers, try to solve it in-place in O(1) extra space.
import "strings"
func reverseWords(s string) string {
    ele := make([]byte,0)
    ans := make([]string,0)
    for i:=0;i<len(s);i++{
        curByte:=s[i]
        if curByte==' '{
            if len(ele)>0{
                ans = append(ans,string(ele))
                ele = make([]byte,0)
            }
        }else{
            ele = append(ele,curByte)
        }
    }
    if len(ele)>0{
        ans = append(ans,string(ele))
    }
    for i,j:=0,len(ans)-1;i<j;i,j=i+1,j-1{
        ans[i],ans[j] = ans[j],ans[i]
    }
    return strings.Join(ans," ")
    
    
}