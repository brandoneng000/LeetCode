from typing import List

class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        pos = [-1] * n
        res = 0

        for i in range(n):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 1:
                    pos[i] = j
                    break
        
        for i in range(n):
            k = -1

            for j in range(i, n):
                if pos[j] <= i:
                    res += j - i
                    k = j
                    break

            if k != -1:
                for j in range(k, i, -1):
                    pos[j], pos[j - 1] = pos[j - 1], pos[j]
            else:
                return -1
        
        return res


    # def minSwaps(self, grid: List[List[int]]) -> int:
    #     n = len(grid)
    #     zeroes = []

    #     for row in grid:
    #         z = 0
    #         for bit in row[::-1]:
    #             if bit == 1:
    #                 break
    #             z += 1
            
    #         zeroes.append(z)
        
    #     zero_required = n - 1
    #     res = 0

    #     for i in range(n):
    #         cur_max = -1
    #         cur_max_index = -1

    #         for j in range(i, n):
    #             if zeroes[j] >= zero_required:
    #                 cur_max = zeroes[j]
    #                 cur_max_index = j
    #                 break
            
    #         if cur_max < zero_required:
    #             return -1
            
    #         while cur_max_index > i:
    #             zeroes[cur_max_index], zeroes[cur_max_index - 1] = zeroes[cur_max_index - 1], zeroes[cur_max_index]
    #             cur_max_index -= 1
    #             res += 1
            
    #         zero_required -= 1
        
    #     return res




def main():
    sol = Solution()
    print(sol.minSwaps(grid = [[0,0,1],[1,1,0],[1,0,0]]))
    print(sol.minSwaps(grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]))
    print(sol.minSwaps(grid = [[1,0,0],[1,1,0],[1,1,1]]))

if __name__ == '__main__':
    main()