from typing import List

class BIT:
    def __init__(self, n: int):
        self.n = n
        self.tree = [0] * (n + 1)

    @staticmethod
    def lowbit(x: int) -> int:
        return x & -x

    def update(self, x: int, v: int) -> None:
        while x <= self.n:
            self.tree[x] ^= v
            x += BIT.lowbit(x)

    def query(self, x: int) -> int:
        ret = 0

        while x:
            ret ^= self.tree[x]
            x -= BIT.lowbit(x)

        return ret

    def updateRange(self, l: int, r: int, v: int) -> None:
        self.update(l, v)
        self.update(r + 1, v)

class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        def dfs(u: int, p: int) -> None:
            nonlocal timer
            timer += 1
            l[u] = timer
            fa[u][0] = p

            for v in g[u]:
                if v == p:
                    continue
                dep[v] = dep[u] + 1
                dfs(v, u)
            r[u] = timer

        def lca(u: int, v: int) -> int:
            if dep[u] < dep[v]:
                u, v = v, u

            diff  = dep[u] - dep[v]

            for i in range(LOG):
                if (diff >> i) & 1:
                    u = fa[u][i]
            if u == v:
                return u

            for i in range(LOG - 1, -1, -1):
                if fa[u][i] != fa[v][i]:
                    u = fa[u][i]
                    v = fa[v][i]

            return fa[u][0]


        g = [[] for _ in range(n)]

        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        LOG = n.bit_length()
        fa = [[0] * LOG for _ in range(n)]
        dep = [0] * n
        l = [0] * n
        r = [0] * n
        timer = 0

        dfs(0, 0)

        for j in range(1, LOG):
            for i in range(n):
                fa[i][j] = fa[fa[i][j - 1]][j - 1]

        bit = BIT(n + 1)
        s = list(s)

        for i in range(n):
            bit.updateRange(l[i], r[i], 1 << (ord(s[i]) - ord('a')))

        res = []

        for q in queries:
            op, *rest = q.split()

            if op == "update":
                u, c = int(rest[0]), rest[1]
                bit.updateRange(
                    l[u],
                    r[u],
                    (1 << (ord(s[u]) - ord('a'))) ^ (1 << (ord(c) - ord('a'))),
                )
                s[u] = c
            else:
                u, v = int(rest[0]), int(rest[1])
                w = lca(u, v)
                mask = (
                    bit.query(l[u])
                    ^ bit.query(l[v])
                    ^ (1 << (ord(s[w]) - ord('a')))
                )
                res.append(mask.bit_count() <= 1)

        return res



def main():
    sol = Solution()
    print(sol.palindromePath(n = 3, edges = [[0,1],[1,2]], s = "aac", queries = ["query 0 2","update 1 b","query 0 2"]))
    print(sol.palindromePath(n = 4, edges = [[0,1],[0,2],[0,3]], s = "abca", queries = ["query 1 2","update 0 b","query 2 3","update 3 a","query 1 3"]))

if __name__ == '__main__':
    main()