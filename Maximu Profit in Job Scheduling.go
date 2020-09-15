// We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

// You're given the startTime , endTime and profit arrays, you need to output the maximum profit you can take such that there are no 2 jobs in the subset with overlapping time range.

// If you choose a job that ends at time X you will be able to start another job that starts at time X.

 

// Example 1:



// Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
// Output: 120
// Explanation: The subset chosen is the first and fourth job. 
// Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.
// Example 2:




// Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
// Output: 150
// Explanation: The subset chosen is the first, fourth and fifth job. 
// Profit obtained 150 = 20 + 70 + 60.
// Example 3:



// Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
// Output: 6
 

// Constraints:

// 1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
// 1 <= startTime[i] < endTime[i] <= 10^9
// 1 <= profit[i] <= 10^4
import "sort"
type task struct {
    start, end, profit int
}

type byStart []task 

func (this byStart) Less(i,j int) bool{
    return this[i].start < this[j].start
}

func (this byStart) Len() int {
    return len(this)
}

func (this byStart) Swap(i,j int) {
    this[i], this[j] = this[j],this[i]
}

func (this byStart) searchStartAfter(target int) int{
    i,j:=0,len(this)-1
    for i<=j{
        //fmt.Println("ij",i,j)
        mid := i + (j-i)/2
        if this[mid].start < target {
            i = mid +1
        }else{
            j = mid - 1
        }
    }
    return i
}

func max(a,b int) (c int) {
    if a>b {
        c = a
    }else{
        c = b
    }
    return
}

func jobScheduling(startTime []int, endTime []int, profit []int) int {
    tasks := make([]task,len(endTime))
    for i:=0;i<len(endTime); i++{
        tasks[i] = task{startTime[i],endTime[i],profit[i]}
    }
    sortedTasks := byStart(tasks)
    sort.Sort(sortedTasks)
    //fmt.Println("Sorted Tasks",sortedTasks)
    profits := make([]int,len(tasks))
    profits[len(profits)-1] = sortedTasks[len(profits)-1].profit
    for j:=len(profits)-2; j>=0; j-- {
        curtask := sortedTasks[j]
        next_available_if_j_is_choosen := sortedTasks.searchStartAfter(curtask.end)
        next_profit := 0
        //fmt.Println(j,next_available_if_j_is_choosen)
        if next_available_if_j_is_choosen >= len(profits){
            next_profit = curtask.profit
        }else{
            next_profit = curtask.profit + profits[next_available_if_j_is_choosen]
        }
        profits[j] = max(profits[j+1],next_profit)
    }
    //fmt.Println("Profit",profits)
    return profits[0]
}