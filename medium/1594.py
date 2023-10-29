from typing import List

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        mod = 1000000007
        m, n = len(grid), len(grid[0])
        largest = [[0] * n for _ in range(m)]
        smallest = [[0] * n for _ in range(m)]

        largest[0][0] = grid[0][0]
        smallest[0][0] = grid[0][0]

        for j in range(1, n):
            largest[0][j] = largest[0][j - 1] * grid[0][j]
            smallest[0][j] = smallest[0][j - 1] * grid[0][j] 

        for i in range(1, m):
            largest[i][0] = largest[i - 1][0] * grid[i][0]
            smallest[i][0] = smallest[i - 1][0] * grid[i][0]
        
        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] > 0:
                    largest[i][j] = max(largest[i - 1][j], largest[i][j - 1]) * grid[i][j]
                    smallest[i][j] = min(smallest[i - 1][j], smallest[i][j - 1]) * grid[i][j]
                else:
                    largest[i][j] = min(smallest[i - 1][j], smallest[i][j - 1]) * grid[i][j]
                    smallest[i][j] = max(largest[i - 1][j], largest[i][j - 1]) * grid[i][j]
        
        return largest[-1][-1] % mod if largest[-1][-1] >= 0 else -1


    # def maxProductPath(self, grid: List[List[int]]) -> int:
    #     def traverse(cur_r: int, cur_c: int):
    #         for dr, dy in [(0, 1), (1, 0)]:
    #             r = cur_r + dr
    #             c = cur_c + dy

    #             if 0 <= r < m and 0 <= c < n:
    #                 if grid[r][c] < 0:
    #                     positives[r][c] = max(positives[r][c], negatives[cur_r][cur_c] * grid[r][c])
    #                     negatives[r][c] = min(negatives[r][c], positives[cur_r][cur_c] * grid[r][c])
    #                 else:
    #                     positives[r][c] = max(positives[r][c], positives[cur_r][cur_c] * grid[r][c])
    #                     negatives[r][c] = min(negatives[r][c], negatives[cur_r][cur_c] * grid[r][c])
    #                 traverse(r, c)
        
    #     mod = 1000000007
    #     m, n = len(grid), len(grid[0])
    #     positives = [[-float('inf')] * n for _ in range(m)]
    #     negatives = [[float('inf')] * n for _ in range(m)]
    #     positives[0][0] = grid[0][0]
    #     negatives[0][0] = grid[0][0]
    #     traverse(0, 0)

    #     return positives[-1][-1] % mod if positives[-1][-1] >= 0 else -1

        
def main():
    sol = Solution()
    print(sol.maxProductPath([[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]))
    print(sol.maxProductPath([[1,-2,1],[1,-2,1],[3,-4,1]]))
    print(sol.maxProductPath([[1,3],[0,-4]]))

if __name__ == '__main__':
    main()