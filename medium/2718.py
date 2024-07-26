from typing import List

class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        size = len(queries)
        used_row = set()
        used_col = set()
        res = 0

        for i in range(size - 1, -1, -1):
            t, index, val = queries[i]

            if t == 0:
                if index not in used_row:
                    res += val * (n - len(used_col))
                    used_row.add(index)
            else:
                if index not in used_col:
                    res += val * (n - len(used_row))
                    used_col.add(index)
            
            if len(used_row) == n and len(used_col) == n:
                break
        
        return res

        
def main():
    sol = Solution()
    print(sol.matrixSumQueries(n = 3, queries = [[0,0,1],[1,2,2],[0,2,3],[1,0,4]]))
    print(sol.matrixSumQueries(n = 3, queries = [[0,0,4],[0,1,2],[1,0,1],[0,2,3],[1,2,1]]))

if __name__ == '__main__':
    main()