from typing import List

class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        def helper(cur: List[int], select_remain: int, index: int):
            if select_remain == 0:
                total = 0
                for i in range(m):
                    if row_totals[i] <= numSelect:
                        for j in range(n):
                            if matrix[i][j] == 1 and j not in cur:
                                break
                        else:
                            total += 1
                self.res = max(self.res, total)
                return 
            
            for j in range(index, n):
                cur.append(j)
                helper(cur, select_remain - 1, j + 1)
                cur.pop()

        m, n = len(matrix), len(matrix[0])
        row_totals = [sum(matrix[i]) for i in range(m)]
        self.res = 0
        helper([], numSelect, 0)

        return self.res

        
def main():
    sol = Solution()
    print(sol.maximumRows(matrix = [[0,0,0],[1,0,1],[0,1,1],[0,0,1]], numSelect = 2))
    print(sol.maximumRows(matrix = [[1],[0]], numSelect = 1))

if __name__ == '__main__':
    main()