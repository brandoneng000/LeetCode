from typing import List
from collections import Counter

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        coord = {}
        row_vals = Counter()
        col_vals = Counter()

        for i in range(m):
            for j in range(n):
                coord[mat[i][j]] = [i, j]
        
        for i, num in enumerate(arr):
            r, c = coord[num]
            row_vals[r] += 1
            col_vals[c] += 1

            if row_vals[r] == n or col_vals[c] == m:
                return i

def main():
    sol = Solution()
    print(sol.firstCompleteIndex(arr = [1,3,4,2], mat = [[1,4],[2,3]]))
    print(sol.firstCompleteIndex(arr = [2,8,7,4,1,3,5,6,9], mat = [[3,2,5],[1,4,6],[8,7,9]]))

if __name__ == '__main__':
    main()