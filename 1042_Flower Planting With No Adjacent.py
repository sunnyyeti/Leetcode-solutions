class Solution(object):
    def gardenNoAdj(self, N, paths):
        """
        :type N: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        self.nbs = {}
        for s, t in paths:
            self.nbs.setdefault(s, set()).add(t)
            self.nbs.setdefault(t, set()).add(s)
        self.ans = [-1] * N
        self.cands = {i: set([1, 2, 3, 4]) for i in range(1, N + 1)}
        for i in range(1, N + 1):
            if self.ans[i - 1] == -1:
                self.search_success(i)
        return self.ans

    def search_success(self, garden):
        cands = self.cands[garden]
        if len(cands)==0:
            return False
        for can in cands:
            self.ans[garden - 1] = can
            store = []
            nbs = [nb for nb in self.nbs.get(garden, set()) if self.ans[nb-1]==-1]
            for nb in nbs:
                if can in self.cands[nb]:
                    self.cands[nb].remove(can)
                    store.append(nb)
            if not nbs:
                return True
            for nb in nbs:
                if not self.search_success(nb):
                    for nb in store:
                        self.cands[nb].add(can)
                    break
            else:
                return True
        return False


if __name__=="__main__":
    print(Solution().gardenNoAdj(4, [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]))