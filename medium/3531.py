from typing import List

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        max_x = {}
        min_x = {}
        max_y = {}
        min_y = {}
        res = 0

        for x, y in buildings:
            max_x[y] = max(max_x.get(y, 0), x)
            min_x[y] = min(min_x.get(y, 100000), x)
            max_y[x] = max(max_y.get(x, 0), y)
            min_y[x] = min(min_y.get(x, 100000), y)

        for x, y in buildings:
            if min_x[y] < x < max_x[y] and min_y[x] < y < max_y[x]:
                res += 1
        
        return res
        
def main():
    sol = Solution()
    print(sol.countCoveredBuildings(n = 3, buildings = [[1,2],[2,2],[3,2],[2,1],[2,3]]))
    print(sol.countCoveredBuildings(n = 3, buildings = [[1,1],[1,2],[2,1],[2,2]]))
    print(sol.countCoveredBuildings(n = 5, buildings = [[1,3],[3,2],[3,3],[3,5],[5,3]]))

if __name__ == '__main__':
    main()