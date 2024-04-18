from typing import List

class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        def check_dist(x1: int, y1: int, x2: int, y2: int, min_dist: int):
            x = x2 - x1
            y = y2 - y1

            return x * x + y * y <= min_dist

        res = set()

        for x, y, r in circles:
            min_dist = r * r
            for i in range(x - r, x + r + 1):
                for j in range(y - r, y + r + 1):
                    if (i, j) in res:
                        continue
                    if check_dist(x, y, i, j, min_dist):
                        res.add((i, j))
        
        return len(res)

        
def main():
    sol = Solution()
    print(sol.countLatticePoints([[2,2,1]]))
    print(sol.countLatticePoints([[2,2,2],[3,4,1]]))

if __name__ == '__main__':
    main()