from typing import List

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        mod = 12345
        m, n = len(grid), len(grid[0])

        prefix = [1]
        suffix = [1]

        for i in range(m):
            for j in range(n):
                prefix.append((prefix[-1] * grid[i][j]) % mod)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1 , -1, -1):
                suffix.append((suffix[-1] * grid[i][j]) % mod)

        for i in range(m):
            for j in range(n):
                k = i * n + j
                grid[i][j] = (prefix[k] * suffix[-k - 2]) % mod
        
        return grid
    
    # def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
    #     mod = 12345
    #     nums = sum(grid, [])
    #     n = len(nums)
    #     res = [1] * n

    #     prefix = 1
    #     for i in range(n):
    #         res[i] = prefix
    #         prefix = (prefix * nums[i]) % mod

    #     suffix = 1

    #     for i in range(n - 1, -1, -1):
    #         res[i] = (res[i] * suffix) % mod
    #         suffix = (suffix * nums[i]) % mod
        
    #     m, n = len(grid), len(grid[0])
    #     return [[res[i * n + j] for j in range(n)] for i in range(m)]

        
def main():
    sol = Solution()
    print(sol.constructProductMatrix([[1,2],[3,4]]))
    print(sol.constructProductMatrix([[12345],[2],[1]]))

if __name__ == '__main__':
    main()

    