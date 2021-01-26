// Design a data structure that supports the following two operations:

// void addWord(word)
// bool search(word)
// search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

// Example:

// addWord("bad")
// addWord("dad")
// addWord("mad")
// search("pad") -> false
// search("bad") -> true
// search(".ad") -> true
// search("b..") -> true
// Note:
// You may assume that all words are consist of lowercase letters a-z.
type Node struct {
    end bool
    children map[byte]*Node
}

type WordDictionary struct {
    root *Node
}


/** Initialize your data structure here. */
func Constructor() WordDictionary {
    root := &Node{end:false,children:make(map[byte]*Node)}
    return WordDictionary{root}
}


/** Adds a word into the data structure. */
func (this *WordDictionary) AddWord(word string)  {
    root := this.root
    for i:=0; i<len(word); i++ {
        curchar := word[i]
        if _,ok:=root.children[curchar];!ok{
            root.children[curchar] = &Node{end:false,children:make(map[byte]*Node)}
            root = root.children[curchar]
        }else{
            root = root.children[curchar]
        }
    }
    root.end = true
}


/** Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. */
func (this *WordDictionary) Search(word string) bool {
    roots := []*Node{this.root}
    for i:=0;i<len(word);i++{
        curchar := word[i]
        nextroots := make([]*Node,0)
        for _, r := range roots {
            if curchar=='.' {
                for _, nr := range r.children {
                    nextroots = append(nextroots,nr)
                }
            }else if _,ok:=r.children[curchar];ok{
                nextroots = append(nextroots,r.children[curchar])
            }
        }
        roots = nextroots
        if len(roots)==0 {return false}
    }
    for _,r:=range roots{
        if r.end {
            return true
        }
    }
    return false
}


type StackEle struct {
    node *Node
    word string
}
func (this *WordDictionary) Search(word string) bool {
    stack := []StackEle{StackEle{this.root,word}}
    for len(stack)>0 {
        curele := stack[len(stack)-1]
        stack = stack[:len(stack)-1]
        curnode := curele.node
        curword := curele.word
        if len(curword)==0 && curnode.end {
            return true
        }else if len(curword)>0{
            curchar := curword[0]
            if curchar=='.'{
                for _,r := range curnode.children{
                    stack = append(stack,StackEle{r,curword[1:]})
                }
            }else if v,ok:=curnode.children[curchar];ok{
                stack = append(stack,StackEle{v,curword[1:]})
            }
        }  
    }
    return false
}


/**
 * Your WordDictionary object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddWord(word);
 * param_2 := obj.Search(word);
 */