
// There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].

// Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

 

// Example 1:

// Input: [[10,20],[30,200],[400,50],[30,20]]
// Output: 110
// Explanation: 
// The first person goes to city A for a cost of 10.
// The second person goes to city A for a cost of 30.
// The third person goes to city B for a cost of 50.
// The fourth person goes to city B for a cost of 20.

// The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
 

// Note:

// 1 <= costs.length <= 100
// It is guaranteed that costs.length is even.
// 1 <= costs[i][0], costs[i][1] <= 1000
import "sort"
func sumCostsForCity(city [][]int, costInd int) int{
    sum:=0
    for _,c := range city{
        sum += c[costInd]
    }
    return sum
}
type costSliceWrapper struct{
    costSlice [][]int
    cmp func(a, b []int) bool
}

func (csw costSliceWrapper) Len() int{
    return len(csw.costSlice)
}
func (csw costSliceWrapper) Less(i,j int) bool{
    return csw.cmp(csw.costSlice[i],csw.costSlice[j])
}
func (csw costSliceWrapper) Swap(i,j int){
    csw.costSlice[i],csw.costSlice[j] = csw.costSlice[j],csw.costSlice[i]
}

func twoCitySchedCost(costs [][]int) int {
    cityA := make([][]int,0)
    cityB := make([][]int,0)
    for _,p:=range costs{
        if p[0]<p[1]{
            cityA = append(cityA,p)
        }else{
            cityB = append(cityB,p)
        }
    }
    //fmt.Println(cityA,cityB)
    if len(cityA)==len(cityB){
        return sumCostsForCity(cityA,0)+sumCostsForCity(cityB,1)
    }else if len(cityA)>len(cityB){
        sort.Sort(costSliceWrapper{cityA,func (a,b []int) bool {return a[1]-a[0]<b[1]-b[0]}})
        //fmt.Println(cityA,cityB)
        move := (len(cityA)-len(cityB))/2
        cityB = append(cityB,cityA[:move]...)
        cityA = cityA[move:]
        return sumCostsForCity(cityA,0)+sumCostsForCity(cityB,1)
    }else{
        //fmt.Print("B")
        sort.Sort(costSliceWrapper{cityB,func (a,b []int) bool {return a[0]-a[1]<b[0]-b[1]}})
        //fmt.Println(cityA,cityB)
        move:=(len(cityB)-len(cityA))/2
        cityA = append(cityA,cityB[:move]...)
        //fmt.Println(cityA,cityB)
        cityB = cityB[move:]
        //fmt.Println(cityA,cityB)
        return sumCostsForCity(cityA,0)+sumCostsForCity(cityB,1)
    }
}