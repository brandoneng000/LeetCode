from typing import List

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        n, m = len(grid), len(grid[0])
        res = 0

        def helper(cur_r: int, cur_c: int, cur_gold: int, visited: set):
            max_gold = cur_gold + grid[cur_r][cur_c]
            visited.add((cur_r, cur_c))
            for dr, dc in directions:
                r = cur_r + dr
                c = cur_c + dc
                if 0 <= r < n and 0 <= c < m and grid[r][c] != 0 and (r, c) not in visited:
                    max_gold = max(max_gold, helper(r, c, cur_gold + grid[cur_r][cur_c], visited))
            
            visited.remove((cur_r, cur_c))

            return max_gold
        
        for i in range(n):
            for j in range(m):
                res = max(res, helper(i, j, 0, set()))
        
        return res

def main():
    sol = Solution()
    print(sol.getMaximumGold([[1,0,7,0,0,0],
                              [2,0,6,0,1,0],
                              [3,5,6,7,4,2],
                              [4,3,1,0,2,0],
                              [3,0,5,0,20,0]]))
    print(sol.getMaximumGold([[0,6,0],[5,8,7],[0,9,0]]))
    print(sol.getMaximumGold([[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]))

if __name__ == '__main__':
    main()