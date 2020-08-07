// Design a HashSet without using any built-in hash table libraries.

// To be specific, your design should include these functions:

// add(value): Insert a value into the HashSet. 
// contains(value) : Return whether the value exists in the HashSet or not.
// remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.

// Example:

// MyHashSet hashSet = new MyHashSet();
// hashSet.add(1);         
// hashSet.add(2);         
// hashSet.contains(1);    // returns true
// hashSet.contains(3);    // returns false (not found)
// hashSet.add(2);          
// hashSet.contains(2);    // returns true
// hashSet.remove(2);          
// hashSet.contains(2);    // returns false (already removed)

// Note:

// All values will be in the range of [0, 1000000].
// The number of operations will be in the range of [1, 10000].
// Please do not use the built-in HashSet library.
type MyHashSet struct {
    store [997][]int
}


/** Initialize your data structure here. */
func Constructor() MyHashSet {
    var hs MyHashSet
    for i:=0;i<len(hs.store);i++{
        hs.store[i] = make([]int,0)
    }
    return hs
}


func (this *MyHashSet) Add(key int)  {
    if this.Contains(key){
        return
    }
    ind := key%len(this.store)
    this.store[ind] = append(this.store[ind],key)
}


func (this *MyHashSet) Remove(key int)  {
    ind := key%len(this.store)
    slice:=this.store[ind]
    for i:=0;i<len(slice);i++{
        if slice[i]==key{
            this.store[ind] = append(slice[:i],slice[i+1:]...)
            return
        }
    }
}


/** Returns true if this set contains the specified element */
func (this *MyHashSet) Contains(key int) bool {
    ind := key % len(this.store)
    slice := this.store[ind]
    for i:=0;i<len(slice);i++{
        if slice[i]==key{
            return true
        }
    }
    return false
}



/**
 * Your MyHashSet object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Add(key);
 * obj.Remove(key);
 * param_3 := obj.Contains(key);
 */