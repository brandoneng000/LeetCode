from typing import List
from collections import Counter

class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        res = [0] * 5
        count = Counter()

        for x, y in coordinates:
            for i in range(max(0, x - 1), min(m - 1, x + 1)):
                for j in range(max(0, y - 1), min(n - 1, y + 1)):
                    count[(i, j)] += 1
        
        for c in count:
            res[count[c]] += 1
        
        res[0] = (m - 1) * (n - 1) - sum(res)
        return res

        
def main():
    sol = Solution()
    print(sol.countBlackBlocks(m = 3, n = 3, coordinates = [[0,0]]))
    print(sol.countBlackBlocks(m = 3, n = 3, coordinates = [[0,0],[1,1],[0,2]]))

if __name__ == '__main__':
    main()