from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        distance = [[float('inf') for i in range(n)] for j in range(m)]
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    distance[i][j] = 0
                else:
                    if i > 0:
                        distance[i][j] = min(distance[i][j], distance[i - 1][j] + 1)
                    if j > 0:
                        distance[i][j] = min(distance[i][j], distance[i][j - 1] + 1)
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i < m - 1:
                    distance[i][j] = min(distance[i][j], distance[i + 1][j] + 1)
                if j < n - 1:
                    distance[i][j] = min(distance[i][j], distance[i][j + 1] + 1)
        
        return distance


def main():
    sol = Solution()
    print(sol.updateMatrix([[1,1,1,1,1,0,1,0,1,0,1,0,1,1,0,1,1,1,0,1,1,1,0,1,1,1,1,0,1,1],
                            [1,1,1,0,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,0,0,1],
                            [1,1,1,1,0,1,0,0,1,1,0,1,1,0,1,1,1,0,1,0,1,0,0,1,0,1,0,1,1,1],
                            [1,1,1,1,1,0,1,1,1,1,1,0,1,1,0,0,0,0,1,0,0,0,0,1,1,1,1,0,0,1],
                            [0,1,0,0,1,0,0,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,0,1]]))
    print(sol.updateMatrix([[1,0,1,1,0,0,1,0,0,1], 
                            [0,1,1,0,1,0,1,0,1,1], 
                            [0,0,1,0,1,0,0,1,0,0], 
                            [1,0,1,0,1,1,1,1,1,1], 
                            [0,1,0,1,1,0,0,0,0,1],
                            [0,0,1,0,1,1,1,0,1,0],
                            [0,1,0,1,0,1,0,0,1,1],
                            [1,0,0,0,1,1,1,1,0,1],
                            [1,1,1,1,1,1,1,0,1,0],
                            [1,1,1,1,0,1,0,0,1,1]]))
    print(sol.updateMatrix([[0,0,0],[0,1,0],[0,0,0]]))
    print(sol.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))

if __name__ == '__main__':
    main()