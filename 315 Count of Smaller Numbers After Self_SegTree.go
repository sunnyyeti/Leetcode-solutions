// You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

 

// Example 1:

// Input: nums = [5,2,6,1]
// Output: [2,1,1,0]
// Explanation:
// To the right of 5 there are 2 smaller elements (2 and 1).
// To the right of 2 there is only 1 smaller element (1).
// To the right of 6 there is 1 smaller element (1).
// To the right of 1 there is 0 smaller element.
 

// Constraints:

// 0 <= nums.length <= 10^5
// -10^4 <= nums[i] <= 10^4
import "math"
func countSmaller(nums []int) []int {
    if len(nums)==0{
        return nums
    }
    length := 20000+1
    height := int(math.Ceil(math.Log2(float64(length))))
    tree := make([]int,int(math.Pow(2,float64(height+1))-1))
    ans := make([]int, len(nums))
    for i:=len(nums)-1;i>-1;i--{
        curele := nums[i]
        ind := curele-(-10000)
        ans[i] =  getSum(tree,0,0,length-1,0,ind-1)
        updateValue(tree,0,0,length-1,ind,1)
    }
    return ans
    
}

func constructSegTree(arr []int, tree []int, treeind, ss, se int) int{
    if ss==se {
        tree[treeind] = arr[ss]
        return arr[ss]
    }
    mid := ss+(se-ss)/2
    left := constructSegTree(arr, tree, 2*treeind+1, ss, mid)
    right := constructSegTree(arr, tree, 2*treeind+2, mid+1,se)
    tree[treeind] = left+right
    return tree[treeind]
}

func getSum(tree []int, treeind, ss, se, qs, qe int) int{
    if qs<=ss && qe>=se {
        return tree[treeind]
    }else if qs>se || qe<ss{
        return 0
    }else{
        mid := ss+(se-ss)/2
        return getSum(tree,treeind*2+1,ss,mid,qs,qe)+getSum(tree,treeind*2+2,mid+1,se,qs,qe)
    }
}

func updateValue(tree []int, treeind, ss,se, ind, delta int){
    if ss<=ind && ind<=se {
        tree[treeind]+=delta
        if ss!=se {
            mid := ss+(se-ss)/2
            updateValue(tree, treeind*2+1,ss,mid,ind,delta)
            updateValue(tree,treeind*2+2, mid+1,se,ind,delta)  
        }
    }else {
        return
    }
}

