class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        stack = []
        ans = 0
        for t in target:
            if not stack:
                stack.append(t)
                ans += t
            elif t < stack[-1]:
                stack.append(t)
            else:
                ans += t-stack[-1]
                stack.append(t)
        return ans