// Given a sentence text (A sentence is a string of space-separated words) in the following format:

// First letter is in upper case.
// Each word in text are separated by a single space.
// Your task is to rearrange the words in text such that all words are rearranged in an increasing order of their lengths. If two words have the same length, arrange them in their original order.

// Return the new text following the format shown above.

// Example 1:

// Input: text = "Leetcode is cool"
// Output: "Is cool leetcode"
// Explanation: There are 3 words, "Leetcode" of length 8, "is" of length 2 and "cool" of length 4.
// Output is ordered by length and the new first word starts with capital letter.
// Example 2:

// Input: text = "Keep calm and code on"
// Output: "On and keep calm code"
// Explanation: Output is ordered as follows:
// "On" 2 letters.
// "and" 3 letters.
// "keep" 4 letters in case of tie order by position in original text.
// "calm" 4 letters.
// "code" 4 letters.
// Example 3:

// Input: text = "To be or not to be"
// Output: "To be or to be not"

// Constraints:

// text begins with a capital letter and then contains lowercase letters and single space between words.
// 1 <= text.length <= 10^5
import (
	"sort"
	"strings"
)

type stringAndIndex struct {
	s   string
	ind int
}

type mySlice []stringAndIndex

func (this mySlice) Less(i, j int) bool {
	return (len(this[i].s) < len(this[j].s)) || (len(this[i].s) == len(this[j].s) && this[i].ind < this[j].ind)
}
func (this mySlice) Len() int {
	return len(this)
}

func (this mySlice) Swap(i, j int) {
	this[i], this[j] = this[j], this[i]
}
func arrangeWords(text string) string {
	terms := strings.Split(text, " ")
	terms[0] = strings.ToLower(terms[0])
	stringInds := make(mySlice, 0)
	for ind, s := range terms {
		stringInds = append(stringInds, stringAndIndex{s, ind})
	}
	sort.Sort(stringInds)
	newterms := make([]string, 0)
	for _, sai := range stringInds {
		newterms = append(newterms, sai.s)
	}
	answer := strings.Join(newterms, " ")
	bytes := []byte(answer)
	bytes[0] -= 32
	return string(bytes)

}