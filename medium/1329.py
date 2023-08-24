from typing import List
import collections

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        d = collections.defaultdict(list)

        for i in range(m):
            for j in range(n):
                d[i - j].append(mat[i][j])
        
        for key in d:
            d[key].sort(reverse=True)
        
        for i in range(m):
            for j in range(n):
                mat[i][j] = d[i - j].pop()
        
        return mat

    # def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
    #     m, n = len(mat), len(mat[0])
    #     res = [[-1 for j in range(n)] for i in range(m)]

    #     for i in range(m - 1, 0, -1):
    #         cur = []
    #         r, c = i, 0
    #         while r < m and c < n:
    #             cur.append(mat[r][c])
    #             r += 1
    #             c += 1
    #         cur.sort()
    #         r, c = i, 0
    #         index = 0
    #         while r < m and c < n:
    #             res[r][c] = cur[index]
    #             index += 1
    #             r += 1
    #             c += 1
        
    #     for j in range(n):
    #         cur = []
    #         r, c = 0, j
    #         while r < m and c < n:
    #             cur.append(mat[r][c])
    #             r += 1
    #             c += 1
    #         cur.sort()
    #         r, c = 0, j
    #         index = 0
    #         while r < m and c < n:
    #             res[r][c] = cur[index]
    #             index += 1
    #             r += 1
    #             c += 1
        
    #     return res

def main():
    sol = Solution()
    print(sol.diagonalSort([[3,3,1,1],
                            [2,2,1,2],
                            [1,1,1,2]]))
    print(sol.diagonalSort([[11,25,66,1,69,7],
                            [23,55,17,45,15,52],
                            [75,31,36,44,58,8],
                            [22,27,33,25,68,4],
                            [84,28,14,11,5,50]]))

if __name__ == '__main__':
    main()