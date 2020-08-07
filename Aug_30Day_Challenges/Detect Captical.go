// Given a word, you need to judge whether the usage of capitals in it is right or not.

// We define the usage of capitals in a word to be right when one of the following cases holds:

// All letters in this word are capitals, like "USA".
// All letters in this word are not capitals, like "leetcode".
// Only the first letter in this word is capital, like "Google".
// Otherwise, we define that this word doesn't use capitals in a right way.
 

// Example 1:

// Input: "USA"
// Output: True
 

// Example 2:

// Input: "FlaG"
// Output: False
 

// Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.
func allCapitals(word string) bool {
    for _,c := range word {
        if c>'Z' {
            return false
        }
    }
    return true
}

func allLowers(word string) bool {
    for _,c := range word{
        if c<'a'{
            return false
        }
    }
    return true
}

func firstCaptical(word string) bool {
    words := []rune(word)
    if words[0]>'Z'{
        return false
    }
    for i:=1;i<len(words);i++{
        if words[i]<'a'{
            return false
        }
    }
    return true
}

func detectCapitalUse(word string) bool {
    return allCapitals(word) || allLowers(word) || firstCaptical(word)
    
}