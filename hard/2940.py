from typing import List
from collections import defaultdict

class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        def helper(height: int, stack: List[int]):
            left = 0
            right = len(stack) - 1
            res = -1

            while left <= right:
                middle = (left + right) // 2

                if stack[middle][0] > height:
                    res = max(res, middle)
                    left = middle + 1
                else:
                    right = middle - 1
            
            return res


        n, m = len(heights), len(queries)
        res = [-1] * m
        stack = []
        new_query = [[] for _ in range(n)]
        
        for i in range(m):
            alice = queries[i][0]
            bob = queries[i][1]

            if alice > bob:
                alice, bob = bob, alice
            
            if heights[bob] > heights[alice] or alice == bob:
                res[i] = bob
            else:
                new_query[bob].append([heights[alice], i])
        
        for i in range(n - 1, -1, -1):
            stack_size = len(stack)

            for a, b in new_query[i]:
                pos = helper(a, stack)

                if pos < stack_size and pos >= 0:
                    res[b] = stack[pos][1]
            
            while stack and stack[-1][0] <= heights[i]:
                stack.pop()
            
            stack.append([heights[i], i])

        return res


    # def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
    #     n = len(heights)
    #     m = len(queries)
    #     taller = {}
    #     res = [float('inf')] * m

    #     for i in range(n - 1, -1, -1):
    #         taller[i] = set([i])

    #         for j in range(i + 1, n):
    #             if heights[j] > heights[i]:
    #                 taller[i].add(j)
        
    #     for i, (alice, bob) in enumerate(queries):
    #         res[i] = min(taller[alice] & taller[bob] | {float('inf')})
        
    #     return res
        
def main():
    sol = Solution()
    print(sol.leftmostBuildingQueries(heights = [6,4,8,5,2,7], queries = [[0,1],[0,3],[2,4],[3,4],[2,2]]))
    print(sol.leftmostBuildingQueries(heights = [5,3,8,2,6,1,4,6], queries = [[0,7],[3,5],[5,2],[3,0],[1,6]]))

if __name__ == '__main__':
    main()