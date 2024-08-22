from typing import List

class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        def get_string(grid: List[List[int]]):
            res = []

            for i in range(3):
                for j in range(3):
                    res.append(str(grid[i][j]))

            return ''.join(res)

        def dfs(grid: List[List[int]]):
            grid_str = get_string(grid)
            
            if grid_str in cache:
                return cache[grid_str]

            if all(grid[i][j] == 1 for i in range(3) for j in range(3)):
                cache[grid_str] = 0
                return cache[grid_str]
            
            res = 10000

            for i in range(3):
                for j in range(3):
                    if grid[i][j] == 0:
                        for u in range(3):
                            for v in range(3):
                                if grid[u][v] > 1:
                                    grid[i][j] += 1
                                    grid[u][v] -= 1
                                    dist = abs(i - u) + abs(j - v)
                                    res = min(res, dist + dfs(grid))
                                    grid[i][j] -= 1
                                    grid[u][v] += 1
            
            cache[grid_str] = res
            return cache[grid_str]
        
        cache = {}

        return dfs(grid)
        
def main():
    sol = Solution()
    print(sol.minimumMoves([[1,1,0],[1,1,1],[1,2,1]]))
    print(sol.minimumMoves([[1,3,0],[1,0,0],[1,0,3]]))
    print(sol.minimumMoves([[1,1,1],[1,1,1],[1,1,1]]))

if __name__ == '__main__':
    main()