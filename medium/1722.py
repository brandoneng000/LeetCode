from typing import List
from collections import defaultdict, Counter

class UnionFind:
    def __init__(self, n: int) -> None:
        self.root = list(range(n))
    
    def union(self, x, y):
        self.root[self.find(x)] = self.find(y)
    
    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        
        return self.root[x]

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        uf = UnionFind(n)

        for i, j in allowedSwaps:
            uf.union(i, j)
        
        m = defaultdict(set)

        for i in range(n):
            m[uf.find(i)].add(i)
        
        res = 0

        for indexes in m.values():
            count_source = Counter(source[j] for j in indexes)
            count_target = Counter(target[j] for j in indexes)
            res += sum((count_source - count_target).values())
        
        return res


    # def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
    #     res = n = len(source)

    #     graph = defaultdict(set)

    #     for i, j in allowedSwaps:
    #         graph[i].add(j)
    #         graph[j].add(i)
        
    #     visited = [False] * n

    #     def dfs(i):
    #         visited[i] = True
    #         found.append(i)

    #         for j in graph[i]:
    #             if not visited[j]:
    #                 dfs(j)
        
    #     for i in range(n):
    #         if visited[i]:
    #             continue
    #         found = []
    #         dfs(i)
    #         count_source = Counter(source[j] for j in found)
    #         count_target = Counter(target[j] for j in found)
    #         res -= sum((count_source & count_target).values())
        
    #     return res
        
        
def main():
    sol = Solution()
    print(sol.minimumHammingDistance(source = [1,2,3,4], target = [2,1,4,5], allowedSwaps = [[0,1],[2,3]]))
    print(sol.minimumHammingDistance(source = [1,2,3,4], target = [1,3,2,4], allowedSwaps = []))
    print(sol.minimumHammingDistance([5,1,2,4,3], target = [1,5,4,2,3], allowedSwaps = [[0,4],[4,2],[1,3],[1,4]]))

if __name__ == '__main__':
    main()