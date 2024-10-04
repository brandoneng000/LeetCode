from typing import List

class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        def check_region(i: int, j: int):
            cur = 0

            for row in range(i - 1, i + 2):
                for col in range(j - 1, j + 2):
                    cur += image[row][col]

                    for dr, dc in directions:
                        r = row + dr
                        c = col + dc

                        if i - 1 <= r < i + 2 and j - 1 <= c < j + 2:
                            if abs(image[row][col] - image[r][c]) > threshold:
                                return -1
            
            return cur // 9

        m, n = len(image), len(image[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        averages = [[[] for j in range(n)] for i in range(m)]
        res = [[0 for j in range(n)] for i in range(m)]

        for i in range(1, m - 1):
            for j in range(1, n - 1):
                temp = check_region(i, j)

                if temp != -1:

                    for u in range(i - 1, i + 2):
                        for v in range(j - 1, j + 2):
                            averages[u][v].append(temp)

        for i in range(m):
            for j in range(n):
                if averages[i][j]:
                    res[i][j] = sum(averages[i][j]) // len(averages[i][j])
                else:
                    res[i][j] = image[i][j]
        
        return res

        
def main():
    sol = Solution()
    print(sol.resultGrid(image = [[1,10,5,5],[10,10,5,5],[10,10,5,5]], threshold = 5))
    print(sol.resultGrid(image = [[5,6,7,10],[8,9,10,10],[11,12,13,10]], threshold = 3))
    print(sol.resultGrid(image = [[10,20,30],[15,25,35],[20,30,40],[25,35,45]], threshold = 12))
    print(sol.resultGrid(image = [[5,6,7],[8,9,10],[11,12,13]], threshold = 1))

if __name__ == '__main__':
    main()