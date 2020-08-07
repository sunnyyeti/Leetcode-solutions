// Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

// Note: For the purpose of this problem, we define empty string as valid palindrome.

// Example 1:

// Input: "A man, a plan, a canal: Panama"
// Output: true
// Example 2:

// Input: "race a car"
// Output: false
 

// Constraints:

// s consists only of printable ASCII characters.
func isalphanumeric(char byte) bool {
    return ('a'<=char && char<='z') || ('A'<=char && char<='Z') || ('0'<=char && char<='9')
}

func isEqual(char1, char2 byte) bool {
    if char1==char2 {
        return true
    }
    if char1<char2 {
        char1,char2 = char2,char1
    }
    return (char1-char2 == 32) && char1>='a'
}

func isPalindrome(s string) bool {
    for i,j:=0,len(s)-1; i<j; {
        if !isalphanumeric(s[i]){
            i++
        }else if !isalphanumeric(s[j]){
            j--
        }else{
            if isEqual(s[i],s[j]){
                i++
                j--
            }else{
                return false
            }
        }
    }
    return true
}