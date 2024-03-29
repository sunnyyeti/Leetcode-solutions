# We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

# You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

# If you choose a job that ends at time X you will be able to start another job that starts at time X.

 

# Example 1:



# Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
# Output: 120
# Explanation: The subset chosen is the first and fourth job. 
# Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.
# Example 2:



# Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
# Output: 150
# Explanation: The subset chosen is the first, fourth and fifth job. 
# Profit obtained 150 = 20 + 70 + 60.
# Example 3:



# Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
# Output: 6
 

# Constraints:

# 1 <= startTime.length == endTime.length == profit.length <= 5 * 104
# 1 <= startTime[i] < endTime[i] <= 109
# 1 <= profit[i] <= 104
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = [(s, e, p) for s, e, p in zip(startTime, endTime, profit)]
        jobs.sort()
        profits = [0]*len(jobs)
        profits[-1] = jobs[-1][-1]
        max_profit = profits[-1]
        for i in range(len(jobs)-2, -1, -1):
            job_s, job_e, job_p = jobs[i]
            left, right = i+1, len(jobs)-1
            while left <= right:
                mid = (left+right)//2
                mid_s = jobs[mid][0]
                if mid_s >= job_e:
                    right = mid-1
                else:
                    left = mid+1
            if left == len(jobs):
                profits[i] = max(job_p, profits[i+1])
            else:
                profits[i] = max(job_p+profits[left], profits[i+1])
            max_profit = max(max_profit, profits[i])
        return max_profit
