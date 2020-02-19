# Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

# Note:
# The number of people is less than 1,100.

 
# Example

# Input:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

# Output:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        if not people:
            return people
        people.sort()
        ans = []
        max_h  = people[-1][0]
        end = len(people)
        for i in reversed(range(len(people))):
            if people[i][0]<max_h:
                for j in range(i+1,end):
                    ans.insert(people[j][1],people[j])
                max_h = people[i][0]
                end = i+1
        for j in range(end):
            ans.insert(people[j][1],people[j])
        return ans