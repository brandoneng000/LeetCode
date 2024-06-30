from typing import List

class UF:
    def __init__(self, n) -> None:
        self.n = n
        self.par = [i for i in range(n + 1)]
        self.rank = [1] * (n + 1)
    
    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x

    def union(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)

        if p1 == p2:
            return 0
        if self.rank[p1] > self.rank[p2]:
            self.rank[p1] += self.rank[p2]
            self.par[p2] = p1
        else:
            self.rank[p2] += self.rank[p2]
            self.par[p1] = p2
        self.n -= 1
        return 1
    
    def is_connected(self):
        return self.n <= 1

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice, bob = UF(n), UF(n)
        count = 0

        for t, u, v in edges:
            if t == 3:
                count += (alice.union(u, v) | bob.union(u, v))
        
        for t, u, v in edges:
            if t == 1:
                count += alice.union(u, v)
            elif t == 2:
                count += bob.union(u, v)
        
        return len(edges) - count if bob.is_connected() and alice.is_connected() else -1


        
def main():
    sol = Solution()
    print(sol.maxNumEdgesToRemove(n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]))
    print(sol.maxNumEdgesToRemove(n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]))
    print(sol.maxNumEdgesToRemove(n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]))

if __name__ == '__main__':
    main()