// Implement a trie with insert, search, and startsWith methods.

// Example:

// Trie trie = new Trie();

// trie.insert("apple");
// trie.search("apple");   // returns true
// trie.search("app");     // returns false
// trie.startsWith("app"); // returns true
// trie.insert("app");
// trie.search("app");     // returns true
// Note:

// You may assume that all inputs are consist of lowercase letters a-z.
// All inputs are guaranteed to be non-empty strings.
type Trie struct {
	isend    bool
	children map[byte]*Trie
}

/** Initialize your data structure here. */
func Constructor() Trie {
	return Trie{isend: false, children: make(map[byte]*Trie)}
}

/** Inserts a word into the trie. */
func (this *Trie) Insert(word string) {
	for i := 0; i < len(word); i++ {
		char := word[i]
		if val, ok := this.children[char]; ok {
			this = val
		} else {
			val := &Trie{false, make(map[byte]*Trie)}
			this.children[char] = val
			this = val
		}
	}
	this.isend = true
}

/** Returns if the word is in the trie. */
func (this *Trie) Search(word string) bool {
	for i := 0; i < len(word); i++ {
		char := word[i]
		if val, ok := this.children[char]; ok {
			this = val
		} else {
			return false
		}
	}
	return this.isend == true
}

/** Returns if there is any word in the trie that starts with the given prefix. */
func (this *Trie) StartsWith(word string) bool {
	for i := 0; i < len(word); i++ {
		char := word[i]
		if val, ok := this.children[char]; ok {
			this = val
		} else {
			return false
		}
	}
	return true
}

/**
 * Your Trie object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Insert(word);
 * param_2 := obj.Search(word);
 * param_3 := obj.StartsWith(prefix);
 */