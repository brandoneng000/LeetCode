from typing import List

class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        cur = [0]
        res = 0

        for j in range(n):
            if cur[-1] + grid[0][j] <= k:
                res += 1
                cur.append(cur[-1] + grid[0][j])
            else:
                break
        
        cur = cur[1:]

        for i in range(1, m):
            row_sum = 0
            next = []
            for j in range(len(cur)):
                if cur[j] + grid[i][j] + row_sum <= k:
                    res += 1
                    next.append(cur[j] + grid[i][j] + row_sum)
                    row_sum += grid[i][j]
                else:
                    break
            cur = next
        
        return res
        
def main():
    sol = Solution()
    print(sol.countSubmatrices(grid = [[7,6,3],[6,6,1]], k = 18))
    print(sol.countSubmatrices(grid = [[7,2,9],[1,5,0],[2,6,6]], k = 20))

if __name__ == '__main__':
    main()