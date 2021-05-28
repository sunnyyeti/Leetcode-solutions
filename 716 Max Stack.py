# Design a max stack data structure that supports the stack operations and supports finding the stack's maximum element.

# Implement the MaxStack class:

# MaxStack() Initializes the stack object.
# void push(int x) Pushes element x onto the stack.
# int pop() Removes the element on top of the stack and returns it.
# int top() Gets the element on the top of the stack without removing it.
# int peekMax() Retrieves the maximum element in the stack without removing it.
# int popMax() Retrieves the maximum element in the stack and removes it. If there is more than one maximum element, only remove the top-most one.
 

# Example 1:

# Input
# ["MaxStack", "push", "push", "push", "top", "popMax", "top", "peekMax", "pop", "top"]
# [[], [5], [1], [5], [], [], [], [], [], []]
# Output
# [null, null, null, null, 5, 5, 1, 5, 1, 5]

# Explanation
# MaxStack stk = new MaxStack();
# stk.push(5);   // [5] the top of the stack and the maximum number is 5.
# stk.push(1);   // [5, 1] the top of the stack is 1, but the maximum is 5.
# stk.push(5);   // [5, 1, 5] the top of the stack is 5, which is also the maximum, because it is the top most one.
# stk.top();     // return 5, [5, 1, 5] the stack did not change.
# stk.popMax();  // return 5, [5, 1] the stack is changed now, and the top is different from the max.
# stk.top();     // return 1, [5, 1] the stack did not change.
# stk.peekMax(); // return 5, [5, 1] the stack did not change.
# stk.pop();     // return 1, [5] the top of the stack and the max element is now 5.
# stk.top();     // return 5, [5] the stack did not change.
 

# Constraints:

# -107 <= x <= 107
# At most 104 calls will be made to push, pop, top, peekMax, and popMax.
# There will be at least one element in the stack when pop, top, peekMax, or popMax is called.
 

# Follow up: Could you come up with a solution that supports O(1) for each top call and O(logn) for each other call? 
from sortedcontainers import SortedDict
class Node:
    def __init__(self,val,prev_=None,next_=None):
        self.val = val
        self.prev_ = prev_
        self.next_ = next_
        
class DLL:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next_ = self.tail
        self.tail.prev_ = self.head
    
    def append(self,node):
        last = self.tail.prev_
        last.next_ = node
        self.tail.prev_ = node
        node.next_ = self.tail
        node.prev_ = last
        
    def remove(self,node):
        prev_ = node.prev_
        next_ = node.next_
        prev_.next_,next_.prev_ = next_,prev_
        
class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.dict = SortedDict()
        self.stack = DLL()
    
    def push(self, x: int) -> None:
        tmp_node = Node(x)
        self.stack.append(tmp_node)
        self.dict.setdefault(x,[]).append(tmp_node)        
        
    def pop(self) -> int:
        last_node = self.stack.tail.prev_
        self.stack.remove(last_node)
        self.dict[last_node.val].pop()
        if len(self.dict[last_node.val])==0:
            del self.dict[last_node.val]
        return last_node.val
        
    def top(self) -> int:
        return self.stack.tail.prev_.val

    def peekMax(self) -> int:
        return self.dict.peekitem(-1)[0]

    def popMax(self) -> int:
        tmp_node = self.dict.peekitem(-1)[1].pop()
        if len(self.dict[tmp_node.val])==0:
            del self.dict[tmp_node.val]
        self.stack.remove(tmp_node)
        return tmp_node.val


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()