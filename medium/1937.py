from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])

        for i in range(m - 1):
            for j in range(n - 2, -1, -1):
                points[i][j] = max(points[i][j], points[i][j + 1] - 1)
            for j in range(n):
                points[i][j] = max(points[i][j], points[i][j - 1] - 1 if j else 0)
                points[i + 1][j] += points[i][j]
            
        return max(points[-1])

        
def main():
    sol = Solution()
    print(sol.maxPoints([[1,2,3],[1,5,1],[3,1,1]]))
    print(sol.maxPoints([[1,5],[2,3],[4,2]]))

if __name__ == '__main__':
    main()