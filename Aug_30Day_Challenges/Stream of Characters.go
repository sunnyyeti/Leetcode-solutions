// Implement the StreamChecker class as follows:

// StreamChecker(words): Constructor, init the data structure with the given words.
// query(letter): returns true if and only if for some k >= 1, the last k characters queried (in order from oldest to newest, including this letter just queried) spell one of the words in the given list.
 

// Example:

// StreamChecker streamChecker = new StreamChecker(["cd","f","kl"]); // init the dictionary.
// streamChecker.query('a');          // return false
// streamChecker.query('b');          // return false
// streamChecker.query('c');          // return false
// streamChecker.query('d');          // return true, because 'cd' is in the wordlist
// streamChecker.query('e');          // return false
// streamChecker.query('f');          // return true, because 'f' is in the wordlist
// streamChecker.query('g');          // return false
// streamChecker.query('h');          // return false
// streamChecker.query('i');          // return false
// streamChecker.query('j');          // return false
// streamChecker.query('k');          // return false
// streamChecker.query('l');          // return true, because 'kl' is in the wordlist
 

// Note:

// 1 <= words.length <= 2000
// 1 <= words[i].length <= 2000
// Words will only consist of lowercase English letters.
// Queries will only consist of lowercase English letters.
// The number of queries is at most 40000.
type Node struct {
    end bool
    children map[byte]*Node
}

func (this *Node) add(word string){
    for i:=0; i<len(word); i++{
        curbyte := word[i]
        if _, ok := this.children[curbyte]; !ok{
            newNode := &Node{false,make(map[byte]*Node)}
            this.children[curbyte] = newNode
        }
        this = this.children[curbyte]
    }
    this.end = true
} 

type StreamChecker struct {
    root *Node
    level []*Node
}


func Constructor(words []string) StreamChecker {
    root := &Node{false,make(map[byte]*Node)}
    for _,word := range words {
        root.add(word)
    }
    return StreamChecker{root, make([]*Node,0)}
}


func (this *StreamChecker) Query(letter byte) bool {
    nextlevel := make([]*Node,0)
    for _, n := range this.level {
        if _,ok := n.children[letter]; ok {
            nextlevel = append(nextlevel,n.children[letter])
        }
    }
    if _, ok := this.root.children[letter]; ok {
        nextlevel = append(nextlevel,this.root.children[letter])
    }
    this.level = nextlevel
    for _, reached := range nextlevel {
        if reached.end {
            return true
        }
    }
    return false
}


/**
 * Your StreamChecker object will be instantiated and called as such:
 * obj := Constructor(words);
 * param_1 := obj.Query(letter);
 */