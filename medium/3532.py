from typing import List

# class UnionFind:
#     def __init__(self, size: int):
#         self.parent = list(range(size))
    
#     def find(self, i: int):
#         if self.parent[i] == i:
#             return i
        
#         return self.find(self.parent[i])

#     def unite(self, i: int, j: int):
#         u = self.find(i)
#         v = self.find(j)

#         self.parent[u] = v

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        component = [0] * n
        comp = 0
        res = []

        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                comp += 1

            component[i] = comp

        for a, b in queries:
            res.append(component[a] == component[b])
        
        return res

    # def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
    #     union = UnionFind(n)
    #     res = []

    #     for i in range(n):
    #         for j in range(n):
    #             diff = abs(nums[i] - nums[j])

    #             if diff <= maxDiff:
    #                 union.unite(i, j)
                
    #             if diff > maxDiff and nums[i] < nums[j]:
    #                 break
        
    #     for a, b in queries:
    #         res.append(union.find(a) == union.find(b))
        
    #     return res
        
def main():
    sol = Solution()
    print(sol.pathExistenceQueries(n = 2, nums = [1,3], maxDiff = 1, queries = [[0,0],[0,1]]))
    print(sol.pathExistenceQueries(n = 4, nums = [2,5,6,8], maxDiff = 2, queries = [[0,1],[0,2],[1,3],[2,3]]))

if __name__ == '__main__':
    main()