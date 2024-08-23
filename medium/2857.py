from typing import List
from collections import Counter

class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        n = len(coordinates)
        count = Counter()
        res = 0

        for i in range(n):
            x1, y1 = coordinates[i]
            
            for x in range(k + 1):
                res += count[(x ^ x1, (k - x) ^ y1)]
            
            count[(x1, y1)] += 1
        
        return res
        
def main():
    sol = Solution()
    print(sol.countPairs(coordinates = [[1,2],[4,2],[1,3],[5,2]], k = 5))
    print(sol.countPairs(coordinates = [[1,3],[1,3],[1,3],[1,3],[1,3]], k = 0))

if __name__ == '__main__':
    main()