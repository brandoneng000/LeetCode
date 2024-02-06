from typing import List
from collections import defaultdict

class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        painting = defaultdict(int)
        res = []

        for start, end, color in segments:
            painting[start] += color
            painting[end] -= color

        prev, color = None, 0

        for cur in sorted(painting):
            if color:
                res.append((prev, cur, color))
            
            color += painting[cur]
            prev = cur

        return res
        
def main():
    sol = Solution()
    print(sol.splitPainting(segments = [[1,4,5],[4,7,7],[1,7,9]]))
    print(sol.splitPainting(segments = [[1,7,9],[6,8,15],[8,10,7]]))
    print(sol.splitPainting(segments = [[1,4,5],[1,4,7],[4,7,1],[4,7,11]]))

if __name__ == '__main__':
    main()