import "sort"
func threeSum(nums []int) [][]int {
    sort.Ints(nums)
    hash_map := make(map[int][]int)
    for ind,ele := range nums{
        if inds,ok:=hash_map[ele];ok{
            inds = append(inds,ind)
            hash_map[ele] = inds
        }else{
            hash_map[ele] = []int{ind}
        }
    }
    var ans [][]int
    first := int((^uint(0))>>1)
    second := first
    for i:=0;i<len(nums)-2;i++{
        if nums[i]!=first{
            first = nums[i]
            for j:=i+1;j<len(nums)-1;j++{
                if nums[j]!=second{
                    second = nums[j]
                    target := -first-second
                    if hash_map[target]!=nil{
                        target_inds := hash_map[target]
                        if target_inds[len(target_inds)-1]>j{
                            ans = append(ans,[]int{first,second,target})
                        }
                    }
                }
            }
        }
    }
    return ans
    
    
}