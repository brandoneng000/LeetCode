from typing import List

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        def helper(row: int, col: int):
            cur = [row, col, row]

            for r in range(row, m):
                if not land[r][col]:
                    break
                cur[-1] = r

            
            cur.append(col)
            for c in range(col, n):
                if not land[row][c]:
                    break
                cur[-1] = c

            res.append(cur)

        m, n = len(land), len(land[0])
        res = []

        for i in range(m):
            for j in range(n):
                if i > 0 and land[i - 1][j] == 1:
                    continue

                if j > 0 and land[i][j - 1] == 1:
                    continue

                if land[i][j] == 1:
                    helper(i, j)
        
        return res
        
def main():
    sol = Solution()
    print(sol.findFarmland([[1,0,0],[0,1,1],[0,1,1]]))
    print(sol.findFarmland([[1,1],[1,1]]))
    print(sol.findFarmland([[0]]))

if __name__ == '__main__':
    main()