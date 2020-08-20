// Implement a SnapshotArray that supports the following interface:

// SnapshotArray(int length) initializes an array-like data structure with the given length.  Initially, each element equals 0.
// void set(index, val) sets the element at the given index to be equal to val.
// int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
// int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id
 

// Example 1:

// Input: ["SnapshotArray","set","snap","set","get"]
// [[3],[0,5],[],[0,6],[0,0]]
// Output: [null,null,0,null,5]
// Explanation: 
// SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
// snapshotArr.set(0,5);  // Set array[0] = 5
// snapshotArr.snap();  // Take a snapshot, return snap_id = 0
// snapshotArr.set(0,6);
// snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5
 

// Constraints:

// 1 <= length <= 50000
// At most 50000 calls will be made to set, snap, and get.
// 0 <= index < length
// 0 <= snap_id < (the total number of times we call snap())
// 0 <= val <= 10^9
type SnapshotArray struct {
    arr []map[int]int
    snapid int
}


func Constructor(length int) SnapshotArray {
    arr := make([]map[int]int,length)
    return SnapshotArray{arr,0}
}


func (this *SnapshotArray) Set(index int, val int)  {
    if this.arr[index] == nil {
        this.arr[index] = make(map[int]int)
    }
    this.arr[index][this.snapid] = val
}


func (this *SnapshotArray) Snap() int {
    tmp := this.snapid
    this.snapid++
    return tmp
}


func (this *SnapshotArray) Get(index int, snap_id int) int {
    dict := this.arr[index]
    if dict==nil{
        return 0
    }
    for {
        if _,ok := dict[snap_id]; !ok {
             snap_id--
            if snap_id<0 {
                return 0
            }
        }else{
             return dict[snap_id]
        }
      
    }
    
}


/**
 * Your SnapshotArray object will be instantiated and called as such:
 * obj := Constructor(length);
 * obj.Set(index,val);
 * param_2 := obj.Snap();
 * param_3 := obj.Get(index,snap_id);
 */