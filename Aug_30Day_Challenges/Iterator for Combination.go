// Design an Iterator class, which has:

// A constructor that takes a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
// A function next() that returns the next combination of length combinationLength in lexicographical order.
// A function hasNext() that returns True if and only if there exists a next combination.

// Example:

// CombinationIterator iterator = new CombinationIterator("abc", 2); // creates the iterator.

// iterator.next(); // returns "ab"
// iterator.hasNext(); // returns true
// iterator.next(); // returns "ac"
// iterator.hasNext(); // returns true
// iterator.next(); // returns "bc"
// iterator.hasNext(); // returns false

// Constraints:

// 1 <= combinationLength <= characters.length <= 15
// There will be at most 10^4 function calls per test.
// It's guaranteed that all calls of the function next are valid.
type CombinationIterator struct {
	chars string
	inds  []int
	res   []byte
}

func Constructor(characters string, combinationLength int) CombinationIterator {
	inds := make([]int, combinationLength)
	res := make([]byte, combinationLength)
	for i := 1; i < len(inds)-1; i++ {
		inds[i] = i
	}
	inds[len(inds)-1] = len(inds) - 2
	for i, ind := range inds {
		if ind >= 0 {
			res[i] = characters[ind]
		}
	}
	return CombinationIterator{chars: characters, inds: inds, res: res}
}

func (this *CombinationIterator) Next() string {
	var startagain int
	for i := len(this.inds) - 1; i >= 0; i-- {
		curind := this.inds[i]
		if curind != len(this.chars)-(len(this.inds)-i) {
			this.inds[i]++
			for j := i + 1; j < len(this.inds); j++ {
				this.inds[j] = this.inds[j-1] + 1
			}
			startagain = i
			break
		}
	}
	for i := startagain; i < len(this.inds); i++ {
		this.res[i] = this.chars[this.inds[i]]
	}
	return string(this.res)
}

func (this *CombinationIterator) HasNext() bool {
	return this.inds[0] != len(this.chars)-len(this.inds)
}

/**
 * Your CombinationIterator object will be instantiated and called as such:
 * obj := Constructor(characters, combinationLength);
 * param_1 := obj.Next();
 * param_2 := obj.HasNext();
 */