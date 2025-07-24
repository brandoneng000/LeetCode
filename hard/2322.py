from typing import List
from collections import defaultdict

class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        def calc(part1:int, part2: int, part3: int):
            return max(part1, part2, part3) - min(part1, part2, part3)
        
        def dfs(x: int, f: int) -> int:
            son = nums[x]

            for y in graph[x]:
                if y == f:
                    continue
                son ^= dfs(y, x)

            for y in graph[x]:
                if y == f:
                    dfs2(y, x, son, x)
            
            return son
        
        def dfs2(x: int, f: int, oth: int, anc: int):
            son = nums[x]

            for y in graph[x]:
                if y == f:
                    continue
                son ^= dfs2(y, x, oth, anc)
            
            if f == anc:
                return son
            nonlocal res
            res = min(res, calc(oth, son, total ^ oth ^ son))
            return son

        n = len(nums)
        graph = defaultdict(list)
        res = float('inf')

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        total = 0
        for num in nums:
            total ^= num
        
        dfs(0, -1)
        return res
        

def main():
    sol = Solution()
    print(sol.minimumScore(nums = [1,5,5,4,11], edges = [[0,1],[1,2],[1,3],[3,4]]))
    print(sol.minimumScore(nums = [5,5,2,4,4,2], edges = [[0,1],[1,2],[5,2],[4,3],[1,3]]))

if __name__ == '__main__':
    main()