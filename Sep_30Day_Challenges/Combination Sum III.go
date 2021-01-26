func getCombination(sum int, k int, start int) [][]int{
    res := [][]int{}
    if k== 1{
        if start == sum {
            res = append(res, []int{start})
            return res
        }
        return res
    }
    for i:=start+1;i<=9;i++ {
        tmp := getCombination(sum-start,k-1,i)
        for _, subarr := range tmp{
            subarr = append(subarr,start)
            res = append(res,subarr)
        }
    }
    return res
}
func combinationSum3(k int, n int) [][]int {
    res := [][]int{}
    for i:=1; i<=9-k+1;i++{
        tmp := getCombination(n,k,i)
        res = append(res,tmp...)
    }
    return res
}