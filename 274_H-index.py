# Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

# According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

# Example:

# Input: citations = [3,0,6,1,5]
# Output: 3 
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had 
#              received 3, 0, 6, 1, 5 citations respectively. 
#              Since the researcher has 3 papers with at least 3 citations each and the remaining 
#              two with no more than 3 citations each, her h-index is 3.
# Note: If there are several possible values for h, the maximum one is taken as the h-index.
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        citations.sort(reverse=True)
        for i,c in enumerate(citations):
            if i+1>=c:
                break
        else:
            return len(citations)
        if i+1==c:
            return c
        # if i==c: #i+1>c
        #     return c
        return i #前面的citation是大于个数；而如果i+1!=c,就是i+1>c,所以c是小于个数的，从c<i+1，那么必然c<=i，从而后面的c也都小于i，前面个数也满足，正好i个，后面也满足
        
# 60 50 40 1 0
# 6 5 4 1 0
# 6 5 2 1 0
# 100 90 80
