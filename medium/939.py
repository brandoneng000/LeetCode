from typing import List
import collections

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        x_axis = collections.defaultdict(list)

        for x, y in points:
            x_axis[x].append(y)

        prev_x = {}
        res = float('inf')
        x_coord = sorted(x_axis)

        for x in x_coord:
            col = x_axis[x]
            col.sort()
            for i, y2 in enumerate(col):
                for j in range(i):
                    y1 = col[j]
                    if (y1, y2) in prev_x:
                        res = min(res, (x - prev_x[y1, y2]) * (y2 - y1))
                    prev_x[y1, y2] = x
            
        return res if res < float('inf') else 0


def main():
    sol = Solution()
    print(sol.minAreaRect([[1,1],[1,3],[3,1],[3,3],[2,2]]))
    print(sol.minAreaRect([[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]))

if __name__ == '__main__':
    main()