from typing import List
from collections import defaultdict
from math import log2

class LCA:
    def __init__(self, edges: List[List[int]], root: int = 1):
        self.n = len(edges) + 1
        self.m = int(log2(self.n)) + 2
        self.e = [[] for _ in range(self.n + 1)]
        self.d = [0] * (self.n + 1)
        self.f = [[0] * self.m for _ in range(self.n + 1)]

        for u, v in edges:
            self.e[u].append(v)
            self.e[v].append(u)
        
        self.dfs(root, 0)

        for i in range(1, self.m):
            for x in range(1, self.n + 1):
                self.f[x][i] = self.f[self.f[x][i - 1]][i - 1]
    
    def dfs(self, x: int, fa: int):
        self.f[x][0] = fa
        
        for y in self.e[x]:
            if y == fa:
                continue

            self.d[y] = self.d[x] + 1
            self.dfs(y, x)
    
    def lca(self, x: int, y: int) -> int:
        if self.d[x] > self.d[y]:
            x, y = y, x

        diff = self.d[y] - self.d[x]

        for i in range(self.m - 1, -1, -1):
            if diff & (1 << i):
                y = self.f[y][i]

        if x == y:
            return x
        
        for i in range(self.m - 1, -1, -1):
            if self.f[x][i] != self.f[y][i]:
                x = self.f[x][i]
                y = self.f[y][i]
        
        return self.f[x][0]

    def dis(self, x: int, y: int) -> int:
        return self.d[x] + self.d[y] - self.d[self.lca(x, y)] * 2

MOD = 1_000_000_007
N = 100010
p2 = [0] * N

def init():
    p2[0] = 1

    for i in range(1, N):
        p2[i] = p2[i - 1] * 2 % MOD

init()

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        lca = LCA(edges, 1)
        m = len(queries)
        res = [0] * m

        for i in range(m):
            x, y = queries[i]
            if x != y:
                res[i] = p2[lca.dis(x, y) - 1]
        
        return res
        
def main():
    sol = Solution()
    print(sol.assignEdgeWeights(edges = [[1,2]], queries = [[1,1],[1,2]]))
    print(sol.assignEdgeWeights(edges = [[1,2],[1,3],[3,4],[3,5]], queries = [[1,4],[3,4],[2,5]]))

if __name__ == '__main__':
    main()