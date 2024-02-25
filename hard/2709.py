from typing import List

class UnionFind:
    def __init__(self, n: int) -> None:
        self.par = [i for i in range(n)]
        self.size = [1] * n
        self.count = n
    
    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        
        if px == py:
            return
    
        if self.size[px] < self.size[py]:
            self.par[px] = self.par[py]
            self.size[py] += self.size[px]
        else:
            self.par[py] = self.par[px]
            self.size[px] += self.size[py]
        
        self.count -= 1

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        uf = UnionFind(len(nums))
        factor_index = {}

        for i, n in enumerate(nums):
            f = 2
            while f * f <= n:
                if n % f == 0:
                    if f in factor_index:
                        uf.union(i, factor_index[f])
                    else:
                        factor_index[f] = i
                    while n % f == 0:
                        n = n // f
                f += 1
            if n > 1:
                if n in factor_index:
                    uf.union(i, factor_index[n])
                else:
                    factor_index[n] = i
        
        return uf.count == 1


    # def canTraverseAllPairs(self, nums: List[int]) -> bool:
    #     n = len(nums)
    #     graph = defaultdict(list)
    #     visited = set()

    #     for i in range(n):
    #         for j in range(i + 1, n):
    #             if gcd(nums[i], nums[j]) > 1:
    #                 graph[i].append(j)
    #                 graph[j].append(i)
        
    #     q = deque([0])

    #     while q:
    #         node = q.popleft()

    #         for next in graph[node]:
    #             if next not in visited:
    #                 q.append(next)
    #                 visited.add(next)
        
    #     return len(visited) == n

        
        
def main():
    sol = Solution()
    print(sol.canTraverseAllPairs([2,3,6]))
    print(sol.canTraverseAllPairs([3,9,5]))
    print(sol.canTraverseAllPairs([4,3,12,8]))

if __name__ == '__main__':
    main()