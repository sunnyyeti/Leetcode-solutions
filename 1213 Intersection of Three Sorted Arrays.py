# Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a sorted array of only the integers that appeared in all three arrays.

 

# Example 1:

# Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
# Output: [1,5]
# Explanation: Only 1 and 5 appeared in the three arrays.
# Example 2:

# Input: arr1 = [197,418,523,876,1356], arr2 = [501,880,1593,1710,1870], arr3 = [521,682,1337,1395,1764]
# Output: []
 

# Constraints:

# 1 <= arr1.length, arr2.length, arr3.length <= 1000
# 1 <= arr1[i], arr2[i], arr3[i] <= 2000
class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        i = j = k = 0
        ans = []
        while i < len(arr1) and j < len(arr2) and k < len(arr3):
            v1, v2, v3 = arr1[i], arr2[j], arr3[k]
            if v1 == v2 == v3:
                ans.append(v1)
                i, j, k = i+1, j+1, k+1
            else:
                inds = [i, j, k]
                arrs = [arr1, arr2, arr3]
                max_ind = max(range(3), key=lambda x: arrs[x][inds[x]])
                for ind in range(3):
                    if ind != max_ind:
                        if arrs[ind][inds[ind]] != arrs[max_ind][inds[max_ind]]:
                            inds[ind] += 1
                i, j, k = inds
        return ans
