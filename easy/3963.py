from typing import List

class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        res = [['#'] * n for _ in range(m)]

        for i in range(m):
            res[i][0] = '.'

        for i in range(n):
            res[-1][i] = '.'

        return [''.join(row) for row in res]

def main():
    sol = Solution()
    print(sol.createGrid(m = 2, n = 3))
    print(sol.createGrid(m = 3, n = 3))
    print(sol.createGrid(m = 1, n = 4))

if __name__ == '__main__':
    main()