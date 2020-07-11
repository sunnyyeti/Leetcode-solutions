// Design a data structure that supports all following operations in average O(1) time.

// insert(val): Inserts an item val to the set if not already present.
// remove(val): Removes an item val from the set if present.
// getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
// Example:

// // Init an empty set.
// RandomizedSet randomSet = new RandomizedSet();

// // Inserts 1 to the set. Returns true as 1 was inserted successfully.
// randomSet.insert(1);

// // Returns false as 2 does not exist in the set.
// randomSet.remove(2);

// // Inserts 2 to the set, returns true. Set now contains [1,2].
// randomSet.insert(2);

// // getRandom should return either 1 or 2 randomly.
// randomSet.getRandom();

// // Removes 1 from the set, returns true. Set now contains [2].
// randomSet.remove(1);

// // 2 was already in the set, so return false.
// randomSet.insert(2);

// // Since 2 is the only number in the set, getRandom always return 2.
// randomSet.getRandom();
import "math/rand"

type RandomizedSet struct {
	arr   []int
	table map[int]int
}

/** Initialize your data structure here. */
func Constructor() RandomizedSet {
	return RandomizedSet{arr: make([]int, 0), table: make(map[int]int)}
}

/** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
func (this *RandomizedSet) Insert(val int) bool {
	if _, ok := this.table[val]; !ok {
		this.arr = append(this.arr, val)
		this.table[val] = len(this.arr) - 1

		return true
	} else {

		return false
	}
}

/** Removes a value from the set. Returns true if the set contained the specified element. */
func (this *RandomizedSet) Remove(val int) bool {
	if ind, ok := this.table[val]; ok {
		delete(this.table, val)
		this.arr[ind], this.arr[len(this.arr)-1] = this.arr[len(this.arr)-1], this.arr[ind]
		this.arr = this.arr[:len(this.arr)-1]
		if ind < len(this.arr) {
			this.table[this.arr[ind]] = ind
		}

		return true
	} else {

		return false
	}
}

/** Get a random element from the set. */
func (this *RandomizedSet) GetRandom() int {
	ind := rand.Intn(len(this.arr))
	return this.arr[ind]
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Insert(val);
 * param_2 := obj.Remove(val);
 * param_3 := obj.GetRandom();
 */