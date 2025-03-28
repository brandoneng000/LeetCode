from typing import List
from collections import deque

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        size = len(queries)
        res = [0] * size
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        prev_query = -1
        prev_index = -1
        
        visited = set()
        q = deque([(0, 0)])
        visited.add((0, 0))
        ignored = deque([])

        for query, index in sorted((query, index) for index, query in enumerate(queries)):
            res[index] = res[prev_index]

            if query == prev_query:
                continue

            while q:
                row, col = q.popleft()

                if query > grid[row][col]:
                    res[index] += 1

                    for dr, dc in directions:
                        r = row + dr
                        c = col + dc
                    
                        if 0 <= r < m and 0 <= c < n and (r, c) not in visited:
                            q.append((r, c))
                            visited.add((r, c))
                else:
                    ignored.append((row, col))
            
            q = ignored
            ignored = deque()
            prev_index = index
            prev_query = query
        
        return res

        
def main():
    sol = Solution()
    print(sol.maxPoints(grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,6]))
    print(sol.maxPoints(grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,2]))
    print(sol.maxPoints(grid = [[5,2,1],[1,1,2]], queries = [3]))

if __name__ == '__main__':
    main()