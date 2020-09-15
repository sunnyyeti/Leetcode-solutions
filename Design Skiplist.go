// Design a Skiplist without using any built-in libraries.

// A Skiplist is a data structure that takes O(log(n)) time to add, erase and search. Comparing with treap and red-black tree which has the same function and performance, the code length of Skiplist can be comparatively short and the idea behind Skiplists are just simple linked lists.

// For example: we have a Skiplist containing [30,40,50,60,70,90] and we want to add 80 and 45 into it. The Skiplist works this way:

// Artyom Kalinin [CC BY-SA 3.0], via Wikimedia Commons

// You can see there are many layers in the Skiplist. Each layer is a sorted linked list. With the help of the top layers, add , erase and search can be faster than O(n). It can be proven that the average time complexity for each operation is O(log(n)) and space complexity is O(n).

// To be specific, your design should include these functions:

// bool search(int target) : Return whether the target exists in the Skiplist or not.
// void add(int num): Insert a value into the SkipList.
// bool erase(int num): Remove a value in the Skiplist. If num does not exist in the Skiplist, do nothing and return false. If there exists multiple num values, removing any one of them is fine.
// See more about Skiplist : https://en.wikipedia.org/wiki/Skip_list

// Note that duplicates may exist in the Skiplist, your code needs to handle this situation.

// Example:

// Skiplist skiplist = new Skiplist();

// skiplist.add(1);
// skiplist.add(2);
// skiplist.add(3);
// skiplist.search(0);   // return false.
// skiplist.add(4);
// skiplist.search(1);   // return true.
// skiplist.erase(0);    // return false, 0 is not in skiplist.
// skiplist.erase(1);    // return true.
// skiplist.search(1);   // return false, 1 has already been erased.

// Constraints:

// 0 <= num, target <= 20000
// At most 50000 calls will be made to search, add, and erase.
// Accepted
import (
	"fmt"
	"math/rand"
)

type Node struct {
	val   int
	nexts []*Node
	//prevs []*Node
}

type Skiplist struct {
	head  *Node
	level int
}

func Constructor() Skiplist {
	header := &Node{-1, []*Node{nil}}
	//rand.Seed(5)
	return Skiplist{head: header, level: 0}
}

func (this *Skiplist) Search(target int) bool {
	//fmt.Println("Search",target)
	curlevel := this.level
	curnode := this.head
	for curlevel > -1 {
		for curnode.nexts[curlevel] != nil && curnode.nexts[curlevel].val < target {
			curnode = curnode.nexts[curlevel]
		}
		if curnode.nexts[curlevel] != nil && curnode.nexts[curlevel].val == target {
			return true
		} else {
			curlevel--
		}
	}
	return false
}

func (this *Skiplist) display() {
	//fmt.Println("total level",this.level)
	for i := 0; i <= this.level; i++ {
		//fmt.Println("level",i)
		s := ""
		curnode := this.head
		for curnode.nexts[i] != nil {
			curnode = curnode.nexts[i]
			s += fmt.Sprintf("->%d", curnode.val)
		}
		fmt.Println(s)
	}
}

func (this *Skiplist) Add(num int) {
	stack := []*Node{}
	curlevel := this.level
	curnode := this.head
	for {
		for curnode.nexts[curlevel] != nil && curnode.nexts[curlevel].val < num {
			curnode = curnode.nexts[curlevel]
		}
		stack = append(stack, curnode)
		if curlevel == 0 {
			break
		} else {
			curlevel--
		}
	}
	newNode := &Node{val: num, nexts: []*Node{}}
	for curlevel == 0 || rand.Intn(2) == 1 {
		if len(stack) > 0 {
			curnode = stack[len(stack)-1]
			stack = stack[:len(stack)-1]
		}
		if curlevel <= this.level {
			newNode.nexts = append(newNode.nexts, curnode.nexts[curlevel])
			curnode.nexts[curlevel] = newNode
		} else {
			curnode = this.head
			curnode.nexts = append(curnode.nexts, newNode)
			newNode.nexts = append(newNode.nexts, nil)
		}
		curlevel++
	}
	curlevel--
	if curlevel > this.level {
		this.level = curlevel
	}
}

func (this *Skiplist) Erase(num int) bool {
	curlevel := this.level
	curnode := this.head
	has_found := false
	var found *Node
	for curlevel > -1 {
		if !has_found {
			for curnode.nexts[curlevel] != nil && curnode.nexts[curlevel].val < num {
				curnode = curnode.nexts[curlevel]
			}
			if curnode.nexts[curlevel] != nil && curnode.nexts[curlevel].val == num {
				found = curnode.nexts[curlevel]
				has_found = true
				curnode.nexts[curlevel] = found.nexts[curlevel]
			}
		} else {
			for curnode.nexts[curlevel] != found {
				curnode = curnode.nexts[curlevel]
			}
			curnode.nexts[curlevel] = found.nexts[curlevel]
		}

		curlevel--

	}
	return has_found
}

/**
 * Your Skiplist object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Search(target);
 * obj.Add(num);
 * param_3 := obj.Erase(num);
 */

/**
 * Your Skiplist object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Search(target);
 * obj.Add(num);
 * param_3 := obj.Erase(num);
 */