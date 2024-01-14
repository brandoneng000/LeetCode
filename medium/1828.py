from typing import List

class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = []

        for x, y, r in queries:
            r_sq = r * r
            count = 0
            for u, v in points:
                count += ((x - u) ** 2 + (y - v) ** 2) <= r_sq
            res.append(count)
        
        return res
            
        
def main():
    sol = Solution()
    print(sol.countPoints(points = [[1,3],[3,3],[5,3],[2,2]], queries = [[2,3,1],[4,3,1],[1,1,2]]))
    print(sol.countPoints(points = [[1,1],[2,2],[3,3],[4,4],[5,5]], queries = [[1,2,2],[2,2,2],[4,3,2],[4,3,3]]))

if __name__ == '__main__':
    main()