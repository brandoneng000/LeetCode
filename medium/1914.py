from typing import List

class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        layers_count = min(m, n) // 2
        layers = []
        res = [[0 for j in range(n)] for i in range(m)]

        for l in range(layers_count):
            cur = []
            for r in range(l, m - l):
                cur.append(grid[r][l])

            for c in range(l + 1, n - l):
                cur.append(grid[r][c])

            for r in range(r - 1, l - 1, -1):
                cur.append(grid[r][c])

            for c in range(c - 1, l, -1):
                cur.append(grid[r][c])

            layers.append(cur)

        for l, layer in enumerate(layers):
            size = len(layer)
            shift = k % size
            layer = layer[-shift:] + layer[:-shift]

            index = 0
            for r in range(l, m - l):
                res[r][l] = layer[index]
                index += 1

            for c in range(l + 1, n - l):
                res[r][c] = layer[index]
                index += 1

            for r in range(r - 1, l - 1, -1):
                res[r][c] = layer[index]
                index += 1

            for c in range(c - 1, l, -1):
                res[r][c] = layer[index]
                index += 1
                    
        return res
                




def main():
    sol = Solution()
    print(sol.rotateGrid(grid = [[40,10],[30,20]], k = 1))
    print(sol.rotateGrid(grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], k = 2))

if __name__ == '__main__':
    main()